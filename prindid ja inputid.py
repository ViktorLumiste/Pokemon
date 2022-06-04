from pokemon import *
input_name1 = input("Sisestage esimese pokemoni nimi: ").lower()
input_name2 = input("Sisestage teise pokemoni nimi: ").lower()

poke1 = Pokemon(input_name1)
poke2 = Pokemon(input_name2)

print("Täna võistlevad enda vahel", input_name1, "ja", input_name2 + "!")

poke1.getMultiplier(poke2)
poke2.getMultiplier(poke1)
poke1.getStats()
poke2.getStats()

turn = 1
print(poke1.response_dict["stats"])
print(poke2.response_dict["stats"])
if poke1.speeeeeeed >= poke2.speeeeeeed:
     print("Esimesena ründab", input_name1)

     sp_atk1 = 0
     sp_atk2 = 0
     sp_def1 = 0
     sp_def2 = 0

     while poke1.hp > 0 and poke2.hp > 0 and turn <= 100:
          atk1 = poke1.getPowah(poke2,sp_atk1,sp_def2)
          if atk1 < 0:
               atk1 = 0
          poke2.hp -= atk1
          sp_atk1 += 1
          sp_def2 += 1
          print(input_name1, "ründab", input_name2, "ja teeb talle", atk1, "damage-i")
          if poke2.hp < 0:
               print(input_name2, "kaotas selle võitluse")
               break
          print(input_name2 + "l jäi ", poke2.hp, "hp")
          atk2 = poke2.getPowah(poke1, sp_atk2, sp_def1)
          if atk2 < 0:
               atk2 = 0
          poke1.hp -= atk2
          sp_atk2 += 1
          sp_def1 += 1
          turn += 1
          print(input_name2, "ründab", input_name1, "ja teeb talle", atk2, "damage-i")
          if poke1.hp < 0:
               print(input_name1, "kaotas selle võitluse")
               break
          print(input_name1 + "l jäi ", poke1.hp, "hp")
elif poke1.speeeeeeed < poke2.speeeeeeed:
     print("Esimesena ründab", input_name2)

     sp_atk1 = 0
     sp_atk2 = 0
     sp_def1 = 0
     sp_def2 = 0

     while poke1.hp > 0 and poke2.hp > 0 and turn <= 100:
          atk2 = poke2.getPowah(poke1, sp_atk2, sp_def1)
          if atk2 < 0:
               atk2 = 0
          poke1.hp -= atk2
          sp_atk2 += 1
          sp_def1 += 1
          print(input_name1, "ründab", input_name2, "ja teeb talle", atk2, "damage-i")
          if poke2.hp < 0:
               print(input_name2, "kaotas selle võitluse")
               break
          print(input_name2 + "l jäi ", poke2.hp, "hp")
          atk1 = poke1.getPowah(poke2, sp_atk1, sp_def2)
          if atk1 < 0:
               atk1 = 0
          poke2.hp -= atk1
          sp_atk1 += 1
          sp_def2 += 1
          turn += 1
          print(input_name2, "ründab", input_name1, "ja teeb talle", atk2, "damage-i")
          if poke1.hp < 0:
               print(input_name1, "kaotas selle võitluse")
               break
          print(input_name1 + "l jäi ", poke1.hp, "hp")

