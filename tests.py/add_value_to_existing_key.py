p1 = {'metapod': {'name': 'metapod', 'abilities': 'shed-skin', 'types': 'bug', 'weight': 99}}
p2 = {'squirtle': {'name': 'squirtle', 'abilities': 'torrent', 'types': 'water', 'weight': 90}}
team = {'owner': {} }

team.update(p1)
print(team)
team.update(p2)
print(team)