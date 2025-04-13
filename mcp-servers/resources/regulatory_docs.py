REGULATORY_DB = {
    "Basel III Capital Adequacy": {
        "id": "REG-001",
        "summary": "Requirements for minimum capital reserves based on risk-weighted assets.",
        "keywords": ["capital", "risk", "basel", "adequacy"]
    },
    "MiFID II Investor Protection": {
        "id": "REG-002",
        "summary": "Rules governing transparency and investor protection in financial markets.",
        "keywords": ["mifid", "investor", "protection", "transparency"]
    },
    "AML/KYC Procedures": {
        "id": "REG-003",
        "summary": "Anti-Money Laundering and Know Your Customer requirements for financial institutions.",
        "keywords": ["aml", "kyc", "laundering", "customer", "due diligence"]
    }
}


def get_all_regulatory_documents():
    results = []
    for title, data in REGULATORY_DB.items():
        results.append({
            "document_id": data['id'],
            "title": title,
            "summary": data['summary'],
        })
    return results


def find_regulatory_document(query: str) -> list:
    print(f"[Resource: RegulatoryDocs] Searching for documents matching '{query}'")
    query_terms = query.lower().split()
    results = []
    for title, data in REGULATORY_DB.items():
        # Simple keyword matching
        match_score = 0
        for term in query_terms:
            if term in title.lower() or any(term in kw for kw in data['keywords']):
                match_score += 1
        if match_score > 0:
            results.append({
                "document_id": data['id'],
                "title": title,
                "summary": data['summary'],
                "match_score": match_score
            })
    results.sort(key=lambda x: x['match_score'], reverse=True)
    return results[:3]
