"""
python 3.12.4

Sistema de automação para ambientes escolares baseados em sophia e google api's.
"""
import os
import time

from config.environments_config import get_environments
from utils.email_domain import return_domain_and_orgunit
from resources.httpclient_resources import HttpClient


if __name__ == "__main__":
    environments = get_environments()
    
    user = environments["sophia"]["user"]
    password = environments["sophia"]["password"]
    
    if not user or not password:
        raise KeyError("Os valores de 'user' e 'password' são obrigatórios.")
    
    client = HttpClient(base_url=environments["sophia"]["base"])
    
    # Auth sophia client
    auth = {"token": client.post(endpoint="Autenticacao", json={"usuario": user, "senha": password}).text}

    # List students
    students = client.get(endpoint=environments["sophia"]["students"], headers=auth, params={"Periodos": 165})
    
    # List sophia classrooms
    sophia_classrooms = client.get(endpoint=environments["sophia"]["classroom"], headers=auth, params={"Periodos": 165})
    
    for student in students:
        for classroom in student["turmas"]:
            print(return_domain_and_orgunit(classroom["descricao"]))

    # Create new user with google api.
    # Create new groups with google api.
    