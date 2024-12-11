from google.oauth2 import service_account
from googleapiclient.discovery import build
from typing import List


class GoogleAdminClient:
    
    def __init__(self, service_account_file: str, admin_email: str):
        """
        Inicializa o cliente do Google Admin com autenticação da Service Account.
        
        :param service_account_file: Caminho para o arquivo da service account JSON.
        :param admin_email: Email de um superadministrador do domínio para delegação.
        """
        self.credentials = service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=[
                "https://www.googleapis.com/auth/admin.directory.user",
                "https://www.googleapis.com/auth/admin.directory.group",
            ]
        ).with_subject(admin_email)
        self.service = build("admin", "directory_v1", credentials=self.credentials)

    def create_user(self, primary_email: str, first_name: str, last_name: str, password: str, org_unit: str):
        """
        Cria um novo usuário no Google Admin.
        """
        body = {
            "name": {
                "givenName": first_name,
                "familyName": last_name,
            },
            "password": password,
            "primaryEmail": primary_email,
            "orgUnitPath": org_unit,
            "changePasswordAtNextLogin": True
        }
        return self.service.users().insert(body=body).execute()

    def create_group(self, group_email: str, name: str, description: str):
        """
        Cria um novo grupo no Google Admin.
        """
        body = {
            "email": group_email,
            "name": name,
            "description": description,
        }
        return self.service.groups().insert(body=body).execute()

    def add_member_to_group(self, group_email: str, member_email: str, role: str = "MEMBER"):
        """
        Adiciona um membro a um grupo.
        """
        body = {
            "email": member_email,
            "role": role,
        }
        return self.service.members().insert(groupKey=group_email, body=body).execute()

    def remove_member_from_group(self, group_email: str, member_email: str):
        """
        Remove um membro de um grupo.
        """
        return self.service.members().delete(groupKey=group_email, memberKey=member_email).execute()

    def authenticate_service_account(self):
        """
        Testa a autenticação da service account retornando as informações do domínio.
        """
        return self.service.customer().get(customerKey="my_customer").execute()
