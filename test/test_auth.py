import requests
import pytest
from lib.reusable_methods import ReusalbeMethods
from lib.assertions import Assertions
from lib.settings import auth_headers
from lib.my_requests import MyRequests


class TestAuth():
    def test_auth_positive(self):
        response = MyRequests.get("/ping", headers=auth_headers)
        Assertions.assert_key_value(response,
                                    "api_key_info",
                                    "Ключ доступа валиден",
                                    f"The value of api_key_info is not equal to 'Ключ доступа валиден'")

    # def test_auth_no_api_key(self):
    #     response = requests.get("http://vs-msk01-app01t/eapteka_t_artamonova2/hs/partners_api2_0/v2/ping",
    #                             headers={"Authorization": "Basic dGVzdF9hcGk6MTIzNDU2"})
    #
    #     assert response.status_code == 401
    #     # Assertions.assert_key_value(response,
    #     #                             "description",
    #     #                             "Не передано значение параметра 'api_key',
    #     #                             f"The key 'description' is not equal to "Не передано значение параметра 'api_key'")
    #
    # def test_auth_no_authorization(self):#status code 401
    #
    # def test_auth_wrong_api_key(self):
    #      Assertions.assert_key_value(response,
    #                              "description",
    #                                  "Невалидный токен", f"The value of key 'description' is not equal to 'Невалидный токен'"
    #
    #
    # def test_auth_wrong_authorization(self):




