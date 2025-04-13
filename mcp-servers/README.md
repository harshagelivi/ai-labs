# MCP Server for Financial SaaS

This is an enterprise-grade MCP (Multi-Component Prompt) server tailored for a company providing SaaS solutions to the world's largest banks. Built with FastMCP, it demonstrates how to structure tools, resources, and prompts for financial services applications.

## Setup

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run the server:
    ```bash
    uv run mcp_server.py
    ```

## Architecture

The server uses FastMCP, a specialized framework for building MCP servers with the following components:

-   **Tools:** Actions the system can perform
    - Compliance Checker: Validates financial transactions against regulatory requirements
    - Risk Analyzer: Evaluates portfolio risk profiles for client assets, providing risk scores and key risk factors

-   **Resources:** Data sources the system can query
    - Market Data: Real-time stock quotes (with price, change percentage, volume) and FX rates
    - Regulatory Documents: Searchable database of financial regulations

-   **Prompts:** Pre-defined templates for specific tasks
    - Transaction Summary: Generates concise summaries of complex transactions
    - Client Report Generation: Creates client-facing portfolio performance reports

The server is structured as follows:
```
mcp-servers/
├── mcp_server.py         # Main server file with FastMCP configuration
├── prompts/              # Prompt templates
│   ├── client_report_generation.py
│   └── transaction_summary.py
├── resources/            # Data sources
│   ├── market_data.py    # Stock quotes and FX rates
│   └── regulatory_docs.py
└── tools/                # Action components
    ├── compliance_checker.py
    └── risk_analyzer.py
```

The server exposes resources through URI patterns (e.g., `stocks://{stock_id}` for stock data) and registers tools and prompts that can be invoked via the API endpoints.

## API Endpoints

- `GET /`: Server status
- `GET /components`: List all available tools, resources, and prompts
- `POST /execute`: Execute MCP tasks (example: portfolio risk analysis)

## Integration with Claude Desktop

To connect this MCP server to Claude Desktop:

1. Ensure the server is running locally
2. Configure Claude Desktop by editing the configuration file at `~/Library/Application Support/Claude/claude_desktop_config.json`
3. Add the following configuration:

```json
{
  "mcpServers": {
    "fis-server": {
      "command": "npx",
      "args": ["mcp-remote", "http://localhost:8000/sse"]
    }
  }
}
```

4. Restart Claude Desktop to apply the changes
5. Claude will now have access to the financial tools and resources provided by this MCP server

## Using MCP Inspector

The MCP Inspector provides a visual interface for debugging and testing the MCP server:

1. Install the MCP Inspector package if you haven't already:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Start the server with the inspector:
   ```bash
   npx @modelcontextprotocol/inspector uv --directory . run mcp_server
   ```

3. The inspector will launch in your browser, allowing you to:
   - View available components (tools, resources, prompts)
   - Test individual components
   - Monitor MCP traffic between Claude and the server
   - Debug issues with component execution
