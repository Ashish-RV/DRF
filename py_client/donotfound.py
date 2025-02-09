import requests


endpoint = "http://localhost:8000/api/products/1234"

get_response = requests.get(endpoint) # HTTP Request

print(get_response.json())
# print(get_response.status_code)