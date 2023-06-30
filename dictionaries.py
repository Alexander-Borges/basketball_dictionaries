class Player:
    def __init__(self,player_dictionary):
        self.name = player_dictionary["name"]
        self.age = player_dictionary["age"]
        self.position = player_dictionary["position"]
        self.team = player_dictionary["team"]
    
    def __repr__(self):
        return "Player: {}, {} years old, position: {}, team: {}".format(self.name,self.age,self.position,self.team)

kevin = {
    'name': 'Kevin Durant',
    'age':  34,
    'position': 'small forward',
    'team': 'Phoenix Suns',
}

jason = {
    'name': "Jason Tatum",
    'age': 25,
    'position': 'power forward',
    'team': 'Boston Celtics',
}

kyrie = {
    'name': "Kyrie Irving",
    'age': 31,
    'position': 'point guard',
    'team': 'Dallas Mavericks',
}

damian = {
    'name': "Damian Lillard",
    'age': 32,
    'position': 'point guard',
    'team': 'Portland Trailblazers',
}

joel = {
    'name': "Joel Embiid",
    'age': 29,
    'position': 'center',
    'team': 'Philadelphia 76ers',
}

player_kevin = Player(kevin)
print('\n')
print(player_kevin) 

player_jason = Player(jason)
#print('\n')
print(player_jason) 

player_kyrie = Player(kyrie)
#print('\n')
print(player_kyrie) 

player_damian = Player(damian)
#print('\n')
print(player_damian) 

player_joel = Player(joel)
#print('\n')
print(player_joel) 


# Given the example list of players at the top of this module (the one with many players)
# write a for loop that will populate an empty list with Player objects from the original list of dictionaries.
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":25, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":31, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":32, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":29, "position": "Center", 
    "team": "Philidelphia 76ers"
    },
    
]

# For loop over the list of dictionaries
    # each time use the dictionary info 
    # to create a new player instance


new_team = []
for player_dictionary in players:
    player = Player(player_dictionary)
    new_team.append(player)

print('\n')
print(new_team)