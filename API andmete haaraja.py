import requests
url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=100000"
response = requests.get(url)
print("Status code: ", response.status_code)
response_dict = response.json()
