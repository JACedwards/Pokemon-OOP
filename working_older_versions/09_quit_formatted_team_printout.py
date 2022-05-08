
from pip._vendor import requests as r
import webbrowser

class BuildTeam():
     """User creates a Pokemon team"""

     def __init__ (self):
          self.team_name_dict = {}

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
               print("The Pokemon official Pokedex is being opened for your exploration pleasure.")
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
          ind_poke_dict["weight"] = weight 

          master_poke_dict[name] = ind_poke_dict
          self.team_name_dict[self.team_name].append(master_poke_dict) 
     
          print(self.team_name_dict)

     # Remove Notes:  Think remove will be too hard because cannot search for name of a name of pokemon when it is nested in dictionary inside a list?
     # code below at least doesn't yield error messages, but also doesn't remove a pokemon
          # I no longer think this is the way to go, but keeping here just in case.
               # This url tells how to remove one value from a key that has more than one:
               # https://stackoverflow.com/questions/39350527/python-how-to-delete-a-specific-value-from-a-dictionary-key-with-multiple-values

     def remove(self):
          remove_poke = input("Which pokemon would you like to remove?  ")
          if self.team_name_dict[self.team_name][0] == remove_poke:
               self.team_name_dict[self.team_name].pop(remove_poke)
          print(self.team_name_dict)
     # End remove

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
          pokemon_list = list(self.team_name_dict.values())[0]
          for x in pokemon_list:
               x = x
               for pok_name in x.keys():
                    print("\t"+ pok_name.title())
                    for pok_name_dict in x.values():
                         for k_v_pairs in pok_name_dict.items():
                              print(f"\t\t{k_v_pairs[0]}: {k_v_pairs[1]}")


     def quit (self):
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
               print(f"\nNow, what would you like to do with your team?")
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
               else:
                    continue

team_object = BuildTeam()
run = Run(team_object)
run.run_program()



