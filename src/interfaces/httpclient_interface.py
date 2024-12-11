from abc import ABC, abstractmethod

from typing import Any, Dict, Optional


class InterfaceHttpClient(ABC):
     
    @abstractmethod
    def get(self, endpoint: str, params: Optional[Dict] = None): ...
    
    @abstractmethod
    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Any] = None): ...
    
    @abstractmethod
    def put(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Any] = None): ...
