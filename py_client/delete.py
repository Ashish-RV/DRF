import requests


endpoint = "http://localhost:8000/api/products/8/delete/"

data = {"title":"Hello World Again","price":155}

get_response = requests.delete(endpoint) # HTTP Request

print(get_response.status_code)
# print(get_response.status_code)