
from distutils.errors import DistutilsOptionError
from locale import normalize
from pip._vendor import requests as r
import webbrowser

class BuildTeam():
     """User creates a Pokemon team"""

     def __init__ (self):
          self.team_name_dict = {}
          self.types_dict = {}

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

          # This was my attempt to deal with user not entering a valid Pokemon name, but I got an error saying that "break" can ony be used in a while loop.
          # if name not in 'https://pokeapi.co/api/v2/pokemon/':
          #      print(f"I am sorry, but {name} is not a Pokeman. \nPlease try again.")
          #      break

          ind_poke_dict["name"] = name 
          ind_poke_dict["abilities"] = abilities 
          ind_poke_dict["types"] = types 
          ind_poke_dict["weight"] = weight 

          master_poke_dict[name] = ind_poke_dict
          self.team_name_dict[self.team_name].append(master_poke_dict) 
          print(f"\nYou have successfully added {name.title()} to your team!")

          if types not in self.types_dict:
               self.types_dict[types] = [name]
          else:
               self.types_dict[types].append(name)

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
          print(self.types_dict)
          # <> (In process of trying to do the following for a single pokemon, then will need to be able to iterate through each pokemon and sort all pokemon by type.)
          #    The above pokemon_list prints this:
               # {'ditto': {'name': 'ditto', 'abilities': 'limber', 'types': 'normal', 'weight': 40}}
               #  It looks like a dictionary, but I think error message says it is a list
               # Goals:
               #    access values of this dictionary
               #    get key  value pairs into tuple (or list) form
               #    Then, sort the entire dictionary by "types"
               #    ideally, "Type:" would print, then name of type, then new line, and entire       
               #         dictionary
               #Entire Dictionary Example:
                    # {'Craig': [
                    #    {'ditto': {'name': 'ditto', 'abilities': 'limber', 'types': 'normal', '  weight': 40}}, 
                    #    {'pikachu': {'name': 'pikachu', 'abilities': 'static', 'types': 'electric', 'weight': 60}}
                    #         ]}

                    # Type: normal
                    #      Ditto
                    #        Pikachu


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
               print("[2]: Remove from team")
               print("[3]: Search")
               print("[4]: See team")
               print("[5]: Sort")
               print("[6]: Stop team-building")
               choice = input("Input a number to indicate what you'd like to do:  ")
               if choice == '1':
                    self.team.add()
               elif choice == '2':
                    self.team.remove()
               elif choice == '3':
                    self.team.search()
               elif choice == '4':
                    self.team.see_team() 
               elif choice == '5':
                    self.team.sort()
               elif choice == '6':
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






