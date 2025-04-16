import yaml
from mcp.server.fastmcp import FastMCP

from prompts import client_report_generation, transaction_summary
from resources import market_data, regulatory_docs
from tools import compliance_checker, risk_analyzer

mcp = FastMCP(
    name="Financial-Enterprise-MCP",
    description="MCP Server for enterprise financial services",
    version="1.0.0"
)


@mcp.tool(name="compliance_checker", description="Check transaction compliance")
async def compliance_check_tool(transaction_id: str, details: dict):
    return compliance_checker.check_transaction_compliance(transaction_id, details)


@mcp.tool(name="risk_analyzer", description="Analyze portfolio risk")
async def risk_analyzer_tool(portfolio_id: str, assets: list):
    return risk_analyzer.analyze_portfolio_risk(portfolio_id, assets)


@mcp.resource(uri='stocks://{stock_id}')
async def get_stocks_data(stock_id: str):
    return market_data.get_stock_quote(stock_id)


@mcp.resource(uri='openapi-spec://account-service-apis',
              description='Returns the api spec of the apis that deal with user accounts and their balances')
async def accounts_service_api_spec():
    with open('resources/apis.yaml', 'r') as stream:
        return yaml.safe_load(stream)


@mcp.resource(uri='stocks://{stock_id}')
async def get_stocks_data(stock_id: str):
    return market_data.get_stock_quote(stock_id)


@mcp.resource(uri='compliance://regulatory-docs')
async def get_regulatory_docs():
    return regulatory_docs.get_all_regulatory_documents()


@mcp.prompt()
def get_client_report_prompt(analysis_data: dict) -> str:
    return client_report_generation.format_client_report_prompt(analysis_data)


@mcp.prompt()
def get_transaction_summary(transaction_id) -> str:
    return transaction_summary.format_transaction_summary_prompt(transaction_id)


if __name__ == '__main__':
    mcp.run(transport='sse')
