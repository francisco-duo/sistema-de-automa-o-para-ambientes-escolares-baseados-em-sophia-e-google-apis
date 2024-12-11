from interfaces.httpclient_interface import InterfaceHttpClient

from typing import Any, Dict, Optional

import requests


class HttpClient(InterfaceHttpClient):
    
    def __init__(self, base_url: str):
        self._base_url = base_url
        
    @property
    def base_url(self):
        return self._base_url
    
    @base_url.setter
    def base_url(self, value: str):
        if not value.startswith("http"):
            raise ValueError("Verifique se a URL começa com 'http' ou 'https'.")
    
    def get(self, endpoint, params = None) -> requests.Response:
        url = f"{self.base_url}/{endpoint.strip('/')}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response

    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Any] = None) -> requests.Response:
        url = f"{self.base_url}/{endpoint.strip('/')}"
        response = requests.post(url, data=data, json=json)
        response.raise_for_status()
        return response

    def put(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Any] = None) -> requests.Response:
        url = f"{self.base_url}/{endpoint.strip('/')}"
        response = requests.put(url, data=data, json=json)
        response.raise_for_status()
        return response