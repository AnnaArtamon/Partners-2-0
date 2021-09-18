import json
from requests import Response


class Assertions:
    @staticmethod
    def assert_key_value(response: Response, key, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. The text of the response is {response.text}"
        assert key in response_as_dict, f"There's no key {key} in the response"
        assert response_as_dict[key] == expected_value, f"{error_message}"

    @staticmethod
    def assert_accepted(response: Response, expected_value, error_message):
        key = "accepted"
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. The text of the response is {response.text}"
        assert key in response_as_dict, f"There's no key {key} in the response"
        assert response_as_dict[key][0] == expected_value, f"{error_message}"

    def assert_rejected(response: Response, expected_value, error_message):
        key = "rejected"
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. The text of the response is {response.text}"
        assert key in response_as_dict, f"There's no key {key} in the response"
        assert response_as_dict[0][key][0] == expected_value, f"{error_message}"
        print(response_as_dict[0][key][0])