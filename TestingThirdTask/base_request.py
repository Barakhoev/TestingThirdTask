import requests


class BaseRequest:
    """Базовый класс для работы с API Petstore"""

    def __init__(self, base_url: str):
        """
        :param base_url: базовый URL тестируемого API
        """
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint: str, params=None, headers=None):
        """GET-запрос"""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        self._log_request("GET", url, None, response)
        return response

    def post(self, endpoint: str, data=None, json=None, headers=None):
        """POST-запрос"""
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=data, json=json, headers=headers)
        self._log_request("POST", url, json or data, response)
        return response

    def put(self, endpoint: str, data=None, json=None, headers=None):
        """PUT-запрос"""
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, data=data, json=json, headers=headers)
        self._log_request("PUT", url, json or data, response)
        return response

    def delete(self, endpoint: str, params=None, headers=None):
        """DELETE-запрос"""
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, params=params, headers=headers)
        self._log_request("DELETE", url, params, response)
        return response

    @staticmethod
    def _log_request(method, url, payload, response):
        """Простое логирование запросов и ответов (для отладки)"""
        print(f"\n[REQUEST] {method} {url}")
        if payload:
            print(f"Payload: {payload}")
        print(f"[RESPONSE] Status: {response.status_code}")
        try:
            print(f"Body: {response.json()}")
        except Exception:
            print("Body: (not JSON)")
