**Connecting the Rhino MCP plugin to Hermes**

Hermes can talk to any MCP‑compatible server via its **native MCP client** (see `hermes-agent → references/native-mcp.md`).  All you need is:

1. a working MCP server for Rhino (the “Rhino MCP plugin” you just installed), and
2. an entry in `~/.hermes/config.yaml` that tells Hermes how to reach it.

Below is a complete, step‑by‑step guide tailored to the typical Rhino MCP installation on macOS.

---

## 1️⃣ Install the MCP SDK (once per machine)

The native client is enabled only if the Python package **`mcp`** is present.

```bash
# In your user environment (no need for a virtualenv)
python3 -m pip install --upgrade mcp   # or: uv pip install mcp
```

> **Why?**
> `hermes-agent` checks for `import mcp`. If the import fails, it silently skips all MCP discovery, so you won’t see any `mcp_*` tools.

---

## 2️⃣ Make sure the Rhino MCP server is runnable

The Rhino plugin ships a small executable (usually called **`rhino-mcp`** or **`RhinoMCPServer`**) that speaks the MCP protocol over **stdio** or **HTTP**.

*If you installed the plugin via a package manager*, locate the binary:

```bash
# Example paths – adjust to your install location
which rhino-mcp                      # should print something like /usr/local/bin/rhino-mcp
# If that fails, look inside the Rhino plug‑in folder:
ls ~/Library/Application\ Support/Rhino/PlugIns/MCP/
```

Run it once manually to verify it starts without errors:

```bash
rhino-mcp --help   # should show usage / version info
```

If the server needs a working directory (e.g. where Rhino stores its models), note that path— you’ll pass it in the config.

---

## 3️⃣ Add an MCP entry to `~/.hermes/config.yaml`

Open the Hermes config for editing:

```bash
hermes config edit          # opens $EDITOR at ~/.hermes/config.yaml
```

Insert (or update) a top‑level key called **`mcp_servers`**.  You have two transport options; pick the one that matches your Rhino server.

### 3A️⃣ Stdio transport (most common for local plugins)

```yaml
mcp_servers:
  rhino:
    command: "rhino-mcp"               # exact binary name you verified above
    args: []                            # extra CLI flags if needed, e.g. ["--port", "10500"]
    env:                               # optional – only expose what the server needs
      RHI_NO_GUI: "1"                  # example of a safe env var; secrets never passed unless you list them
    timeout: 120                        # per‑tool call limit (seconds)
    connect_timeout: 30                 # how long Hermes waits for the server to start
```

*Notes*

- **Never expose your full shell environment** – Hermes filters everything except a safe whitelist. If Rhino needs an API key, add it under `env:` explicitly.
- The command is launched once at agent startup and kept alive for the entire session, so you don’t need a port number here.

### 3B️⃣ HTTP/Streamable‑HTTP transport (if the plugin runs as a background service)

If your Rhino MCP server is already listening on localhost:10500 (the “MCPStart part”), use the URL form:

```yaml
mcp_servers:
  rhino:
    url: "http://127.0.0.1:10500/mcp"   # exact endpoint that speaks the MCP protocol
    headers:
      Authorization: "Bearer <YOUR_TOKEN_IF_ANY>"
    timeout: 120
    connect_timeout: 30
```

*Make sure the server’s HTTP mode is enabled; otherwise Hermes will fail to negotiate.*

---

## 4️⃣ Restart Hermes so it picks up the new config

```bash
# If you’re running the CLI:
hermes   # start a fresh session (or press /reset inside an interactive chat)

# If you run Hermes as a gateway service, restart that process:
pkill -f hermes          # stop any existing daemon
hermes &                 # launch again (or use your systemd/launchctl command)
```

During startup you should see logs like:

```
[INFO] Discovering MCP servers…
[INFO] Connecting to MCP server “rhino” via stdio …
[INFO] Discovered 7 tools from MCP server “rhino”
```

If those messages appear, the native client succeeded and the server’s tools are now part of Hermes’ toolset.

---

## 5️⃣ Use the newly‑registered tools

All MCP tools are prefixed with **`mcp_<server>_`**.  Run `hermes tools list` (or `/tools` in an interactive chat) to see them.

