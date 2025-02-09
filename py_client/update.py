import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {"title":"Hello World Again","price":155}

get_response = requests.put(endpoint, json=data) # HTTP Request

print(get_response.json())
# print(get_response.status_code)