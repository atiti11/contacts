import requests

data = {"name": "Hanka", "surname": "Nováková", "email": "anna@novakova.cz", "phone": "+420555666888", "note": "nový uživatel"}
header = {"auth": "NSE5LN40ftVsWkTka7Xg"}
response = requests.post("http://127.0.0.1:8000/contact", data=data, headers=header)
print(response)
print(response.text)
