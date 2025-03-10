import requests
from custom_types import SpaceXQuery
from utils import fetch_paginated_data


class Client():

    def __init__(self, base_url: str):
        self.API_URL = base_url

    def _set_endpoint(self, endpoint: str, id: str = None, query: SpaceXQuery = None):
        if id is not None:
            endpoint = f"{endpoint}/{id}"
        else:
            endpoint = f"{endpoint}/query"
        return endpoint

    def _post_request(self, endpoint: str, query: dict = None):
        response = requests.post(
            endpoint, json=query, timeout=20)
        response.raise_for_status()
        return response.json()

    def _get_request(self, endpoint: str, query: dict = None):
        response = requests.get(endpoint, json=query, timeout=20)
        response.raise_for_status()
        return response.json()

    def _fetch_data(self, endpoint: str, id: str = None, query: dict = None):
        try:
            # fetches data using paginated responses
            endpoint = self._set_endpoint(
                endpoint=endpoint, query=query, id=id)
            if id:
                return self._get_request(endpoint)
            if query is not None and "limit" in query['options']:
                return self._post_request(endpoint, query)['docs']
            else:
                return fetch_paginated_data(self, endpoint=endpoint, query=query)
        except requests.exceptions.Timeout:
            raise TimeoutError("Request timed out. Try again later.")
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(
                f"API request failed: {e}")
