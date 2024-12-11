import os

from dotenv import load_dotenv

load_dotenv()


def get_environments():
    return {
        "sophia": {
            "base": os.getenv("SOPHIA_BASE"),
            "auth": os.getenv("SOPHIA_AUTH"),
            "classroom": os.getenv("SOPHIA_CLASSROOM"),
            "students": os.getenv("SOPHIA_STUDENT"),
            "user": os.getenv("SOPHIA_USER"),
            "password": os.getenv("SOPHIA_PASSWORD"),
        },
        "google": {
            "scopes": [
                    os.getenv("GOOGLE_SCOPE_USER"),
                    os.getenv("GOOGLE_SCOPE_GROUP"),
                ],
            "service_account_file": os.getenv("GOOGLE_CREDENTIAL"),
            "service_account_email": os.getenv("GOOGLE_EMAIL")
        }
    }
