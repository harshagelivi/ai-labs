import random
from datetime import datetime


def get_stock_quote(ticker: str) -> dict:
    print(f"[Resource: MarketData] Fetching quote for {ticker}")
    price = round(random.uniform(50.0, 500.0), 2)
    change = round(random.uniform(-5.0, 5.0), 2)
    volume = random.randint(100000, 5000000)
    return {
        "ticker": ticker.upper(),
        "price": price,
        "change_percent": round((change / (price - change)) * 100, 2) if (price - change) != 0 else 0,
        "volume": volume,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


def get_fx_rate(currency_pair: str) -> dict:
    print(f"[Resource: MarketData] Fetching FX rate for {currency_pair}")
    # Simulate fetching data
    rate = round(random.uniform(0.8, 1.5), 4)
    return {
        "pair": currency_pair.upper(),
        "rate": rate,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
