import json

import requests

#class Pokemon():
with open('pokemonid.json') as json_file:
     data = json.load(json_file)
     # Print the type of data variable
     print("Type:", type(data))


     # Print the data of dictionary
#     print("\nPeople1:", data['url'])
#     print("\nPeople2:", data['name'])
#poke1 = Pokemon()
print(data[0]['url'])