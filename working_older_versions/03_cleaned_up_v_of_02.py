
from pip._vendor import requests as r
import webbrowser

class BuildTeam():
     """User creates a Pokemon team"""

     def __init__ (self):
          self.team_name_dict = {}

     def name_team(self):
          self.team_name = input("What would you like to name your team? ")
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
          print(master_poke_dict) 
          self.team_name_dict[self.team_name].append(master_poke_dict) 
     
          print(self.team_name_dict)


class Run():
     """Runs Program"""
     def __init__(self, built_team):
          self.team = built_team

     def run_program(self):
          while True:
               print("\n[1]: Name your team")
               print("[2]: Add to team")
               print("[3]: Explore Pokemon Options")
               print("[4]: Remove from team")
               print("[5]: Stop team-building")
               choice = input("Input a number to indicate what you'd like to do:  ")
               if choice == '1':
                    self.team.name_team()
               elif choice == '2':
                    self.team.add()
               elif choice == '3':
                    self.team.explore()
               elif choice == '4':
                    self.team.remove() 
               elif choice == '5':
                    self.team.quit()
               else:
                    continue

team_object = BuildTeam()
run = Run(team_object)
run.run_program()



