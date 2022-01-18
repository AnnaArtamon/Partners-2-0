import json
from lib.assertions import Assertions
from lib.settings import auth_headers, order_body
from lib.my_requests import MyRequests


class TestOrders():
    def test_order_positive(self):
        response = MyRequests.post("/orders", headers=auth_headers, data=order_body.encode('utf-8'))
        external_id = json.loads(order_body)["orders"][0]["external_id"]
        Assertions.assert_accepted(response, external_id, f"{external_id} is not in accepted array")