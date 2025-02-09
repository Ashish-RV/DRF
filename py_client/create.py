import requests


endpoint = "http://localhost:8000/api/products/"

data = {"title":"my world is good", "price":189}

get_response = requests.post(endpoint, json=data) # HTTP Request

print(get_response.json())
# print(get_response.status_code)