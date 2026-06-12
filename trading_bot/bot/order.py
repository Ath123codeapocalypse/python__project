def summarize_order(order):
    return {
        "orderId": order.get("orderId"),
        "status": order.get("status"),
        "executedQty": order.get("executedQty"),
        "avgPrice": order.get("avgPrice", "N/A")
    }
