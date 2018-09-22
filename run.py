from flask import Flask, Response,abort, render_template, url_for, request, redirect, session, make_response,jsonify
import json 
from App.utils import search_orders, modify_helper 
app = Flask(__name__)

orders = [] 
@app.route("/api/v1/orders", methods= ['GET'])
def all_orders():
    return make_response(jsonify(orders)),200

@app.route("/api/v1/orders/<int:order_id>", methods= ['GET'])
def fetch_one_order(order_id):
    order = search_orders(orders, order_id)
    if order is None:
        abort(404)
    else:
        return make_response(jsonify(order)),200

@app.route("/api/v1/orders", methods= ['POST'])
def place_order():
    data = request.json
    if len(orders) == 0:
        order_id = 1
        orders.append({'order_id' : order_id,'user_id': data.get('user_id'),'item_ordered': data.get('item_ordered'),
              'item_quantity':data.get('item_quantity') })
    else:
        last_dict = orders[len(orders)-1]
        id = int(last_dict['order_id'])
        new_id = id + 1 
        orders.append({'order_id' : new_id, 'user_id' : data.get('user_id'),'item_ordered' : data.get('item_ordered'), 'item_quantity': data.get('item_quantity')} )
    
    return make_response(jsonify(orders)),200

@app.route("/api/v1/orders/<int:order_id>", methods= ['PUT'])
def modify_order(order_id):
     data = request.json
     if data:
         status = data.get('status')
         response =  modify_helper(orders,order_id,status)

     return  make_response(jsonify(response)),200



if __name__ == '__main__':
    app.run(debug=True)
