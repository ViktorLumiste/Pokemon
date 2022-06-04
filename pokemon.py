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
                    break

          if poke2.types2 != "":
               for i in range(len(self.double_damage_from)):
                    if self.double_damage_from[i]["name"] == poke2.types2["name"]:
                         self.take_dam2 = 2
                         break

          for i in range(len(self.double_damage_to)):
               if self.double_damage_to[i]["name"] == poke2.types1["name"]:
                    self.deal_dam1 = 2
                    break

          if poke2.types2 != "":
               for i in range(len(self.double_damage_to)):
                    if self.double_damage_to[i]["name"] == poke2.types2["name"]:
                         self.deal_dam2 = 2
                         break

          for i in range(len(self.half_damage_from)):
               if self.half_damage_from[i]["name"] == poke2.types1["name"]:
                    self.take_dam1 = 0.5
                    break

          if poke2.types2 != "":
               for i in range(len(self.half_damage_from)):
                    if self.half_damage_from[i]["name"] == poke2.types2["name"]:
                         self.take_dam2 = 0.5
                         break

          for i in range(len(self.half_damage_to)):
               if self.half_damage_to[i]["name"] == poke2.types1["name"]:
                    self.deal_dam1 = 0.5
                    break

          if poke2.types2 != "":
               for i in range(len(self.half_damage_to)):
                    if self.half_damage_to[i]["name"] == poke2.types2["name"]:
                         self.deal_dam2 = 0.5
                         break

          for i in range(len(self.no_damage_from)):
               if self.no_damage_from[i]["name"] == poke2.types1["name"]:
                    self.take_dam1 = 0
                    break

          if poke2.types2 != "":
               for i in range(len(self.no_damage_from)):
                    if self.no_damage_from[i]["name"] == poke2.types2["name"]:
                         self.take_dam2 = 0
                         break

          for i in range(len(self.no_damage_to)):
               if self.no_damage_to[i]["name"] == poke2.types1["name"]:
                    self.deal_dam1 = 0
                    break

          if poke2.types2 != "":
               for i in range(len(self.no_damage_to)):
                    if self.no_damage_to[i]["name"] == poke2.types2["name"]:
                         self.deal_dam2 = 0
                         break

          self.deal_dam = max(self.deal_dam1, self.deal_dam2)
          self.take_dam = max(self.take_dam1, self.take_dam2)
     def getStats(self):
          stats = self.response_dict["stats"]
          self.hp = stats[0]["base_stat"]
          self.atk = stats[1]["base_stat"]
          self.de = stats[2]["base_stat"]
          self.sp_atk = stats[3]["base_stat"]
          self.sp_de = stats[4]["base_stat"]
          self.speeeeeeed = stats[5]["base_stat"]
     def getPowah(self, poke2, atk_count, def_count):
          if atk_count % 3:
               atk = self.sp_atk
          else:
               atk = self.atk
          if def_count % 2:
               defe = poke2.sp_de
          else:
               defe = poke2.de
          power = atk * self.deal_dam - defe
          return power






poke1 = Pokemon("charizard")
poke2 = Pokemon("bulbasaur")
poke1.getMultiplier(poke2)
poke2.getMultiplier(poke1)
poke1.getStats()
poke2.getStats()
turn = 1
print(poke1.response_dict["stats"])
print(poke2.response_dict["stats"])
if poke1.speeeeeeed >= poke2.speeeeeeed:
     sp_atk1 = 0
     sp_atk2 = 0
     sp_def1 = 0
     sp_def2 = 0
     while poke1.hp > 0 and poke2.hp > 0 and turn <= 100:
          atk1 = poke1.getPowah(poke2,sp_atk1,sp_def2)
          poke2.hp -= atk1
          sp_atk1 += 1
          sp_def2 += 1
          print(poke2.hp)
          atk2 = poke2.getPowah(poke1, sp_atk2, sp_def1)
          poke1.hp -= atk2
          sp_atk2 += 1
          sp_def1 += 1
          print(poke1.hp)
elif poke1.speeeeeeed < poke2.speeeeeeed:
     sp_atk1 = 0
     sp_atk2 = 0
     sp_def1 = 0
     sp_def2 = 0
     while poke1.hp > 0 and poke2.hp > 0 and turn <= 100:
          atk2 = poke2.getPowah(poke1, sp_atk2, sp_def1)
          poke1.hp -= atk2
          sp_atk2 += 1
          sp_def1 += 1
          print(poke1.hp)
          atk1 = poke1.getPowah(poke2, sp_atk1, sp_def2)
          poke2.hp -= atk1
          sp_atk1 += 1
          sp_def2 += 1
          print(poke2.hp)


#print(poke1.andmed)
#double_damage_from
#double_damage_to
#half_damage_from
#half_damage_to
#no_damage_from
#no_damage_to
