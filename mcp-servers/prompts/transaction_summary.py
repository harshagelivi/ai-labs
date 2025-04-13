TRANSACTION_SUMMARY_PROMPT = """
Generate a concise summary for the following financial transaction intended for an internal risk
 review meeting. Focus on the key details, counterparties, amount, jurisdiction, and any potential 
 compliance flags.

Transaction Details:
{transaction_data}

"""


def format_transaction_summary_prompt(transaction_id: dict) -> str:
    return TRANSACTION_SUMMARY_PROMPT.format(transaction_data=str(transaction_id))
