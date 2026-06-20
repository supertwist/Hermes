---
Model: gpt-oss:120b
Prompt: "I am a designer who uses Rhino 8. Are there MCPs for Rhino 8? If the are more than one, create a comparison table with the following columns: - name of tool - link to download - a short summary of the scope of fuctionality Do not leave any cells blank. If you are unsure, at any point, ask me for guidance. For the source links: check that they are live; if 404 then do not include. For the referrer links: check that they are live if no referrer links can be found, do not include the source. Save the result as \"Rhino-research.md\" to /Users/james/GIT/Hermes/OSSI/demo Prepend the model used, the prompt (remove any special characters that violate YAML conventions), and the date it was generated to the beginning of the document in the following YAML structure: — Model: (model name) Prompt: (insert prompt) Date: (insert yy/mm/dd) —"
Date: 26/06/2026
---

| Name of Tool | Download Link | Summary |
|--------------|---------------|---------|
| RhinoMCP (jingcheng-chen) | https://github.com/jingcheng-chen/rhinomcp/releases/download/releases/0.3.1/rhinomcp-0.3.1-rh8_17-any.yak | A Model Context Protocol plugin for Rhino 8 that adds Grasshopper preview capture, batched component I/O inspection, improved graph creation/editing, and transient retry handling for socket requests. |
| RhinoMCP (mcneel) | https://github.com/mcneel/RhinoMCP/releases/download/plugin-v0.1.5/rhino-mcp-platform-0.1.5-rh8_29-mac.yak | Official MCP server plugin targeting Rhino 8, providing a TCP socket interface with support for geometry creation, slot logic, and NUnit‑based testing across macOS and Windows builds. |
| RhinoAIBridge (tanishqbhattad) | https://github.com/tanishqbhattad/rhino-mcp/releases/download/v4.8.0/RhinoAIBridge-v4.8.0.zip | A comprehensive AI bridge for Rhino 8 implementing Protocol 5 with multiplexed connections, idempotent retries, cooperative cancellation, binary image frames, and extensive toolset (~115 tools) for architectural modeling workflows. |
