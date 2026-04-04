import os
from dotenv import load_dotenv

load_dotenv()

def check_auth(auth: str) -> bool:
    if auth is None:
        return False
    valid_token = os.getenv("AUTH_TOKEN")
    if not valid_token:
        return False
    return auth == valid_token
