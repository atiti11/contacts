authentication_strings = ["NSE5LN40ftVsWkTka7Xg"]
def check_auth(auth: str) -> bool:
    if auth is None:
        return False
    if auth in authentication_strings:
        return True
    else:
         return False