
# from tkinter import INSIDE
from pip._vendor import requests as r
import webbrowser

class BuildTeam():
     """User creates a Pokemon team"""

     def __init__ (self):
          self.team = {}
          
     def name_team(self):
          self.team_name = input("What would you like to name your team? ")
          self.team['team name'] = self.team_name
          #developer print test
          print(self.team)

     def add(self):
          self.add1 = input("\nAre you ready to [1] input a name or [2] do you wish to explore your options ?  ")

          if self.add1 == '1':
               add_pok = input("Which Pokemon do you want to add to your team?  ")
               # self.team['Pokemon'] = add_pok
               build_poke(f'https://pokeapi.co/api/v2/pokemon/{add_pok.lower()}')

                                
          if self.add1 == '2':
               print("The Pokemon official Pokedex is being opened for your exploration pleasure.")
               webbrowser.open('https://www.pokemon.com/us/pokedex/')

def build_poke(url):
     
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
     # self.team['Pokemon'] = add_pok ???????????

# for n in range(1,21):
#      output = build_poke(f'https://pokeapi.co/api/v2/pokemon/{n}')


     



class Run():
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

test_team = BuildTeam()
run = Run(test_team)
run.run_program()


#   #<>start here:
  #       in middle of option 1 above
  #       have to figure out how to add pokemon to the TEAM dictionary I created earlier 
  #       I assume name of pokemon will become a key in the team dicitonary and the value of
          # of the key will be a dictionary with the name, abilities, type, weight, AND Habitat info INSIDE
          # Note:   Should be able to use some of the commented out code at end of this file to build dicitonary for individual pokemon.
          # Don't forget I'll have to call the api too.

          # also need to figure out how to get the WEBBROWSER code below to work



# 
# 
# def build_poke(url):
     
#      pokemon = r.get(url)
#      if pokemon.status_code == 200:
#           pokemon = pokemon.json()

#      name = pokemon['name']
#      abilities = pokemon['abilities'][0]['ability']['name']
#      types = pokemon['types'][0]['type']['name']
#      weight = pokemon['weight']
#      ind_poke_dict = {}
#      master_poke_dict = {}

#      ind_poke_dict["name"] = name 
#      ind_poke_dict["abilities"] = abilities 
#      ind_poke_dict["types"] = types 
#      ind_poke_dict["weight"] = weight 

#      master_poke_dict[name] = ind_poke_dict
#      print(master_poke_dict)

# for n in range(1,21):
#      output = build_poke(f'https://pokeapi.co/api/v2/pokemon/{n}')
