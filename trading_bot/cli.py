import typer
from bot.client import BinanceClient
from bot.orders import summarize_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

app = typer.Typer()

@app.command()
def trade(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    setup_logging(f"logs/{order_type.lower()}_order.log")

    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"
    base_url = "https://testnet.binancefuture.com"

    client = BinanceClient(api_key, api_secret, base_url)

    try:
        validate_order(symbol, side, order_type, quantity, price)
        order = client.place_order(symbol, side, order_type, quantity, price)
        summary = summarize_order(order)

        typer.echo("✅ Order Request Summary:")
        typer.echo(f"Symbol: {symbol}, Side: {side}, Type: {order_type}, Qty: {quantity}, Price: {price}")
        typer.echo("📊 Order Response:")
        typer.echo(summary)
    except Exception as e:
        typer.echo(f"❌ Error: {e}")

if __name__ == "__main__":
    app()
