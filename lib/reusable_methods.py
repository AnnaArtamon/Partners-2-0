import json
import requests
from requests import Response


class ReusalbeMethods:
    def get_json_value_by_key(self, response: Response, key):
        assert response.status_code == 200, f"Response status code is not 200, it's {response.status_code}"
        try:
            response_as_json = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. The response text is '{response.text}"

        assert key in response_as_json, f"Response JSON doesn't have key {key}"
        return response_as_json[key]

