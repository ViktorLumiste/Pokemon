import json
import requests
class Pokemon():
     def __init__(self, name):
          self.input_name = name
          with open('pokemonid.json') as json_file:
               data = json.load(json_file)
          i = 0
          for poke in data:
               if self.input_name == data[i]["name"]:
                    pokeurl = (data[i]["url"])
                    i += 1
               else:
                    i += 1
          self.response = requests.get(pokeurl)
          self.response_dict = self.response.json()
          self.failname = self.input_name + ".json"
          self.andmed = requests.get(pokeurl).json()
          with open(self.failname, 'w') as json_file:
               json.dump(self.andmed, json_file)
          self.tyybid = self.andmed["types"]
          if len(self.tyybid) > 1:
               self.types1 = self.tyybid[0]["type"]
               self.types2 = self.tyybid[1]["type"]
          else:
               self.types1 = self.tyybid[0]["type"]
               self.types2 = ""
          if self.types2 != "":
               response1 = requests.get(self.types1["url"])
               self.response_dict1 = response1.json()
               response2 = requests.get(self.types2["url"])
               self.response_dict2 = response2.json()
          else:
                response1 = requests.get(self.types1["url"])
                self.response_dict1 = response1.json()
     def getMultiplier(self, poke2):
          self.take_dam = 1
          self.take_dam1 = 1
          self.take_dam2 = 1
          self.deal_dam = 1
          self.deal_dam1 = 1
          self.deal_dam2 = 1
          self.double_damage_from = self.response_dict1["damage_relations"]["double_damage_from"]
          self.double_damage_to = self.response_dict1["damage_relations"]["double_damage_to"]
          self.half_damage_from = self.response_dict1["damage_relations"]["half_damage_from"]
          self.half_damage_to = self.response_dict1["damage_relations"]["half_damage_to"]
          self.no_damage_from = self.response_dict1["damage_relations"]["no_damage_from"]
          self.no_damage_to = self.response_dict1["damage_relations"]["no_damage_to"]
          for i in range(len(self.double_damage_from)):
               if self.double_damage_from[i]["name"] == poke2.types1["name"]:
                    self.take_dam1 = 2

          if poke2.types2 != "":
               for i in range(len(self.double_damage_from)):
                    if self.double_damage_from[i]["name"] == poke2.types2["name"]:
                         self.take_dam2 = 2

          for i in range(len(self.double_damage_to)):
               if self.double_damage_to[i]["name"] == poke2.types1["name"]:
                    self.deal_dam1 = 2

          if poke2.types2 != "":
               for i in range(len(self.double_damage_to)):
                    if self.double_damage_to[i]["name"] == poke2.types2["name"]:
                         self.deal_dam2 = 2

          for i in range(len(self.half_damage_from)):
               if self.half_damage_from[i]["name"] == poke2.types1["name"]:
                    self.take_dam1 = 0.5

          if poke2.types2 != "":
               for i in range(len(self.half_damage_from)):
                    if self.half_damage_from[i]["name"] == poke2.types2["name"]:
                         self.take_dam2 = 0.5

          for i in range(len(self.half_damage_to)):
               if self.half_damage_to[i]["name"] == poke2.types1["name"]:
                    self.deal_dam1 = 0.5

          if poke2.types2 != "":
               for i in range(len(self.half_damage_to)):
                    if self.half_damage_to[i]["name"] == poke2.types2["name"]:
                         self.deal_dam2 = 0.5

          for i in range(len(self.no_damage_from)):
               if self.no_damage_from[i]["name"] == poke2.types1["name"]:
                    self.take_dam1 = 0

          if poke2.types2 != "":
               for i in range(len(self.no_damage_from)):
                    if self.no_damage_from[i]["name"] == poke2.types2["name"]:
                         self.take_dam2 = 0

          for i in range(len(self.no_damage_to)):
               if self.no_damage_to[i]["name"] == poke2.types1["name"]:
                    self.deal_dam1 = 0

          if poke2.types2 != "":
               for i in range(len(self.no_damage_to)):
                    if self.no_damage_to[i]["name"] == poke2.types2["name"]:
                         self.deal_dam2 = 0

          self.deal_dam = max(self.deal_dam1, self.deal_dam2)
          self.take_dam = max(self.take_dam1, self.take_dam2)


poke2 = Pokemon("ivysaur")
poke1 = Pokemon("bulbasaur")
print(poke1.getMultiplier(poke2))
print(poke1.take_dam1)
print(poke1.take_dam2)
print(poke1.take_dam)
print(poke1.deal_dam1)
print(poke1.deal_dam2)
print(poke1.deal_dam)
print(poke1.types1)
print(poke1.response_dict1["damage_relations"])

#print(poke1.andmed)
#double_damage_from
#double_damage_to
#half_damage_from
#half_damage_to
#no_damage_from
#no_damage_to