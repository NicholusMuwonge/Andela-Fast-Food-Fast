import unittest 
import run
from run import app
 
 

class Test_api(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.orders = [{"order_id":1,"user_id":"user1","item_ordered":"chicken",
        "item_quantity":"2kg"}]
        self.new_order = {"order_id":2,"user_id":"user2","item_ordered":"beef",
        "item_quantity":"5kg"}

    def tearDown(self):
        print('TearDown')

    def place_order_helper(self,new_order):
        self.new_order = new_order
        return self.app.post('http://127.0.0.1/api/v1/orders', data = jsonify(self.new_order) , follow_redirects = True ) 

    def test_place_order(self):
        response =  place_order_helper(self.new_order)
        self.assertEqual(response.status_code,201)

    def get_orders_helper(self):
        return self.app.get('http://127.0.0.1:5000/api/v1/orders', follow_redirects=True)

    def test_get_orders(self):
        response = self.get_orders_helper()
        self.assertEqual(response.status_code,200)

    def get_one_order_helper(self,order_id=1):
        return self.app.get('http://127.0.0.1:5000/api/v1/orders/<int:order_id>', follow_redirects = True)

    def test_get_one_order(self):
        response = get_one_order_helper()
        self.assertEqual(response.status_code,200)

    def modify_order_helper(self,status="Accepted"):
        return self.app.put('http://127.0.0.1:5000/api/v1/orders/1', data = jsonify(status), follow_redirects=True)
        
    def test_modify_order(self):
        self.assertEqual(response.status_code,201)

    
        


if __name__ == '__main__':
    unittest.main() 