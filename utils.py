def search_orders(orders,order_id):
    for order in orders:
        if order['order_id'] == order_id:
            return order

def modify_helper(orders, order_id, status):
    for order in orders:
        if order['order_id'] == order_id:

            order['status'] = status
    return orders