Typical Rhino–MCP tool names might be:

| Prefix | Example |
|--------|---------|
| `mcp_rhino_get_current_time` | Returns the current Rhino server time |
| `mcp_rhino_list_sessions`    | Lists active Rhino sessions |
| `mcp_rhino_run_command`      | Executes a Rhino‑specific command (e.g. “ExportModel”) |
| `mcp_rhino_read_file`        | Reads a file from the Rhino data folder |
| `mcp_rhino_write_file`       | Writes a file into the Rhino workspace |

#### Example usage inside Hermes:

```text
User: What are the currently running Rhino sessions?
Hermes (calls tool):
{
  "tool_calls": [
    {
      "name": "mcp_rhino_list_sessions",
      "arguments": {}
    }
  ]
}
```

The LLM will receive the JSON result and can answer:

> “There are two active Rhino sessions: `session‑a1b2c3` (started 10 min ago) and `session‑d4e5f6` (started 2 h ago).”

You can also **combine** MCP tools with ordinary Hermes tools. For instance, read a file produced by Rhino and then parse it:

```text
User: Give me the first 20 lines of the export log from session “session‑a1b2c3”.
Hermes:
{
  "tool_calls": [
    {
      "name": "mcp_rhino_read_file",
      "arguments": { "path": "/exports/session-a1b2c3/log.txt" }
    },
    {
      "name": "read_file",               # standard Hermes file tool
      "arguments": { "path": "/tmp/last_mcp_output.txt", "offset": 1, "limit": 20 }
    }
  ]
}
```

(You’d normally pipe the MCP output to a temporary file first; the exact workflow can be scripted with `terminal` if you prefer.)

---

## 6️⃣ (Optional) Verify the connection manually

If you ever need to debug:

```bash
hermes mcp list               # shows all configured servers and their status
hermes mcp test rhino          # performs a quick “list_tools” round‑trip and prints any error
```

A successful test prints something like:

```
[OK] MCP server “rhino” responded – 7 tools discovered.
```

If it fails, the log will include the filtered stderr of the subprocess or HTTP error code.

---

## 7️⃣ Security & Best Practices

| Concern | Recommendation |
|---------|----------------|
| **Secrets leakage** | Only put secrets under `env:` (stdio) or `headers:` (HTTP). Hermes redacts them from any tool output. |
| **Tool name collisions** | The prefix (`mcp_rhino_`) guarantees uniqueness, even if two MCP servers expose a `read_file` tool. |
| **Server stability** | Keep the MCP process running in the background (e.g., via `launchctl` or a simple `nohup rhino-mcp &`). Hermes will automatically reconnect on disconnects. |
| **Version compatibility** | The native client works with any MCP 1.x server spec. If Rhino updates its server, you only need to restart Hermes – no code changes required. |
| **Auditing** | Set `hermes config set logging.level debug` and watch `~/.hermes/logs/agent.log` for connection attempts. |

---

## 📋 TL;DR Cheat Sheet

```bash
# 1️⃣ Install MCP SDK
python3 -m pip install --upgrade mcp

# 2️⃣ Verify Rhino MCP binary exists
which rhino-mcp    # should resolve to /usr/local/bin/rhino-mcp

# 3️⃣ Add config (edit ~/.hermes/config.yaml)

mcp_servers:
  rhino:
    command: "rhino-mcp"
    args: []                     # add --port 10500 if you need it
    env: {}
    timeout: 120
    connect_timeout: 30

# 4️⃣ Restart Hermes
pkill -f hermes   # optional, only if a daemon is running
hermes             # start fresh CLI session (or restart your gateway)

# 5️⃣ List discovered tools
hermes tools list | grep rhino
```

Now you can call any `mcp_rhino_…` tool directly from within Hermes, giving you full programmatic access to the Rhino MCP plugin without ever leaving the chat.

---

**That’s it!** Once those steps are done, Hermes will treat the Rhino MCP server exactly like a built‑in toolset. If anything goes wrong—missing binary, connection timeout, or unexpected tool names—run `hermes mcp test rhino` and share the error output; we can troubleshoot further from there. Happy modeling!