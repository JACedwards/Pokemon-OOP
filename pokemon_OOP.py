# Two things wanted to do but couldn't figure out:
     # avoid error when user input name that was not a Pokemon:  tried
          # things like if/else and try/except
     # sort by weight:  integer messed me up, tried using str(), but not sure 
          # was putting str() in the right place or if I needed to do something else too

from distutils.errors import DistutilsOptionError
from locale import normalize
from pip._vendor import requests as r
import webbrowser

class BuildTeam():
     """User creates a Pokemon team"""

     def __init__ (self):
          self.team_name_dict = {}
          self.types_dict = {}
          self.abilities_dict = {}
          self.weight_dict = {}
          self.name_dict = {}

     def name_team(self):
          self.team_name = input("What would you like to name your team? ")
          self.team_name = self.team_name.title()
          self.team_name_dict[self.team_name] = []

     def add(self):
          self.add1 = input("\nAre you ready to [1] input a name or [2] do you wish to explore your options ?  ")
          if self.add1 == '1':
               add_pok = input("Which Pokemon do you want to add to your team?  ")
               self.build_poke(f'https://pokeapi.co/api/v2/pokemon/{add_pok.lower()}')
          if self.add1 == '2':
               print("\nThe Pokemon official Pokedex is being opened in your browser for your exploration pleasure.")
               webbrowser.open('https://www.pokemon.com/us/pokedex/')

     def build_poke(self, url):
          
          pokemon = r.get(url)
          if pokemon.status_code == 200:
               pokemon = pokemon.json()

          name = pokemon['name']
          abilities = pokemon['abilities'][0]['ability']['name']
          types = pokemon['types'][0]['type']['name']
          weight = pokemon['weight']
          ind_poke_dict = {}
          master_poke_dict = {}

          ind_poke_dict["name"] = name 
          ind_poke_dict["abilities"] = abilities 
          ind_poke_dict["types"] = types 
          ind_poke_dict["weight"] = str(weight) 

          master_poke_dict[name] = ind_poke_dict
          self.team_name_dict[self.team_name].append(master_poke_dict) 
          print(f"\nYou have successfully added {name.title()} to your team!")

          if types not in self.types_dict:
               self.types_dict[types] = [name]
          else:
               self.types_dict[types].append(name)

          if types not in self.abilities_dict:
               self.abilities_dict[abilities] = [name]
          else:
               self.abilities_dict[abilities].append(name)  

          if types not in self.name_dict:
               self.name_dict[name] = [name]
          else:
               self.name_dict[name].append(name)                                        

     def see_team(self):
          print("Here is your team: ")
          print(*(list(self.team_name_dict.keys())), sep = ":\n")          
          pokemon_list = list(self.team_name_dict.values())[0]
          for x in pokemon_list:
               x = x
               for pok_name in x.keys():
                    print("\t"+ pok_name.title())
                    for pok_name_dict in x.values():
                         for k_v_pairs in pok_name_dict.items():
                              print(f"\t\t{k_v_pairs[0]}: {k_v_pairs[1]}")


     def sort(self):  
          print("\nHere are your sort choices:")
          print("[1] By name")
          print("[2] By type")
          print("[3] By abilities")

          sort_ask = input("How would you like to sort?  ")

          if sort_ask == '1':
               print("\nHere are the Pokemon on your team sorted by name: ")
               for key, value in self.name_dict.items():
                    print(f"{key.title()}:")
                    for x in value:
                         print(f"\t {x.title()}")

          elif sort_ask == '2':
               print("\nHere are the Pokemon on your team sorted by type: ")
               for key, value in self.types_dict.items():
                    print(f"{key.title()}:")
                    for x in value:
                         print(f"\t {x.title()}")

          elif sort_ask == '3':
               print("\nHere are the Pokemon on your team sorted by abilities: ")
               for key, value in self.abilities_dict.items():
                    print(f"{key.title()}:")
                    for x in value:
                         print(f"\t {x.title()}")



     def quit(self):
          print("\nHope you enjoyed building your team!")
          print(f"\nHere are your final team data: ")
          print(*(list(self.team_name_dict.keys())), sep = ":\n")          
          pokemon_list = list(self.team_name_dict.values())[0]
          for x in pokemon_list:
               x = x
               for pok_name in x.keys():
                    print("\t"+ pok_name.title())
                    for pok_name_dict in x.values():
                         for k_v_pairs in pok_name_dict.items():
                              print(f"\t\t{k_v_pairs[0]}: {k_v_pairs[1]}")



class Run():
     """Runs Program"""
     def __init__(self, built_team):
          self.team = built_team

     def run_program(self):
         
          self.team.name_team()
 
          while True:
               print(f"\nWhat would you like to do with your team?")
               print("[1]: Add to team")
               print("[2]: See team")
               print("[3]: Sort")
               print("[4]: Stop team-building")
               choice = input("Input a number to indicate what you'd like to do:  ")
               if choice == '1':
                    self.team.add()
               elif choice == '2':
                    self.team.see_team() 
               elif choice == '3':
                    self.team.sort()
               elif choice == '4':
                    self.team.quit()
                    break
               elif choice != '1' or choice != '2' or choice != '3' or choice != '4' or choice != '5' or choice != '6':
                    print("\nYou have not entered a valid number. \nPlease try again.")
                    continue
               else:
                    continue

team_1 = BuildTeam()
run = Run(team_1)
run.run_program()






