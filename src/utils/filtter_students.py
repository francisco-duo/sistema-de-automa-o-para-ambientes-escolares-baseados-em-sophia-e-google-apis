from typing import Dict

from .email_domain import return_domain_and_orgunit


def student_body(student: Dict) -> Dict:
    if student.get("email"):
        pass
    
    for classroom in student.get("turmas", []):
        domain, orgunit = return_domain_and_orgunit(classroom["descricao"])
        
        # Create email in correct format
        first_name = student["nome"].split()[0]
        email = f"{first_name}{student['codigoExterno']@{domain}}".lower()
        
        user_data = {
                "primaryEmail": email,
                "name": {
                    "givenName": first_name,
                    "familyName": ' '.join(student["nome"].split()[1:])  # Sobrenome
                },
                "password": f"cci{student['codigoExterno']}",  # Defina uma senha inicial
                "orgUnitPath": orgunit,  # Unidade organizacional baseada na turma
                "changePasswordAtNextLogin": True  # Obrigar o usuário a alterar a senha no próximo login
            }
    