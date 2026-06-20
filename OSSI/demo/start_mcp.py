import subprocess
import os

# Path to the Rhino MCP router executable (the same one configured in Hermes)
ROUTER_PATH = r"/Users/james/Library/Application Support/McNeel/Rhinoceros/packages/8.0/Rhino-MCP-Platform/0.1.5/router/osx-arm64/rhino-mcp-router"

def main():
    """Start the Rhino MCP router in a detached background process.
    This script is intended to be placed in Rhino's startup folder so that the
    router is launched automatically whenever Rhino opens.
    """
    # Ensure the executable exists before trying to launch it
    if not os.path.isfile(ROUTER_PATH):
        raise FileNotFoundError(f"Rhino MCP router not found at {ROUTER_PATH}")

    # Launch the process without attaching its stdout/stderr to the terminal.
    # Using DEVNULL silences the output; the process will stay alive as long
    # as Rhino is running (or until the user kills it).
    subprocess.Popen(
        [ROUTER_PATH],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        close_fds=True,
    )

if __name__ == "__main__":
    main()
