import requests
from lib.settings import base_url

class MyRequests():
    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict =None):
       response = MyRequests._send(url, data, headers, cookies, "get")

       return response

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        response = MyRequests._send(url, data, headers, cookies, "post")

        return response

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f"{base_url}{url}"

        if data is None:
            data = {}
        if cookies is None:
            cookies = {}
        if headers is None:
            headers = {}

        if method == "get":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "post":
            response = requests.post(url, data=data, headers=headers, cookies=cookies)

        return response

