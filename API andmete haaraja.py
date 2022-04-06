import requests
import json
url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=100000"
response = requests.get(url)
print("Status code: ", response.status_code)
response_dict = response.json()
print(response_dict)
with open("pokemonid.json", "a") as outfile:
    outfile.write("[ \n")
for poke in response_dict["results"]:
    pokemon = json.dumps(poke, indent=4)
    with open("pokemonid.json", "a") as outfile:
        outfile.write(pokemon)
        outfile.write(", \n")
with open("pokemonid.json", "a") as outfile:
    outfile.write("]")

    print(poke)
    print(pokemon)
