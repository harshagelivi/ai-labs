import random


def check_transaction_compliance(transaction_id: str, details: dict) -> dict:
    print(f"[Tool: ComplianceChecker] Checking transaction {transaction_id}")
    is_compliant = random.choice([True, False, True])
    issues = []
    if not is_compliant:
        if details.get("amount", 0) > 1000000:
            issues.append("Large transaction requires enhanced due diligence.")
        if details.get("jurisdiction") == "HighRiskCountry":
            issues.append("Transaction involves a high-risk jurisdiction.")
        if not issues:
            issues.append("General compliance flag triggered.")

    return {
        "transaction_id": transaction_id,
        "compliant": is_compliant,
        "issues": issues
    }
