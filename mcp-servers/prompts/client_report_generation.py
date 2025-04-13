CLIENT_REPORT_PROMPT = """
Generate a client-facing quarterly portfolio performance report based on the provided analysis.
Use clear, professional language suitable for a high-net-worth client at a major bank. Explain
the overall performance, highlight key risk factors identified, and mention any strategic 
adjustments made or recommended. Avoid overly technical jargon.

Portfolio Analysis Data:
{analysis_data}

Client Report:
"""

def format_client_report_prompt(analysis_data: dict) -> str:
    return CLIENT_REPORT_PROMPT.format(analysis_data=str(analysis_data))

