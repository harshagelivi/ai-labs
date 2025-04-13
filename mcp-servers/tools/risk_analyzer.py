import random


def analyze_portfolio_risk(portfolio_id: str, assets: list) -> dict:
    print(f"[Tool: RiskAnalyzer] Analyzing portfolio {portfolio_id}")
    risk_score = round(random.uniform(0.1, 0.9), 2)
    factors = []
    if risk_score > 0.7:
        factors.append("High concentration in volatile tech stocks.")
    if risk_score > 0.5:
        factors.append("Significant exposure to emerging markets debt.")
    if not factors and risk_score > 0.3:
        factors.append("Moderate currency exchange risk detected.")
    if not factors:
        factors.append("Standard market risk.")

    return {
        "portfolio_id": portfolio_id,
        "risk_score": risk_score,
        "key_factors": factors
    }
