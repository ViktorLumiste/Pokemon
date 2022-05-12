import json
import requests
class Pokemon():
     def __init__(self, name):
          self.input_name = name
     with open('pokemonid.json') as json_file:
          data = json.load(json_file)
     i = 0
     for poke in data:
          if input_name == data[i]["name"]:
               pokeurl = (data[i]["url"])
               i += 1
          else:
               i += 1
     response = requests.get(pokeurl)
     response_dict = response.json()
     failname = input_name + ".json"
     andmed = requests.get(pokeurl).json()
     with open(failname, 'w') as json_file:
          json.dump(andmed, json_file)
     tyybid = andmed["types"]
     if len(tyybid) > 1:
          types1 = tyybid[0]["type"]
          types2 = tyybid[1]["type"]
     else:
          types1 = tyybid[0]["type"]
          types2 = ""
     def getTypes(self, tyyp1, tyyp2):
          if tyyp2 != "":
               response1 = requests.get(self.types1["url"])
               response_dict1 = response1.json()
               response2 = requests.get(self.types2["url"])
               response_dict2 = response2.json()
               print(response_dict1["damage_relations"])
               print(response_dict2["damage_relations"])
          else:
                response1 = requests.get(self.types1["url"])
                response_dict1 = response1.json()
                print(response_dict1["damage_relations"])
     def getMultiplier(self,poke1, poke2):
          for typ in self.poke1.response_dict1:
               for a in typ:
                    if a["name"] == poke2.types1:
                         pass
poke1 = Pokemon()
poke1.getTypes(poke1.types1, poke1.types2)

#print(poke1.data[0]['url'])