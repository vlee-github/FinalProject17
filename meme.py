import random
import copy
allpokemon = {'Bulbasaur' : {1 : 'Tackle', 2: 'Growl', 3: 'none', 4: 'none', 'type1':'grass', 'type2':'poison', 'level':5, 'status':'none', 'hp':21, 'attack':11, 'defense':11, 'special attack':13, 'special defense':13, 'speed':11, 'exp needed to level up':100},
'Charmander' : {1 : 'Scratch', 2:'Growl', 3:'none', 4:'none', 'type1': 'fire', 'type2':'none', 'level':5, 'status':'none', 'hp':20, 'attack':11, 'defense':10, 'special attack':12,'special defense':11, 'speed':13, 'exp needed to level up':100},
'Squirtle' : {1 : 'Tackle', 2:'Tail Whip', 3:'none', 4:'none', 'type1': 'water', 'type2':'none', 'level':5, 'status':'none', 'hp':20, 'attack':11,'defense':13, 'special attack':11,'special defense':12, 'speed':10, 'exp needed to level up':100}}
rivalpokemon = {'Bulbasaur' : {1 : 'Tackle', 2: 'Growl', 3: 'none', 4: 'none', 'type1':'grass', 'type2':'poison', 'level':5, 'status':'none', 'hp':21, 'attack':11, 'defense':11, 'special attack':13, 'special defense':13, 'speed':11, 'exp':100},
'Charmander' : {1 : 'Scratch', 2:'Growl', 3:'none', 4:'none', 'type1': 'fire', 'type2':'none', 'level':5, 'status':'none', 'hp':20, 'attack':11, 'defense':10, 'special attack':12,'special defense':11, 'speed':13, 'exp':100},
'Squirtle' : {1 : 'Tackle', 2:'Tail Whip', 3:'none', 4:'none', 'type1': 'water', 'type2':'none', 'level':5, 'status':'none', 'hp':20, 'attack':11,'defense':13, 'special attack':11,'special defense':12, 'speed':10, 'exp':100}}
allmoves = {'Ember' : {'type':'fire', 'category':'special', 'bp':40, 'effect':'10%burn'},
'Vine Whip' : {'type':'grass', 'category':'physical', 'bp':45, 'effect':'none'},
'Water Gun' : {'type':'water', 'category':'special', 'bp':40, 'effect':'none'},
'Tackle' : {'type':'normal', 'category':'physical', 'bp':40, 'effect':'none'},
'Scratch' : {'type':'normal', 'category':'physical', 'bp':40, 'effect':'none'},
'Tail Whip' : {'type':'normal', 'category':'status', 'effect':'lowerdefenseby1'},
'Growl' : {'type':'normal', 'category':'status', 'effect':'lowerattackby1'}}
party = {}
team = {}
money = 3000
name = input("What is your name?\n")
rivalname = input("What is your rival's name?\n")
rival = {}
pokemonstatchanges = []
opponentstatchanges = []
bag = ['Potion']
starter = input("Which starter do you want? Bulbasaur, Charmander, or Squirtle?\n")
starter = starter.title()
t = 5
while t == 5:
    if starter == 'Bulbasaur':
        team['Bulbasaur']='none'
        party['Bulbasaur']=allpokemon['Bulbasaur']
        rival['Charmander']=rivalpokemon['Charmander']
        rivalstarter = 'Charmander'
        break
    elif starter == 'Charmander':
        team['Charmander']='none'
        party['Charmander']=allpokemon['Charmander']
        rival['Squirtle']=rivalpokemon['Squirtle']
        rivalstarter = 'Squirtle'
        break
    elif starter == 'Squirtle':
        team['Squirtle']='none'
        party['Squirtle']=allpokemon['Squirtle']
        rival['Bulbasaur']=rivalpokemon['Bulbasaur']
        rivalstarter = 'Bulbasaur'
        break
    else:
        print("That is not a valid starter")
        starter = input("Choose a starter.\n")
        starter = starter.title()
party2 = copy.deepcopy(party)
opponents = {rivalname:rival}
opponents2 = copy.deepcopy(opponents)
def firemove():
    global type
    if party[next(iter(team))]['type1'] == 'grass':
        type = 2
    elif party[next(iter(team))]['type2'] == 'grass':
        type = 4
    elif party[next(iter(team))]['type1'] == 'bug':
        type = 2
    elif party[next(iter(team))]['type1'] == 'ice':
        type = 2
    elif party[next(iter(team))]['type2'] == 'ice':
        type = 1
    elif party[next(iter(team))]['type1'] == 'dragon':
        type = .5
    elif party[next(iter(team))]['type1'] == 'rock':
        if party[next(iter(team))]['type2'] == 'water':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(team))]['type1'] == 'water':
        if opponents[opponent][next(iter(team))]['type2'] == 'ice':
            type = 1
        else:
            type = .5
    elif party[next(iter(team))]['type2'] == 'rock':
        type = .5
    else:
        type = 1
def grassmove():
    global type
    if party[next(iter(team))]['type1'] == 'water':
        if party[next(iter(team))]['type2'] == 'poison':
            type = 1
        elif party[next(iter(team))]['type2'] == 'flying':
            type = 1
        elif party[next(iter(team))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif party[next(iter(team))]['type1'] == 'ground':
        if party[next(iter(team))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif party[next(iter(team))]['type2'] == 'ground':
        if party[next(iter(team))]['type2'] == 'poison':
            type = 1
        elif party[next(iter(team))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif party[next(iter(team))]['type1'] == 'rock':
        type = 1
    elif party[next(iter(team))]['type1'] == 'bug':
        if party[next(iter(team))]['type2'] == 'poison':
            type = .25
        elif party[next(iter(team))]['type'] == 'flying':
            type = .25
        elif party[next(iter(team))]['type2'] == 'grass':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type1'] == 'dragon':
        if party[next(iter(team))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type1'] == 'fire':
        if party[next(iter(team))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type2'] == 'flying':
        if party[next(iter(team))]['type1'] == 'poison':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type1'] == 'grass':
        if party[next(iter(team))]['type2'] == 'poison':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type1'] == 'poison':
        type = .5
    else:
        type = 1
def watermove():
    global type
    if party[next(iter(team))]['type1'] == 'fire':
        type = 2
    elif party[next(iter(team))]['type1'] == 'ground':
        if party[next(iter(team))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif party[next(iter(team))]['type2'] == 'ground':
        if party[next(iter(team))]['type1'] == 'rock':
            type = 4
        else:
            type = 2
    elif party[next(iter(team))]['type1'] == 'rock':
        if party[next(iter(team))]['type2'] == 'water':
            type = 1
        else:
            type = 2
    elif party[next(iter(team))]['type1'] == 'dragon':
        type = .5
    elif party[next(iter(team))]['type1'] == 'grass':
        type = .5
    elif party[next(iter(team))]['type2'] == 'grass':
        type = .5
    elif party[next(iter(team))]['type1'] == 'water':
        type = .5
    else:
        type = 1
def icemove():
    global type
    if party[next(iter(team))]['type1'] == 'dragon':
        if party[next(iter(team))]['type2'] == 'flying':
            type = 4
        else:
            type = 2
    elif party[next(iter(team))]['type2'] == 'flying':
        if party[next(iter(team))]['type1'] == 'fire':
            type = 1
        elif party[next(iter(team))]['type1'] == 'water':
            type = 1
        elif party[next(iter(team))]['type1'] == 'ice':
            type = 1
    elif party[next(iter(team))]['type1'] == 'grass':
        type = 2
    elif party[next(iter(team))]['type2'] == 'grass':
        type = 2
    elif party[next(iter(team))]['type1'] == 'ground':
        type = 2
    elif party[next(iter(team))]['type2'] == 'ground':
        type = 2
    else:
        type = 1
def groundmove():
    global type
    if party[next(iter(team))]['type2'] == 'flying':
        type = 0
    elif party[next(iter(team))]['type1'] == 'electric':
        type = 2
    elif party[next(iter(team))]['type1'] == 'fire':
        type = 2
    elif party[next(iter(team))]['type1'] == 'poison':
        type = 2
    elif party[next(iter(team))]['type2'] == 'poison':
        if party[next(iter(team))]['type1'] == 'bug':
            type = 1
        elif party[next(iter(team))]['type1'] == 'grass':
            type = 1
    elif party[next(iter(team))]['type1'] == 'rock':
        type = 2
    elif party[next(iter(team))]['type2'] == 'rock':
        type = 2
    elif party[next(iter(team))]['type1'] == 'bug':
        if party[next(iter(team))]['type2'] == 'grass':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type1'] == 'grass':
        type = .5
    else:
        type = 1
def electricmove():
    global type
    if party[next(iter(team))]['type1'] == 'ground':
        type = 0
    elif party[next(iter(team))]['type1'] == 'water':
        if party[next(iter(team))]['type2'] == 'flying':
            type = 4
        else:
            type = 2
    elif party[next(iter(team))]['type2'] == 'water':
        type = 2
    elif party[next(iter(team))]['type2'] == 'flying':
        if party[next(iter(team))]['type1'] == 'electric':
            type = 1
        elif party[next(iter(team))]['type1'] == 'dragon':
            type = 1
        else:
            type = 2
    elif party[next(iter(team))]['type1'] == 'dragon':
        type = .5
    elif party[next(iter(team))]['type1'] == 'electric':
        type = .5
    elif party[next(iter(team))]['type1'] == 'grass':
        type = .5
    elif party[next(iter(team))]['type2'] == 'grass':
        type = .5
    else:
        type = 1
def flyingmove():
    global type
    if party[next(iter(team))]['type1'] == 'bug':
        if party[next(iter(team))]['type2'] == 'grass':
            type = 4
        else:
            type = 2
    elif party[next(iter(team))]['type2'] == 'grass':
        type = 4
    elif party[next(iter(team))]['type1'] == 'fighting':
        type = 2
    elif party[next(iter(team))]['type2'] == 'fighting':
        type = 2
    elif party[next(iter(team))]['type1'] == 'electric':
        type = .5
    elif party[next(iter(team))]['type1'] == 'rock':
        type = .5
    elif party[next(iter(team))]['type2'] == 'rock':
        type = .5
    else:
        type = 1
def ghostmove():
    global type
    if party[next(iter(team))]['type1'] == 'normal':
        type = 0
    elif party[next(iter(team))]['type1'] == 'ghost':
        type = 2
    elif party[next(iter(team))]['type1'] == 'psychic':
        type = 2
    elif party[next(iter(team))]['type2'] == 'psychic':
        type = 2
    else:
        type = 1
def rockmove():
    global type
    if party[next(iter(team))]['type1'] == 'fire':
        if party[next(iter(team))]['type2'] == 'flying':
            type = 4
        else:
            type = 2
    elif party[next(iter(team))]['type2'] == 'flying':
        if party[next(iter(team))]['type1'] == 'bug':
            type = 4
        elif party[next(iter(team))]['type1'] == 'ice':
            type = 4
        else:
            type = 2
    elif party[next(iter(team))]['type1'] == 'bug':
        type  = 2
    elif party[next(iter(team))]['type1'] == 'ice':
        type = 2
    elif party[next(iter(team))]['type2'] == 'ice':
        type = 2
    elif party[next(iter(team))]['type1'] == 'ground':
        type = .5
    elif party[next(iter(team))]['type2'] == 'ground':
        type = .5
    elif party[next(iter(team))]['type1'] == 'fighting':
        type = .5
    elif party[next(iter(team))]['type2'] == 'fighting':
        type = .5
    else:
        type = 1
def poisonmove():
    global type
    if party[next(iter(team))]['type1'] == 'grass':
        if party[next(iter(team))]['type1'] == 'poison':
            type = 1
        else:
            type = 2
    elif party[next(iter(team))]['type2'] == 'grass':
        type = 2
    elif party[next(iter(team))]['type1'] == 'ghost':
        type = .25
    elif party[next(iter(team))]['type1'] == 'ground':
        if party[next(iter(team))]['type2'] == 'rock':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type2'] == 'ground':
        if party[next(iter(team))]['type1'] == 'rock':
            type = .25
        elif party[next(iter(team))]['type1'] == 'poison':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type1'] == 'rock':
        type = .5
    elif party[next(iter(team))]['type1'] == 'poison':
        type = .5
    elif party[next(iter(team))]['type2'] == 'poison':
        type = .5
    else:
        type = 1
def psychicmove():
    global type
    if party[next(iter(team))]['type1'] == 'fighting':
        type = 2
    elif party[next(iter(team))]['type2'] == 'fighting':
        type = 2
    elif party[next(iter(team))]['type1'] == 'poison':
        type = 2
    elif party[next(iter(team))]['type2'] == 'poison':
        type = 2
    elif party[next(iter(team))]['type1'] == 'psychic':
        type =.5
    elif party[next(iter(team))]['type2'] == 'psychic':
        type = .5
    else:
        type = 1
def bugmove():
    global type
    if party[next(iter(team))]['type1'] == 'grass':
        if party[next(iter(team))]['type1'] == 'poison':
            type = 1
        else:
            type = 2
    elif party[next(iter(team))]['type2'] == 'grass':
        type = 2
    elif party[next(iter(team))]['type1'] == 'psychic':
        type = 2
    elif party[next(iter(team))]['type2'] == 'psychic':
        type = 2
    elif party[next(iter(team))]['type1'] == 'fighting':
        type = .5
    elif party[next(iter(team))]['type2'] == 'fighting':
        type = .5
    elif party[next(iter(team))]['type1'] == 'fire':
        if party[next(iter(team))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type1'] == 'ghost':
        type = .25
    elif party[next(iter(team))]['type1'] == 'poison':
        if party[next(iter(team))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type2'] == 'poison':
        type = .5
    elif party[next(iter(team))]['type2'] == 'flying':
        type = .5
    else:
        type = 1
def fightingmove():
    global type
    if party[next(iter(team))]['type1'] == 'ghost':
        type = 0
    elif party[next(iter(team))]['type1'] == 'rock':
        if party[next(iter(team))]['type2'] == 'flying':
            type = 1
        else:
            type = 2
    elif party[next(iter(team))]['type2'] == 'rock':
        type = 2
    elif party[next(iter(team))]['type1'] == 'ice':
        if party[next(iter(team))]['type2'] == 'flying':
            type = 1
        elif party[next(iter(team))]['type2'] == 'psychic':
            type = 1
        else:
            type = 2
    elif party[next(iter(team))]['type2'] == 'ice':
        type = 2
    elif party[next(iter(team))]['type1'] == 'normal':
        if party[next(iter(team))]['type2'] == 'flying':
            type = 1
        else:
            type = 2
    elif party[next(iter(team))]['type1'] == 'bug':
        if party[next(iter(team))]['type2'] == 'flying':
            type = .25
        elif party[next(iter(team))]['type2'] == 'poison':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type2'] == 'flying':
        if party[next(iter(team))]['type1'] == 'poison':
            type = .25
        else:
            type = .5
    elif party[next(iter(team))]['type1'] == 'poison':
        type = .25
    elif party[next(iter(team))]['type2'] == 'poison':
        type = .5
    else:
        type = 1
def normalmove():
    global type
    if party[next(iter(team))]['type1'] == 'ghost':
        type = 0
    elif party[next(iter(team))]['type1'] == 'rock':
        type = .5
    elif party[next(iter(team))]['type2'] == 'rock':
        type = .5
    else:
        type = 1

def firemoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'grass':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'grass':
        type = 4
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'bug':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ice':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'ice':
        type = 1
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'dragon':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'water':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'ice':
            type = 1
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'rock':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'water':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'rock':
        type = .5
    else:
        type = 1
def grassmoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'water':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'poison':
            type = 1
        elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = 1
        elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ground':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'ground':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'poison':
            type = 1
        elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'rock':
        type = 1
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'bug':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'poison':
            type = .25
        elif opponents[opponent][next(iter(opponents[opponent]))]['type'] == 'flying':
            type = .25
        elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'grass':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'dragon':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fire':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'grass':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'poison':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
        type = .5
    else:
        type = 1
def watermoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fire':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ground':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'ground':
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'rock':
            type = 4
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'rock':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'water':
            type = 1
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'dragon':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'grass':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'grass':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'water':
        type = .5
    else:
        type = 1
def icemoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'dragon':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = 4
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fire':
            type = 1
        elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'water':
            type = 1
        elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ice':
            type = 1
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'grass':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'grass':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ground':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'ground':
        type = 2
    else:
        type = 1
def groundmoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
        type = 0
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'electric':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fire':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'poison':
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'bug':
            type = 1
        elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'grass':
            type = 1
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'rock':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'rock':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'bug':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'grass':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'grass':
        type = .5
    else:
        type = 1
def electricmoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ground':
        type = 0
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'water':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = 4
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'water':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'electric':
            type = 1
        elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'dragon':
            type = 1
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'dragon':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'electric':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'grass':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'grass':
        type = .5
    else:
        type = 1
def flyingmoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'bug':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'grass':
            type = 4
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'grass':
        type = 4
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fighting':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'fighting':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'electric':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'rock':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'rock':
        type = .5
    else:
        type = 1
def ghostmoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'normal':
        type = 0
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ghost':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'psychic':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'psychic':
        type = 2
    else:
        type = 1
def rockmoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fire':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = 4
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'bug':
            type = 4
        elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ice':
            type = 4
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'bug':
        type  = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ice':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'ice':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ground':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'ground':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fighting':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'fighting':
        type = .5
    else:
        type = 1
def poisonmoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'grass':
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
            type = 1
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'grass':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ghost':
        type = .25
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ground':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'rock':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'ground':
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'rock':
            type = .25
        elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'rock':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'poison':
        type = .5
    else:
        type = 1
def psychicmoveopponent(opponent,r):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fighting':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'fighting':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'poison':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'psychic':
        type =.5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'psychic':
        type = .5
    else:
        type = 1
def bugmoveopponent(opponent,r):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'grass':
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
            type = 1
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'grass':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'psychic':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'psychic':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fighting':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'fighting':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fire':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ghost':
        type = .25
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'poison':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
        type = .5
    else:
        type = 1
def fightingmoveopponent(opponent,r):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ghost':
        type = 0
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'rock':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = 1
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'rock':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ice':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = 1
        elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'psychic':
            type = 1
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'ice':
        type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'normal':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = 1
        else:
            type = 2
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'bug':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = .25
        elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'poison':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
            type = .25
        else:
            type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'poison':
        type = .25
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'poison':
        type = .5
    else:
        type = 1
def normalmoveopponent(opponent):
    global type
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ghost':
        type = 0
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'rock':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'rock':
        type = .5
    else:
        type = 1

def userstatusmove(move,opponent):
    print(next(iter(team)), "used", move)
    if allmoves[move]['effect']=='lowerdefenseby1':
        if opponentstatchanges.count('raisedefenseby1')==1:
            opponentstatchanges.remove('raisedefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was lowered.')
        elif opponentstatchanges.count('raisedefenseby1')>1:
            opponentstatchanges.remove('lowerdefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was lowered.')
        elif opponentstatchanges.count('lowerdefenseby1')==6:
            print('The defense of', next(iter(opponents[opponent])), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerdefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was lowered.')
    elif allmoves[move]['effect']=='lowerdefenseby2':
        if opponentstatchanges.count('raisedefenseby1')==1:
            opponentstatchanges.remove('raisedefenseby1')
            opponentstatchanges.append('lowerdefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was sharply lowered.')
        elif opponentstatchanges.count('raisedefenseby1')>1:
            opponentstatchanges.remove('raisedefenseby1')
            opponentstatchanges.remove('raisedefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was sharply lowered.')
        elif opponentstatchanges.count('lowerdefenseby1')==6:
            print('The defense of', next(iter(opponents[opponent])), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerdefenseby1')
            opponentstatchanges.append('lowerdefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was sharply lowered.')
    elif allmoves[move]['effect']=='raisedefenseby1':
        if pokemonstatchanges.count('lowerdefenseby1')==1:
            pokemonstatchanges.remove('lowerdefenseby1')
            print('The defense of', next(iter(tean)), 'was raised.')
        elif pokemonstatchanges.count('lowerdefenseby1')>1:
            pokemonstatchanges.remove('lowerdefenseby1')
            print('The defense of', next(iter(tean)), 'was raised.')
        elif pokemonstatchanges.count('raisedefenseby1')==6:
            print('The defense of', next(iter(team)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisedefenseby1')
            print('The defense of', next(iter(tean)), 'was raised.')
    elif allmoves[move]['effect']=='raisedefenseby2':
        if pokemonstatchanges.count('lowerdefenseby1')==1:
            pokemonstatchanges.remove('lowerdefenseby1')
            pokemonstatchanges.append('raisedefenseby1')
            print('The defense of', next(iter(tean)), 'was sharply raised.')
        elif pokemonstatchanges.count('lowerdefenseby1')>1:
            pokemonstatchanges.remove('lowerdefenseby1')
            pokemonstatchanges.remove('lowerdefenseby1')
            print('The defense of', next(iter(tean)), 'was sharply raised.')
        elif pokemonstatchanges.count('raisedefenseby1')==6:
            print('The defense of', next(iter(team)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisedefenseby1')
            pokemonstatchanges.append('raisedefenseby1')
            print('The defense of', next(iter(tean)), 'was sharply raised.')
    elif allmoves[move]['effect']=='lowerattackby1':
        if opponentstatchanges.count('raiseattackby1')==1:
            opponentstatchanges.remove('raiseattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was lowered.')
        elif opponentstatchanges.count('raiseattackby1')>1:
            opponentstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was lowered.')
        elif opponentstatchanges.count('lowerattackby1')==6:
            print('The attack of', next(iter(opponents[opponent])), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was lowered.')
    elif allmoves[move]['effect']=='lowerattackby2':
        if opponentstatchanges.count('raiseattackby1')==1:
            opponentstatchanges.remove('raiseattackby1')
            opponentstatchanges.append('lowerattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was sharply lowered.')
        elif opponentstatchanges.count('raiseattackby1')>1:
            opponentstatchanges.remove('raiseattackby1')
            opponentstatchanges.remove('raiseattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was sharply lowered.')
        elif opponentstatchanges.count('lowerattackby1')==6:
            print('The attack of', next(iter(opponents[opponent])), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerattackby1')
            opponentstatchanges.append('lowerattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was sharply lowered.')
    elif allmoves[move]['effect']=='raiseattackby1':
        if pokemonstatchanges.count('lowerattackby1')==1:
            pokemonstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(team)), 'was raised.')
        elif pokemonstatchanges.count('lowerattackby1')>1:
            pokemonstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(team)), 'was raised.')
        elif pokemonstatchanges.count('raiseattackby1')==6:
            print('The attack of', next(iter(team)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raiseattackby1')
            print('The attack of', next(iter(team)), 'was raised.')
    elif allmoves[move]['effect']=='raiseattackby2':
        if pokemonstatchanges.count('lowerattackby1')==1:
            pokemonstatchanges.remove('lowerattackby1')
            pokemonstatchanges.append('raiseattackby1')
            print('The attack of', next(iter(team)), 'was sharply raised.')
        elif pokemonstatchanges.count('lowerattackby1')>1:
            pokemonstatchanges.remove('lowerattackby1')
            pokemonstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(team)), 'was sharply raised.')
        elif pokemonstatchanges.count('raiseattackby1')==6:
            print('The attack of', next(iter(team)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raiseattackby1')
            pokemonstatchanges.append('raiseattackby1')
            print('The attack of', next(iter(team)), 'was sharply raised.')
    elif allmoves[move]['effect']=='lowerspeedby1':
        if opponentstatchanges.count('raisespeedby1')==1:
            opponentstatchanges.remove('raisespeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was lowered.')
        elif opponentstatchanges.count('raisespeedby1')>1:
            opponentstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was lowered.')
        elif opponentstatchanges.count('lowerspeedby1')==6:
            print('The speed of', next(iter(opponents[opponent])), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerspeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was lowered.')
    elif allmoves[move]['effect']=='lowerspeedby2':
        if opponentstatchanges.count('raisespeedby1')==1:
            opponentstatchanges.remove('raisespeedby1')
            opponentstatchanges.append('lowerspeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was sharply lowered.')
        elif opponentstatchanges.count('raisespeedby1')>1:
            opponentstatchanges.remove('raisespeedby1')
            opponentstatchanges.remove('raisespeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was sharply lowered.')
        elif opponentstatchanges.count('lowerspeedby1')==6:
            print('The speed of', next(iter(opponents[opponent])), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerspeedby1')
            opponentstatchanges.append('lowerspeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was sharply lowered.')
    elif allmoves[move]['effect']=='raisespeedby1':
        if pokemonstatchanges.count('lowerspeedby1')==1:
            pokemonstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(team)), 'was raised.')
        elif pokemonstatchanges.count('lowerspeedby1')>1:
            pokemonstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(team)), 'was raised.')
        elif pokemonstatchanges.count('raisespeedby1')==6:
            print('The speed of', next(iter(team)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespeedby1')
            print('The speed of', next(iter(team)), 'was raised.')
    elif allmoves[move]['effect']=='raisespeedby2':
        if pokemonstatchanges.count('lowerspeedby1')==1:
            pokemonstatchanges.remove('lowerspeedby1')
            pokemonstatchanges.append('raisespeedby1')
            print('The speed of', next(iter(team)), 'was sharply raised.')
        elif pokemonstatchanges.count('lowerspeedby1')>1:
            pokemonstatchanges.remove('lowerspeedby1')
            pokemonstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(team)), 'was sharply raised.')
        elif pokemonstatchanges.count('raisespeedby1')==6:
            print('The speed of', next(iter(team)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespeedby1')
            pokemonstatchanges.append('raisespeedby1')
            print('The speed of', next(iter(team)), 'was sharply raised.')
    elif allmoves[move]['effect']=='lowerspecialattackby1':
        if opponentstatchanges.count('raisespecialattackby1')==1:
            opponentstatchanges.remove('raisespecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was lowered.')
        elif opponentstatchanges.count('raisespecialattackby1')>1:
            opponentstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was lowered.')
        elif opponentstatchanges.count('lowerspecialattackby1')==6:
            print('The special attack of', next(iter(opponents[opponent])), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerspecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was lowered.')
    elif allmoves[move]['effect']=='lowerspecialattackby2':
        if opponentstatchanges.count('raisespecialattackby1')==1:
            opponentstatchanges.remove('raisespecialattackby1')
            opponentstatchanges.append('lowerspecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was sharply lowered.')
        elif opponentstatchanges.count('raisespecialattackby1')>1:
            opponentstatchanges.remove('raisespecialattackby1')
            opponentstatchanges.remove('raisespecialattackby1')
        elif opponentstatchanges.count('lowerspecialattackby1')==6:
            print('The special attack of', next(iter(opponents[opponent])), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerspecialattackby1')
            opponentstatchanges.append('lowerspecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was sharply lowered.')
    elif allmoves[move]['effect']=='raisespecialattackby1':
        if pokemonstatchanges.count('lowerspecialattackby1')==1:
            pokemonstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(team)), 'was raised.')
        elif pokemonstatchanges.count('lowerspecialattackby1')>1:
            pokemonstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(team)), 'was raised.')
        elif pokemonstatchanges.count('raisespecialattackby1')==6:
            print('The special attack of', next(iter(team)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespecialattackby1')
            print('The special attack of', next(iter(team)), 'was raised.')
    elif allmoves[move]['effect']=='raisespecialattackby2':
        if pokemonstatchanges.count('lowerspecialattackby1')==1:
            pokemonstatchanges.remove('lowerspecialattackby1')
            pokemonstatchanges.append('raisespecialattackby1')
            print('The special attack of', next(iter(team)), 'was sharply raised.')
        elif pokemonstatchanges.count('lowerspecialattackby1')>1:
            pokemonstatchanges.remove('lowerspecialattackby1')
            pokemonstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(team)), 'was sharply raised.')
        elif pokemonstatchanges.count('raisespecialattackby1')==6:
            print('The special attack of', next(iter(team)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespecialattackby1')
            pokemonstatchanges.append('raisespecialattackby1')
            print('The special attack of', next(iter(team)), 'was sharply raised.')
    elif allmoves[move]['effect']=='lowerspecialdefenseby1':
        if opponentstatchanges.count('raisespecialdefenseby1')==1:
            opponentstatchanges.remove('raisespecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was lowered.')
        elif opponentstatchanges.count('raisespecialdefenseby1')>1:
            opponentstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was lowered.')
        elif opponentstatchanges.count('lowerspecialdefenseby1')==6:
            print('The special defense of', next(iter(opponents[opponent])), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerspecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was lowered.')
    elif allmoves[move]['effect']=='lowerspecialdefenseby2':
        if opponentstatchanges.count('raisespecialdefenseby1')==1:
            opponentstatchanges.remove('raisespecialdefenseby1')
            opponentstatchanges.append('lowerspecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was sharply lowered.')
        elif opponentstatchanges.count('raisespecialdefenseby1')>1:
            opponentstatchanges.remove('raisespecialdefenseby1')
            opponentstatchanges.remove('raisespecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was sharply lowered.')
        elif opponentstatchanges.count('lowerspecialdefenseby1')==6:
            print('The special defense of', next(iter(opponents[opponent])), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerspecialdefenseby1')
            opponentstatchanges.append('lowerspecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was sharply lowered.')
    elif allmoves[move]['effect']=='raisespecialdefenseby1':
        if pokemonstatchanges.count('lowerspecialdefenseby1')==1:
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was raised.')
        elif pokemonstatchanges.count('lowerspecialdefenseby1')>1:
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was raised.')
        elif pokemonstatchanges.count('raisespecialdefenseby1')==6:
            print('The special defense of', next(iter(team)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was raised.')
    elif allmoves[move]['effect']=='raisespecialdefenseby2':
        if pokemonstatchanges.count('lowerspecialdefenseby1')==1:
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            pokemonstatchanges.append('raisespecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was sharply raised.')
        elif pokemonstatchanges.count('lowerspecialdefenseby1')>1:
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was sharply raised.')
        elif pokemonstatchanges.count('raisespecialdefenseby1')==6:
            print('The special defense of', next(iter(team)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespecialdefenseby1')
            pokemonstatchanges.append('raisespecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was sharply raised.')

def opponentstatusmove(opponent, opponentmove):
    print(next(iter(opponents[opponent])), 'used', opponentmove)
    if allmoves[opponentmove]['effect']=='lowerdefenseby1':
        if pokemonstatchanges.count('raisedefenseby1')==1:
            pokemonstatchanges.remove('raisedefenseby1')
            print('The defense of', next(iter(team)), 'was lowered.')
        elif pokemonstatchanges.count('raisedefenseby1')>1:
            pokemonstatchanges.remove('lowerdefenseby1')
            print('The defense of', next(iter(team)), 'was lowered.')
        elif pokemonstatchanges.count('lowerdefenseby1')==6:
            print('The defense of', next(iter(team)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerdefenseby1')
            print('The defense of', next(iter(team)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerdefenseby2':
        if pokemonstatchanges.count('raisedefenseby1')==1:
            pokemonstatchanges.remove('raisedefenseby1')
            pokemonstatchanges.append('lowerdefenseby1')
            print('The defense of', next(iter(team)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raisedefenseby1')>1:
            pokemonstatchanges.remove('raisedefenseby1')
            pokemonstatchanges.remove('raisedefenseby1')
            print('The defense of', next(iter(team)), 'was sharply lowered.')
        elif pokemonstatchanges.count('lowerdefenseby1')==6:
            print('The defense of', next(iter(team)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerdefenseby1')
            pokemonstatchanges.append('lowerdefenseby1')
            print('The defense of', next(iter(team)), 'was sharply lowered.')
    elif allmoves[opponentmove]['effect']=='raisedefenseby1':
        if opponentstatchanges.count('lowerdefenseby1')==1:
            opponentstatchanges.remove('lowerdefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('lowerdefenseby1')>1:
            opponentstatchanges.remove('lowerdefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('raisedefenseby1')==6:
            print('The defense of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raisedefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was raised.')
    elif allmoves[opponentmove]['effect']=='raisedefenseby2':
        if opponentstatchanges.count('lowerdefenseby1')==1:
            opponentstatchanges.remove('lowerdefenseby1')
            opponentstatchanges.append('raisedefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('lowerdefenseby1')>1:
            opponentstatchanges.remove('lowerdefenseby1')
            opponentstatchanges.remove('lowerdefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif pokemonstatchanges.count('raisedefenseby1')==6:
            print('The defense of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raisedefenseby1')
            opponentstatchanges.append('raisedefenseby1')
            print('The defense of', next(iter(opponents[opponent])), 'was sharply raised.')
    elif allmoves[opponentmove]['effect']=='lowerattackby1':
        if pokemonstatchanges.count('raiseattackby1')==1:
            pokemonstatchanges.remove('raiseattackby1')
            print('The attack of', next(iter(team)), 'was lowered.')
        elif pokemonstatchanges.count('raiseattackby1')>1:
            pokemonstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(team)), 'was lowered.')
        elif pokemonstatchanges.count('lowerattackby1')==6:
            print('The attack of', next(iter(team)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerattackby1')
            print('The attack of', next(iter(team)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerattackby2':
        if pokemonstatchanges.count('raiseattackby1')==1:
            pokemonstatchanges.remove('raiseattackby1')
            pokemonstatchanges.append('lowerattackby1')
            print('The attack of', next(iter(team)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raiseattackby1')>1:
            pokemonstatchanges.remove('raiseattackby1')
            pokemonstatchanges.remove('raiseattackby1')
            print('The attack of', next(iter(team)), 'was sharply lowered.')
        elif pokemonstatchanges.count('lowerattackby1')==6:
            print('The attack of', next(iter(team)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerattackby1')
            pokemonstatchanges.append('lowerattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was sharply lowered.')
    elif allmoves[opponentmove]['effect']=='raiseattackby1':
        if opponentstatchanges.count('lowerattackby1')==1:
            opponentstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('lowerattackby1')>1:
            opponentstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was raised.')
        elif pokemonstatchanges.count('raiseattackby1')==6:
            print('The attack of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raiseattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was raised.')
    elif allmoves[opponentmove]['effect']=='raiseattackby2':
        if opponentstatchanges.count('lowerattackby1')==1:
            pokemonstatchanges.remove('lowerattackby1')
            opponentstatchanges.append('raiseattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('lowerattackby1')>1:
            pokemonstatchanges.remove('lowerattackby1')
            pokemonstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif pokemonstatchanges.count('raiseattackby1')==6:
            print('The attack of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raiseattackby1')
            opponentstatchanges.append('raiseattackby1')
            print('The attack of', next(iter(team)), 'was sharply raised.')
    elif allmoves[opponentmove]['effect']=='lowerspeedby1':
        if pokemonstatchanges.count('raisespeedby1')==1:
            pokemonstatchanges.remove('raisespeedby1')
            print('The speed of', next(iter(team)), 'was lowered.')
        elif pokemonstatchanges.count('raisespeedby1')>1:
            opponentstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(team)), 'was lowered.')
        elif opponentstatchanges.count('lowerspeedby1')==6:
            print('The speed of', next(iter(team)), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerspeedby1')
            print('The speed of', next(iter(team)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerspeedby2':
        if pokemonstatchanges.count('raisespeedby1')==1:
            pokemonstatchanges.remove('raisespeedby1')
            opponentstatchanges.append('lowerspeedby1')
            print('The speed of', next(iter(team)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raisespeedby1')>1:
            pokemonstatchanges.remove('raisespeedby1')
            pokemonstatchanges.remove('raisespeedby1')
            print('The speed of', next(iter(team)), 'was sharply lowered.')
        elif opponentstatchanges.count('lowerspeedby1')==6:
            print('The speed of', next(iter(team)), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerspeedby1')
            opponentstatchanges.append('lowerspeedby1')
            print('The speed of', next(iter(team)), 'was sharply lowered.')
    elif allmoves[opponentmove]['effect']=='raisespeedby1':
        if opponentstatchanges.count('lowerspeedby1')==1:
            pokemonstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('lowerspeedby1')>1:
            opponentstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('raisespeedby1')==6:
            print('The speed of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raisespeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was raised.')
    elif allmoves[opponentmove]['effect']=='raisespeedby2':
        if opponentstatchanges.count('lowerspeedby1')==1:
            opponentstatchanges.remove('lowerspeedby1')
            opponentstatchanges.append('raisespeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('lowerspeedby1')>1:
            opponentstatchanges.remove('lowerspeedby1')
            opponentstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('raisespeedby1')==6:
            print('The speed of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raisespeedby1')
            opponentstatchanges.append('raisespeedby1')
            print('The speed of', next(iter(opponents[opponent])), 'was sharply raised.')
    elif allmoves[opponentmove]['effect']=='lowerspecialattackby1':
        if pokemonstatchanges.count('raisespecialattackby1')==1:
            pokemonstatchanges.remove('raisespecialattackby1')
            print('The special attack of', next(iter(team)), 'was lowered.')
        elif pokemonstatchanges.count('raisespecialattackby1')>1:
            pokemonstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(team)), 'was lowered.')
        elif pokemonstatchanges.count('lowerspecialattackby1')==6:
            print('The special attack of', next(iter(team)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerspecialattackby1')
            print('The special attack of', next(iter(team)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerspecialattackby2':
        if pokemonstatchanges.count('raisespecialattackby1')==1:
            pokemonstatchanges.remove('raisespecialattackby1')
            opponentstatchanges.append('lowerspecialattackby1')
            print('The special attack of', next(iter(team)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raisespecialattackby1')>1:
            pokemonstatchanges.remove('raisespecialattackby1')
            pokemonstatchanges.remove('raisespecialattackby1')
            print('The special attack of', next(iter(team)), 'was sharply lowered.')
        elif pokemonstatchanges.count('lowerspecialattackby1')==6:
            print('The special attack of', next(iter(team)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerspecialattackby1')
            pokemonstatchanges.append('lowerspecialattackby1')
            print('The special attack of', next(iter(team)), 'was sharply lowered.')
    elif allmoves[opponentmove]['effect']=='raisespecialattackby1':
        if opponentstatchanges.count('lowerspecialattackby1')==1:
            opponentstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('lowerspecialattackby1')>1:
            opponentstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('raisespecialattackby1')==6:
            print('The special attack of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raisespecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was raised.')
    elif allmoves[opponentmove]['effect']=='raisespecialattackby2':
        if opponentstatchanges.count('lowerspecialattackby1')==1:
            opponentstatchanges.remove('lowerspecialattackby1')
            opponentstatchanges.append('raisespecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('lowerspecialattackby1')>1:
            opponentstatchanges.remove('lowerspecialattackby1')
            opponentstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('raisespecialattackby1')==6:
            print('The special attack of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raisespecialattackby1')
            opponentstatchanges.append('raisespecialattackby1')
            print('The special attack of', next(iter(opponents[opponent])), 'was sharply raised.')
    elif allmoves[opponentmove]['effect']=='lowerspecialdefenseby1':
        if pokemonstatchanges.count('raisespecialdefenseby1')==1:
            pokemonstatchanges.remove('raisespecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was lowered.')
        elif pokemonstatchanges.count('raisespecialdefenseby1')>1:
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was lowered.')
        elif pokemonstatchanges.count('lowerspecialdefenseby1')==6:
            print('The special defense of', next(iter(team)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerspecialdefenseby2':
        if pokemonstatchanges.count('raisespecialdefenseby1')==1:
            pokemonstatchanges.remove('raisespecialdefenseby1')
            pokemonstatchanges.append('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raisespecialdefenseby1')>1:
            pokemonstatchanges.remove('raisespecialdefenseby1')
            pokemonstatchanges.remove('raisespecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was sharply lowered.')
        elif pokemonstatchanges.count('lowerspecialdefenseby1')==6:
            print('The special defense of', next(iter(team)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerspecialdefenseby1')
            pokemonstatchanges.append('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team)), 'was sharply lowered.')
    elif allmoves[opponentmove]['effect']=='raisespecialdefenseby1':
        if opponentstatchanges.count('lowerspecialdefenseby1')==1:
            opponentstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('lowerspecialdefenseby1')>1:
            opponentstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was raised.')
        elif pokemonstatchanges.count('raisespecialdefenseby1')==6:
            print('The special defense of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raisespecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was raised.')
    elif allmoves[opponentmove]['effect']=='raisespecialdefenseby2':
        if opponentstatchanges.count('lowerspecialdefenseby1')==1:
            opponentstatchanges.remove('lowerspecialdefenseby1')
            opponentstatchanges.append('raisespecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('lowerspecialdefenseby1')>1:
            opponentstatchanges.remove('lowerspecialdefenseby1')
            opponentstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('raisespecialdefenseby1')==6:
            print('The special defense of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raisespecialdefenseby1')
            opponentstatchanges.append('raisespecialdefenseby1')
            print('The special defense of', next(iter(opponents[opponent])), 'was sharply raised.')

def userdamage(opponent, move):
    level = party[next(iter(team))]['level']
    power = allmoves[move]['bp']
    if allmoves[move]['category']=='physical':
        if pokemonstatchanges.count('raiseattackby1') > 1:
            t = pokemonstatchanges.count('raiseattackby1')
            c = party[next(iter(team))]['attack']
            if t == 1:
                b=1.5
            elif t == 2:
                b=2
            elif t == 3:
                b=2.5
            elif t == 4:
                b=3
            elif t == 5:
                b=3.5
            else:
                b=6
            a=b*c
        elif pokemonstatchanges.count('lowerattackby1') > 1:
            t = pokemonstatchanges.count('lowerattackby1')
            c = party[next(iter(team))]['attack']
            if t == 1:
                b=2/3
            elif t == 2:
                b=.5
            elif t == 3:
                b=.4
            elif t == 4:
                b=1/3
            elif t == 5:
                b=2/7
            else:
                b=.25
            a=b*c
        else:
            a = party[next(iter(team))]['attack']
    else:
        if pokemonstatchanges.count('raisespecialattackby1') > 1:
            t = pokemonstatchanges.count('raisespecialattackby1')
            c = party[next(iter(team))]['special attack']
            if t == 1:
                b=1.5
            elif t == 2:
                b=2
            elif t == 3:
                b=2.5
            elif t == 4:
                b=3
            elif t == 5:
                b=3.5
            else:
                b=6
            a=b*c
        elif pokemonstatchanges.count('lowerspecialattackby1') > 1:
            t = pokemonstatchanges.count('lowerspecialattackby1')
            c = party[next(iter(team))]['special attack']
            if t == 1:
                b=2/3
            elif t == 2:
                b=.5
            elif t == 3:
                b=.4
            elif t == 4:
                b=1/3
            elif t == 5:
                b=2/7
            else:
                b=.25
            a=b*c
        else:
            a = party[next(iter(team))]['special attack']
    if allmoves[move]['category']=='physical':
        if opponentstatchanges.count('raisedefenseby1') > 1:
            t = opponentstatchanges.count('raisedefenseby1')
            c = opponents[opponent][next(iter(opponents[opponent]))]['defense']
            if t == 1:
                b=1.5
            elif t == 2:
                b=2
            elif t == 3:
                b=2.5
            elif t == 4:
                b=3
            elif t == 5:
                b=3.5
            else:
                b=6
            d=b*c
        elif opponentstatchanges.count('lowerdefenseby1') > 1:
            t = opponentstatchanges.count('lowerdefenseby1')
            c = opponents[opponent][next(iter(opponents[opponent]))]['defense']
            if t == 1:
                b=2/3
            elif t == 2:
                b=.5
            elif t == 3:
                b=.4
            elif t == 4:
                b=1/3
            elif t == 5:
                b=2/7
            else:
                b=.25
            d=b*c
        else:
            d = opponents[opponent][next(iter(opponents[opponent]))]['defense']
    else:
        if opponentstatchanges.count('raisespecialdefenseby1') > 1:
            t = opponentstatchanges.count('raisespecialdefenseby1')
            c = opponents[opponent][next(iter(opponents[opponent]))]['special defense']
            if t == 1:
                b=1.5
            elif t == 2:
                b=2
            elif t == 3:
                b=2.5
            elif t == 4:
                b=3
            elif t == 5:
                b=3.5
            else:
                b=6
            d=b*c
        elif opponentstatchanges.count('lowerspecialdefenseby1') > 1:
            t = opponentstatchanges.count('lowerspecialdefenseby1')
            c = opponents[opponent][next(iter(opponents[opponent]))]['special defense']
            if t == 1:
                b=2/3
            elif t == 2:
                b=.5
            elif t == 3:
                b=.4
            elif t == 4:
                b=1/3
            elif t == 5:
                b=2/7
            else:
                b=.25
            d=b*c
        else:
            d = opponents[opponent][next(iter(opponents[opponent]))]['special defense']
    h = random.randint(1,16)
    if h == 1:
        crit=1.5
    else:
        crit=1
    i = random.randint(85,100)
    rand = i/100
    if allmoves[move]['type']=='fire':
        firemoveopponent(opponent)
    elif allmoves[move]['type']=='grass':
        grassmoveopponent(opponent)
    elif allmoves[move]['type']=='water':
        watermoveopponent(opponent)
    elif allmoves[move]['type']=='ice':
        icemoveopponent(opponent)
    elif allmoves[move]['type']=='ground':
        groundmoveopponent(opponent)
    elif allmoves[move]['type']=='electric':
        electricmoveopponent(opponent)
    elif allmoves[move]['type']=='flying':
        flyingmoveopponent(opponent)
    elif allmoves[move]['type']=='ghost':
        ghostmoveopponent(opponent)
    elif allmoves[move]['type']=='rock':
        rockmoveopponent(opponent)
    elif allmoves[move]['type']=='poison':
        poisonmoveopponent(opponent)
    elif allmoves[move]['type']=='psychic':
        psychicmoveopponent(opponent)
    elif allmoves[move]['type']=='bug':
        bugmoveopponent(opponent)
    elif allmoves[move]['type']=='fighting':
        fightingmoveopponent(opponent)
    else:
        normalmoveopponent(opponent)
    if party[next(iter(team))]['type1'] == allmoves[move]['type']:
        stab = 1.5
    elif party[next(iter(team))]['type2'] == allmoves[move]['type']:
        stab = 1.5
    else:
        stab = 1
    if party[next(iter(team))]['status']=='burn':
                burn = .5
    else:
        burn = 1
    modifier =  crit*rand*stab*type*burn
    global damage
    damage = ((((((2*level)/5)+2)*power*(a/d))/50)+2)*modifier
    print(next(iter(team)), 'used', move)
    if type>1:
        print("It's super effective!")
    elif type<1:
        print("It's not very effective!")
    o = int(damage)
    if opponents[opponent][next(iter(opponents[opponent]))]['hp']-o<0:
        o=opponents[opponent][next(iter(opponents[opponent]))]['hp']
    if o>1:
        print(next(iter(opponents[opponent])), "lost", o, "hit points!")
    else:
        print(next(iter(opponents[opponent])), "lost", o, "hit point!")
    x = opponents[opponent][next(iter(opponents[opponent]))]['hp']-o
    opponents[opponent][next(iter(opponents[opponent]))]['hp'] = x
    if allmoves[move]['effect']=='10%burn':
        h = random.randint(1,10)
        if h == 1:
            if opponents[opponent][next(iter(opponents[opponent]))]['status']=='none':
                print(next(iter(opponents[opponent])), "was burned!")
                opponents[opponent][next(iter(opponents[opponent]))]['status']='burn'

def opponentdamage(opponent, opponentmove):
    level = opponents[opponent][next(iter(opponents[opponent]))]['level']
    power = allmoves[opponentmove]['bp']
    if allmoves[move]['category']=='physical':
        if opponentstatchanges.count('raiseattackby1') > 1:
            t = opponentstatchanges.count('raiseattackby1')
            c = opponents[opponent][next(iter(opponents[opponent]))]['attack']
            if t == 1:
                b=1.5
            elif t == 2:
                b=2
            elif t == 3:
                b=2.5
            elif t == 4:
                b=3
            elif t == 5:
                b=3.5
            else:
                b=6
            a=b*c
        elif opponentstatchanges.count('lowerattackby1') > 1:
            t = opponentstatchanges.count('lowerattackby1')
            c = opponents[opponent][next(iter(opponents[opponent]))]['attack']
            if t == 1:
                b=2/3
            elif t == 2:
                b=.5
            elif t == 3:
                b=.4
            elif t == 4:
                b=1/3
            elif t == 5:
                b=2/7
            else:
                b=.25
            a=b*c
        else:
            a = opponents[opponent][next(iter(opponents[opponent]))]['attack']
    else:
        if opponentstatchanges.count('raisespecialattackby1') > 1:
            t = opponentstatchanges.count('raisespecialattackby1')
            c = opponents[opponent][next(iter(opponents[opponent]))]['special attack']
            if t == 1:
                b=1.5
            elif t == 2:
                b=2
            elif t == 3:
                b=2.5
            elif t == 4:
                b=3
            elif t == 5:
                b=3.5
            else:
                b=6
            a=b*c
        elif opponentstatchanges.count('lowerspecialattackby1') > 1:
            t = opponentstatchanges.count('lowerspecialattackby1')
            c = opponents[opponent][next(iter(opponents[opponent]))]['special attack']
            if t == 1:
                b=2/3
            elif t == 2:
                b=.5
            elif t == 3:
                b=.4
            elif t == 4:
                b=1/3
            elif t == 5:
                b=2/7
            else:
                b=.25
            a=b*c
        else:
            a = opponents[opponent][next(iter(opponents[opponent]))]['special attack']
    if allmoves[move]['category']=='physical':
        if pokemonstatchanges.count('raisedefenseby1') > 1:
            t = pokemonstatchanges.count('raisedefenseby1')
            c = party[next(iter(team))]['defense']
            if t == 1:
                b=1.5
            elif t == 2:
                b=2
            elif t == 3:
                b=2.5
            elif t == 4:
                b=3
            elif t == 5:
                b=3.5
            else:
                b=6
            d=b*c
        elif pokemonstatchanges.count('lowerdefenseby1') > 1:
            t = pokemonstatchanges.count('lowerdefenseby1')
            c = party[next(iter(team))]['defense']
            if t == 1:
                b=2/3
            elif t == 2:
                b=.5
            elif t == 3:
                b=.4
            elif t == 4:
                b=1/3
            elif t == 5:
                b=2/7
            else:
                b=.25
            d=b*c
        else:
            d = party[next(iter(team))]['defense']
    else:
        if pokemonstatchanges.count('raisespecialdefenseby1') > 1:
            t = pokemonstatchanges.count('raisespecialdefenseby1')
            c = party[next(iter(team))]['special defense']
            if t == 1:
                b=1.5
            elif t == 2:
                b=2
            elif t == 3:
                b=2.5
            elif t == 4:
                b=3
            elif t == 5:
                b=3.5
            else:
                b=6
            d=b*c
        elif pokemonstatchanges.count('lowerspecialdefenseby1') > 1:
            t = pokemonstatchanges.count('lowerspecialdefenseby1')
            c = party[next(iter(team))]['special defense']
            if t == 1:
                b=2/3
            elif t == 2:
                b=.5
            elif t == 3:
                b=.4
            elif t == 4:
                b=1/3
            elif t == 5:
                b=2/7
            else:
                b=.25
            d=b*c
        else:
            d = party[next(iter(team))]['special defense']
    h = random.randint(1,16)
    if h == 1:
        crit=1.5
    else:
        crit=1
    i = random.randint(85,100)
    rand = i/100
    if allmoves[opponentmove]['type']=='fire':
        firemove()
    elif allmoves[opponentmove]['type']=='grass':
        grassmove()
    elif allmoves[opponentmove]['type']=='water':
        watermove()
    elif allmoves[opponentmove]['type']=='ice':
        icemove()
    elif allmoves[opponentmove]['type']=='ground':
        groundmove()
    elif allmoves[opponentmove]['type']=='electric':
        electricmove()
    elif allmoves[opponentmove]['type']=='flying':
        flyingmove()
    elif allmoves[opponentmove]['type']=='ghost':
        ghostmove()
    elif allmoves[opponentmove]['type']=='rock':
        rockmove()
    elif allmoves[opponentmove]['type']=='poison':
        poisonmove()
    elif allmoves[opponentmove]['type']=='psychic':
        psychicmove()
    elif allmoves[opponentmove]['type']=='bug':
        bugmove()
    elif allmoves[opponentmove]['type']=='fighting':
        fightingmove()
    else:
        normalmove()
    if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == allmoves[move]['type']:
        stab = 1.5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == allmoves[move]['type']:
        stab = 1.5
    else:
        stab = 1
    if opponents[opponent][next(iter(opponents[opponent]))]['status']=='burn':
                burn = .5
    else:
        burn = 1
    modifier =  crit*rand*stab*type*burn
    global damage
    damage = ((((((2*level)/5)+2)*power*(a/d))/50)+2)*modifier
    print(next(iter(opponents[opponent])), "used", opponentmove)
    if type>1:
        print("It's super effective!")
    elif type<1:
        print("It's not very effective!")
    o = int(damage)
    if party2[next(iter(team))]['hp']-o<0:
        o=party2[next(iter(team))]['hp']
    if o>1:
        print(next(iter([next(iter(team))])), "lost", o, "hit points!")
    else:
        print(next(iter([next(iter(team))])), "lost", o, "hit point!")
    x = party2[next(iter(team))]['hp']-o
    party2[next(iter(team))]['hp'] = x
    if allmoves[opponentmove]['effect']=='10%burn':
        h = random.randint(1,10)
        h=1
        if h == 1:
            if team2[next(iter(team))]=='none':
                print(next(iter(team)), "was burned!")
                team2[next(iter(team))]='burn'

def shifting():
    if w == 0:
        a = team2[q]
        b=list(team2.keys())[1]
        c=list(team2.values())[1]
        d=list(team2.keys())[2]
        e=list(team2.values())[2]
        f=list(team2.keys())[3]
        g=list(team2.values())[3]
        h=list(team2.keys())[4]
        i=list(team2.values())[4]
        j=list(team2.keys())[5]
        k=list(team2.values())[5]
        team2.clear()
        team2[q]=a
        team2[b]=c
        team2[d]=e
        team2[f]=g
        team2[h]=i
        team2[j]=k
    elif w == 1:
        a = team2[q]
        b=list(team2.keys())[0]
        c=list(team2.values())[0]
        d=list(team2.keys())[2]
        e=list(team2.values())[2]
        f=list(team2.keys())[3]
        g=list(team2.values())[3]
        h=list(team2.keys())[4]
        i=list(team2.values())[4]
        j=list(team2.keys())[5]
        k=list(team2.values())[5]
        team2.clear()
        team2[q]=a
        team2[b]=c
        team2[d]=e
        team2[f]=g
        team2[h]=i
        team2[j]=k
    elif w == 2:
        a = team2[q]
        b=list(team2.keys())[0]
        c=list(team2.values())[0]
        d=list(team2.keys())[1]
        e=list(team2.values())[1]
        f=list(team2.keys())[3]
        g=list(team2.values())[3]
        h=list(team2.keys())[4]
        i=list(team2.values())[4]
        j=list(team2.keys())[5]
        k=list(team2.values())[5]
        team2.clear()
        team2[q]=a
        team2[b]=c
        team2[d]=e
        team2[f]=g
        team2[h]=i
        team2[j]=k
    elif w == 3:
        a = team2[q]
        b=list(team2.keys())[0]
        c=list(team2.values())[0]
        d=list(team2.keys())[1]
        e=list(team2.values())[1]
        f=list(team2.keys())[2]
        g=list(team2.values())[2]
        h=list(team2.keys())[4]
        i=list(team2.values())[4]
        j=list(team2.keys())[5]
        k=list(team2.values())[5]
        team2.clear()
        team2[q]=a
        team2[b]=c
        team2[d]=e
        team2[f]=g
        team2[h]=i
        team2[j]=k
    elif w == 4:
        a = team2[q]
        b=list(team2.keys())[0]
        c=list(team2.values())[0]
        d=list(team2.keys())[1]
        e=list(team2.values())[1]
        f=list(team2.keys())[2]
        g=list(team2.values())[2]
        h=list(team2.keys())[3]
        i=list(team2.values())[3]
        j=list(team2.keys())[5]
        k=list(team2.values())[5]
        team2.clear()
        team2[q]=a
        team2[b]=c
        team2[d]=e
        team2[f]=g
        team2[h]=i
        team2[j]=k
    else:
        a = team2[q]
        b=list(team2.keys())[0]
        c=list(team2.values())[0]
        d=list(team2.keys())[1]
        e=list(team2.values())[1]
        f=list(team2.keys())[2]
        g=list(team2.values())[2]
        h=list(team2.keys())[3]
        i=list(team2.values())[3]
        j=list(team2.keys())[4]
        k=list(team2.values())[4]
        team.clear()
        team2[q]=a
        team2[b]=c
        team2[d]=e
        team2[f]=g
        team2[h]=i
        team2[j]=k
    global v
    v = 7

def battle(opponent, cash):
    global team2
    team2 = copy.deepcopy(team)
    global party3
    global rr
    party3=copy.deepcopy(party2)
    print(opponent, "has challenged you to battle!")
    print(opponent, "sent out %s!" %(next(iter(opponents[opponent]))))
    print(name, "sent out %s!" %(next(iter(team))))
    while len(opponents[opponent])!=0:
        g = input("Battle\nBag\nSwitch\nRun\n")
        g = g.title()
        if g == "Bag":
            print(bag)
            global q
            global w
            global money
            item = input("Which item would you like to use?\n")
            item=item.title()
            v=1
            while v == 1:
                if item == "Potion":
                    print(team)
                    aa=input("Which Pokemon would you like to heal up?\n")
                    aa=aa.title()
                    u=1
                    while u==1:
                        if party2[aa]['hp']==0:
                            print(aa, "has already fainted!")
                        elif party2[aa]['hp']==party[aa]['hp']:
                            print("It will have no effect!")
                        elif aa not in party2:
                            print(aa, "is not a Pokemon in your party!")
                        else:
                            if party2[aa]['hp']+10>party[aa]['hp']:
                                bb=party[aa]['hp']-party2[aa]['hp']
                                print(aa, "was healed up by",bb, "HP")
                                cc=party2[aa]['hp']+bb
                            else:
                                bb=party2[aa]['hp']+10
                                party2[aa]['hp']=bb
                            u=2
                            m = random.randint(1,4)
                            while opponents[opponent][next(iter(opponents[opponent]))][m]=='none':
                                m = random.randint(1,4)
                                opponentmove=opponents[opponent][next(iter(opponents[opponent]))][m]
                                if allmoves[opponentmove]['category']== 'status':
                                    opponentstatusmove(opponent,opponentmove)
                                else:
                                    opponentdamage(opponent,opponentmove)
                                if party2[next(iter(team))]['hp']<=0:
                                    print(next(iter(team)), "fainted!")
                                    pokemonstatchanges.clear()
                                    del party3[next(iter(team))]
                                    if len(party3)==0:
                                        print("You blacked out")
                                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                        money = money/2
                                        break
                                    else:
                                        print(team)
                                        v == 5
                                        while v == 5:
                                            q=input("Which Pokemon would you like to send out?")
                                            q=q.title()
                                            w = list(team.keys()).index(q)
                                            if party2[q]['hp']<=0:
                                                print(q, "has no strength to battle.")
                                            else:
                                                shifting()
                        u=2
                    v=2
            if party[next(iter(team))]['status']=='burn':
                x=party[next(iter(team))]['hp']*0.0625
                x=int(x)
                if party2[next(iter(team))]['hp']-x<0:
                    x=party2[next(iter(team))]
                i = party2[next(iter(team))]['hp']-x
                party2[next(iter(team))]['hp']=i
                print(next(iter(team)), "was hurt by the burn")
                if x==1:
                    print(next(iter(team)), "lost", x, "hit point.")
                else:
                    print(next(iter(team)), "lost", x, "hit points.")
                if party2[next(iter(team))]['hp']<=0:
                    print(next(iter(team)), "fainted!")
                    pokemonstatchanges.clear()
                    del party3[next(iter(team))]
                    if len(party3)==0:
                        print("You blacked out")
                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                        money=money/2
                        break
                    else:
                        print(team)
                        v == 5
                        while v == 5:
                            q=input("Which Pokemon would you like to send out?")
                            q=q.title()
                            w = list(team.keys()).index(q)
                            if party2[q]['hp']<=0:
                                print(q, "has no strength to battle.")
                            else:
                                shifting()
            if opponents[opponent][next(iter(opponents[opponent]))]['status']=='burn':
                x=opponents2[opponent][next(iter(opponents[opponent]))]['hp']*0.0625
                x=int(x)
                if opponents[opponent][next(iter(opponents[opponent]))]['hp']-x<0:
                    x=opponents[opponent][next(iter(opponents[opponent]))]
                i = opponents[opponent][next(iter(opponents[opponent]))]['hp']-x
                opponents[opponent][next(iter(opponents[opponent]))]['hp']=i
                print(next(iter(opponents[opponent])), "was hurt by the burn")
                if x==1:
                    print(next(iter(opponents[opponent])), "lost", x, "hit point.")
                else:
                    print(next(iter(opponents[opponent])), "lost", x, "hit points.")
                if opponents[opponent][next(iter(opponents[opponent]))]['hp']<=0:
                    print(next(iter(opponents[opponent])), "fainted!")
                    oo = party[next(iter(party2))]['exp needed to level up']-opponents[opponent][next(iter(opponents[opponent]))]['exp']
                    if oo<=0:
                        if party[next(iter(party2))]['level']<100:
                            print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                            print(next(iter(party2)), "leveled up!")
                            hh = party[next(iter(party2))]['level']+1
                            party[next(iter(party2))]['level']=hh
                            rr = party[next(iter(party2))]['level']-1
                            party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                        else:
                            break
                    else:
                        print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                        party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                    opponentstatchanges.clear()
                    del opponents[opponent][next(iter(opponents[opponent]))]
            print("Your %s: %s HP"%(next(iter(party2)), party2[next(iter(party2))]['hp']))
            print("Opponent's %s: %s HP"%(next(iter(opponents[opponent])), opponents[opponent][next(iter(opponents[opponent]))]['hp']))
        elif g == "Switch":
            print(team)
            q = input("Which would Pokemon would you like to send out?\n")
            q = q.title()
            v = 5
            while v == 5:
                if q == next(iter(team2)):
                    print(q, "is already on the field!")
                    q = input("Which Pokemon would you like to send out?\n")
                    q = q.title()
                elif q == "Back":
                    break
                elif party2[q]['hp']<=0:
                    print(q, "has no strength to battle")
                else:
                    print("Good job", next(iter(team2)), "Go", q)
                    w = list(team2.keys()).index(q)
                    shifting()
                    m = random.randint(1,4)
                    while opponents[opponent][next(iter(opponents[opponent]))][m]=='none':
                        m = random.randint(1,4)
                        opponentmove=opponents[opponent][next(iter(opponents[opponent]))][m]
                    if allmoves[opponentmove]['category']== 'status':
                        opponentstatusmove(opponent,opponentmove)
                    else:
                        opponentdamage(opponent,opponentmove)
                        if party2[next(iter(team))]['hp']<=0:
                            print(next(iter(team)), "fainted!")
                            pokemonstatchanges.clear()
                            del party3[next(iter(team))]
                            if len(party3)==0:
                                print("You blacked out")
                                print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                money = money/2
                                break
                            else:
                                print(team)
                                v == 5
                                while v == 5:
                                    q=input("Which Pokemon would you like to send out?")
                                    q=q.title()
                                    w = list(team.keys()).index(q)
                                    if party2[q]['hp']<=0:
                                        print(q, "has no strength to battle.")
                                    else:
                                        shifting()
                        else:
                            v = 7
            if party[next(iter(team))]['status']=='burn':
                x=party[next(iter(team))]['hp']*0.0625
                x=int(x)
                if party2[next(iter(team))]['hp']-x<0:
                    x=party2[next(iter(team))]
                i = party2[next(iter(team))]['hp']-x
                party2[next(iter(team))]['hp']=i
                print(next(iter(team)), "was hurt by the burn")
                if x==1:
                    print(next(iter(team)), "lost", x, "hit point.")
                else:
                    print(next(iter(team)), "lost", x, "hit points.")
                if party2[next(iter(team))]['hp']<=0:
                    print(next(iter(team)), "fainted!")
                    pokemonstatchanges.clear()
                    del party3[next(iter(team))]
                    if len(party3)==0:
                        print("You blacked out")
                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                        money=money/2
                        break
                    else:
                        print(team)
                        v == 5
                        while v == 5:
                            q=input("Which Pokemon would you like to send out?")
                            q=q.title()
                            w = list(team.keys()).index(q)
                            if party2[q]['hp']<=0:
                                print(q, "has no strength to battle.")
                            else:
                                shifting()
            if opponents[opponent][next(iter(opponents[opponent]))]['status']=='burn':
                x=opponents2[opponent][next(iter(opponents[opponent]))]['hp']*0.0625
                x=int(x)
                if opponents[opponent][next(iter(opponents[opponent]))]['hp']-x<0:
                    x=opponents[opponent][next(iter(opponents[opponent]))]
                i = opponents[opponent][next(iter(opponents[opponent]))]['hp']-x
                opponents[opponent][next(iter(opponents[opponent]))]['hp']=i
                print(next(iter(opponents[opponent])), "was hurt by the burn")
                if x==1:
                    print(next(iter(opponents[opponent])), "lost", x, "hit point.")
                else:
                    print(next(iter(opponents[opponent])), "lost", x, "hit points.")
                if opponents[opponent][next(iter(opponents[opponent]))]['hp']<=0:
                    print(next(iter(opponents[opponent])), "fainted!")
                    oo = party2[next(iter(party2))]['exp needed to level up']-opponents[opponent][next(iter(opponents[opponent]))]['exp']
                    if oo<=0:
                        if party[next(iter(party2))]['level']<100:
                            print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                            print(next(iter(party2)), "leveled up!")
                            hh = party[next(iter(party2))]['level']+1
                            party[next(iter(party2))]['level']=hh
                            rr = party[next(iter(party2))]['level']-1
                            party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                        else:
                            break
                    else:
                        print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                        party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                    opponentstatchanges.clear()
                    del opponents[opponent][next(iter(opponents[opponent]))]
                    v = 7
            print("Your %s: %s HP"%(next(iter(party2)), party2[next(iter(party2))]['hp']))
            print("Opponent's %s: %s HP"%(next(iter(opponents[opponent])), opponents[opponent][next(iter(opponents[opponent]))]['hp']))
        elif g == "Battle":
            print(party2[next(iter(team))][1],"\n",party2[next(iter(team))][2],"\n",party2[next(iter(team))][3],"\n",party2[next(iter(team))][4])
            global move
            move = input("Which move would you like to use?\n")
            move = move.title()
            j = 5
            while j==5:
                if move == party2[next(iter(team))][1]:
                    break
                elif move == party2[next(iter(team))][2]:
                    break
                elif move == party2[next(iter(team))][3]:
                    break
                elif move == party2[next(iter(team))][4]:
                    break
                else:
                    print("That is not a valid move.")
                    move = input("Which move would you like to use?\n")
                    move = move.title()
            m = random.randint(1,4)
            while opponents[opponent][next(iter(opponents[opponent]))][m]=='none':
                m = random.randint(1,4)
            opponentmove=opponents[opponent][next(iter(opponents[opponent]))][m]
            if party2[next(iter(team))]['speed']>opponents[opponent][next(iter(opponents[opponent]))]['speed']:
                if allmoves[move]['category']=='status':
                    userstatusmove(move, opponent)
                    if opponents[opponent][next(iter(opponents[opponent]))]['hp']>0:
                        if allmoves[opponentmove]['category']=='status':
                            opponentstatusmove(opponent,opponentmove)
                        else:
                            opponentdamage(opponent,opponentmove)
                            if party[next(iter(team))]['hp']<=0:
                                print(next(iter(team)), "fainted!")
                                pokemonstatchanges.clear()
                                del party3[next(iter(team))]
                                if len(party3)==0:
                                    print("You blacked out")
                                    print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                    money=money/2
                                    break
                                else:
                                    print(team)
                                    v == 5
                                    while v == 5:
                                        q=input("Which Pokemon would you like to send out?")
                                        q=q.title()
                                        w = list(team.keys()).index(q)
                                        if party2[q]['hp']<=0:
                                            print(q, "has no strength to battle.")
                                        else:
                                            shifting()
                else:
                    userdamage(opponent,move)
                    if opponents[opponent][next(iter(opponents[opponent]))]['hp']>0:
                        if allmoves[opponentmove]['category']=='status':
                            opponentstatusmove(opponent,opponentmove)
                        else:
                            opponentdamage(opponent,opponentmove)
                    else:
                        print(next(iter(opponents[opponent])), "fainted!")
                        oo = party2[next(iter(party2))]['exp needed to level up']-opponents[opponent][next(iter(opponents[opponent]))]['exp']
                        if oo<=0:
                            if party[next(iter(party2))]['level']<100:
                                print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                                print(next(iter(party2)), "leveled up!")
                                hh = party[next(iter(party2))]['level']+1
                                party[next(iter(party2))]['level']=hh
                                rr = party[next(iter(party2))]['level']-1
                                party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                            else:
                                break
                        else:
                            print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                            party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                        opponentstatchanges.clear()
                        del opponents[opponent][next(iter(opponents[opponent]))]
            elif party2[next(iter(team))]['speed']==opponents[opponent][next(iter(opponents[opponent]))]['speed']:
                speedtie=random.randint(1,2)
                if speedtie==1:
                    if allmoves[move]['category']=='status':
                        userstatusmove(move, opponent)
                        if opponents[opponent][next(iter(opponents[opponent]))]['hp']>0:
                            if allmoves[opponentmove]['category']=='status':
                                opponentstatusmove(opponent,opponentmove)
                            else:
                                opponentdamage(opponent,opponentmove)
                                if party[next(iter(team))]['hp']<=0:
                                    print(next(iter(team)), "fainted!")
                                    pokemonstatchanges.clear()
                                    del party3[next(iter(team))]
                                    if len(party3)==0:
                                        print("You blacked out")
                                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                        money=money/2
                                        break
                                    else:
                                        print(team)
                                        v == 5
                                        while v == 5:
                                            q=input("Which Pokemon would you like to send out?")
                                            q=q.title()
                                            w = list(team.keys()).index(q)
                                            if party2[q]['hp']<=0:
                                                print(q, "has no strength to battle.")
                                            else:
                                                shifting()
                    else:
                        userdamage(opponent,move)
                        if opponents[opponent][next(iter(opponents[opponent]))]['hp']>0:
                            if allmoves[opponentmove]['category']=='status':
                                opponentstatusmove(opponent, opponentmove)
                            else:
                                opponentdamage(opponent,opponentmove)
                                if party[next(iter(team))]['hp']<=0:
                                    print(next(iter(team)), "fainted!")
                                    pokemonstatchanges.clear()
                                    del party3[next(iter(team))]
                                    if len(party3)==0:
                                        print("You blacked out")
                                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                        money=money/2
                                        break
                                    else:
                                        print(team)
                                        v == 5
                                        while v == 5:
                                            q=input("Which Pokemon would you like to send out?")
                                            q=q.title()
                                            w = list(team.keys()).index(q)
                                            if party2[q]['hp']<=0:
                                                print(q, "has no strength to battle.")
                                            else:
                                                shifting()
                        else:
                            print(next(iter(opponents[opponent])), "fainted!")
                            oo = party2[next(iter(party2))]['exp needed to level up']-opponents[opponent][next(iter(opponents[opponent]))]['exp']
                            if oo<=0:
                                if party[next(iter(party2))]['level']<100:
                                    print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                                    print(next(iter(party2)), "leveled up!")
                                    hh = party[next(iter(party2))]['level']+1
                                    party[next(iter(party2))]['level']=hh
                                    rr = party[next(iter(party2))]['level']-1
                                    party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                                else:
                                    break
                            else:
                                print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                                party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                            opponentstatchanges.clear()
                            del opponents[opponent][next(iter(opponents[opponent]))]
                else:
                    if allmoves[opponentmove]['category']=='status':
                        opponentstatusmove(opponent, opponentmove)
                        if allmoves[move]['category']=='status':
                            userstatusmove(move, opponent)
                        else:
                            userdamage(opponent,move)
                            if opponents[opponent][next(iter(opponents[opponent]))]['hp']<=0:
                                print(next(iter(opponents[opponent])), "fainted!")
                                opponentstatchanges.clear()
                                del opponents[opponent][next(iter(opponents[opponent]))]
                    else:
                        opponentdamage(opponent,opponentmove)
                        if party[next(iter(team))]['hp']>0:
                            if allmoves[move]['category']=='status':
                                userstatusmove(move,opponent)
                            else:
                                userdamage(opponent,move)
                                if opponents[opponent][next(iter(opponents[opponent]))]['hp']<=0:
                                    print(next(iter(opponents[opponent])), "fainted!")
                                    oo = party[next(iter(party2))]['exp needed to level up']-opponents[opponent][next(iter(opponents[opponent]))]['exp']
                                    if oo<=0:
                                        if party[next(iter(party2))]['level']<100:
                                            print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                                            print(next(iter(party2)), "leveled up!")
                                            hh = party[next(iter(party2))]['level']+1
                                            party[next(iter(party2))]['level']=hh
                                            rr = party[next(iter(party2))]['level']-1
                                            party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                                        else:
                                            break
                                    else:
                                        print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                                        party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                                    opponentstatchanges.clear()
                                    del opponents[opponent][next(iter(opponents[opponent]))]
                        else:
                            print(next(iter(team)), "fainted!")
                            pokemonstatchanges.clear()
                            del party3[next(iter(team))]
                            if len(party3)==0:
                                print("You blacked out")
                                print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                money=money/2
                                break
                            else:
                                print(team)
                                v == 5
                                while v == 5:
                                    q=input("Which Pokemon would you like to send out?")
                                    q=q.title()
                                    w = list(team.keys()).index(q)
                                    if party2[q]['hp']<=0:
                                        print(q, "has no strength to battle.")
                                    else:
                                        shifting()
            else:
                if allmoves[opponentmove]['category']=='status':
                    opponentstatusmove(opponent, opponentmove)
                    if allmoves[move]['category']=='status':
                        userstatusmove(move, opponent)
                    else:
                        userdamage(opponent,move)
                        if opponents[opponent][next(iter(opponents[opponent]))]['hp']<=0:
                            print(next(iter(opponents[opponent])), "fainted!")
                            oo = party2[next(iter(party2))]['exp needed to level up']-opponents[opponent][next(iter(opponents[opponent]))]['exp']
                            if oo<=0:
                                if party[next(iter(party2))]['level']<100:
                                    print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                                    print(next(iter(party2)), "leveled up!")
                                    hh = party[next(iter(party2))]['level']+1
                                    party[next(iter(party2))]['level']=hh
                                    rr = party[next(iter(party2))]['level']-1
                                    party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                                else:
                                    break
                            else:
                                print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                                party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                            opponentstatchanges.clear()
                            del opponents[opponent][next(iter(opponents[opponent]))]
                else:
                    opponentdamage(opponent,opponentmove)
                    if party[next(iter(team))]['hp']>0:
                        if allmoves[move]['category']=='status':
                            userstatusmove(move,opponent)
                        else:
                            userdamage(opponent,move)
                            if opponents[opponent][next(iter(opponents[opponent]))]['hp']<=0:
                                print(next(iter(opponents[opponent])), "fainted!")
                                oo = party2[next(iter(party2))]['exp needed to level up']-opponents[opponent][next(iter(opponents[opponent]))]['exp']
                                if oo<=0:
                                    if party[next(iter(party2))]['level']<100:
                                        print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                                        print(next(iter(party2)), "leveled up!")
                                        hh = party[next(iter(party2))]['level']+1
                                        party[next(iter(party2))]['level']=hh
                                        rr = party[next(iter(party2))]['level']-1
                                        party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                                    else:
                                        break
                                else:
                                    print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                                    party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                                opponentstatchanges.clear()
                                del opponents[opponent][next(iter(opponents[opponent]))]
                    else:
                        print(next(iter(team)), "fainted!")
                        pokemonstatchanges.clear()
                        del party3[next(iter(team))]
                        if len(party3)==0:
                            print("You blacked out")
                            print("You quickly went back to the Pokemon Center to heal your Pokemon")
                            money=money/2
                            break
                        else:
                            print(team)
                            v == 5
                            while v == 5:
                                q=input("Which Pokemon would you like to send out?")
                                q=q.title()
                                w = list(team.keys()).index(q)
                                if party2[q]['hp']<=0:
                                    print(q, "has no strength to battle.")
                                else:
                                    shifting()
            if len(party3)!=0:
                if party[next(iter(team))]['status']=='burn':
                    x=party[next(iter(team))]['hp']*0.0625
                    x=int(x)
                    if party2[next(iter(team))]['hp']-x<0:
                        x=party2[next(iter(team))]
                    i = party2[next(iter(team))]['hp']-x
                    party2[next(iter(team))]['hp']=i
                    print(next(iter(team)), "was hurt by the burn")
                    if x==1:
                        print(next(iter(team)), "lost", x, "hit point.")
                    else:
                        print(next(iter(team)), "lost", x, "hit points.")
                    if party2[next(iter(team))]['hp']<=0:
                        print(next(iter(team)), "fainted!")
                        pokemonstatchanges.clear()
                        del party3[next(iter(team))]
                        if len(party3)==0:
                            print("You blacked out")
                            print("You quickly went back to the Pokemon Center to heal your Pokemon")
                            money=money/2
                            break
                        else:
                            print(team)
                            v == 5
                            while v == 5:
                                q=input("Which Pokemon would you like to send out?")
                                q=q.title()
                                w = list(team.keys()).index(q)
                                if party2[q]['hp']<=0:
                                    print(q, "has no strength to battle.")
                                else:
                                    shifting()
            if len(opponents[opponent])!=0:
                if opponents[opponent][next(iter(opponents[opponent]))]['status']=='burn':
                    x=opponents2[opponent][next(iter(opponents[opponent]))]['hp']*0.0625
                    x=int(x)
                    if opponents[opponent][next(iter(opponents[opponent]))]['hp']-x<0:
                        x=opponents[opponent][next(iter(opponents[opponent]))]
                    i = opponents[opponent][next(iter(opponents[opponent]))]['hp']-x
                    opponents[opponent][next(iter(opponents[opponent]))]['hp']=i
                    print(next(iter(opponents[opponent])), "was hurt by the burn")
                    if x==1:
                        print(next(iter(opponents[opponent])), "lost", x, "hit point.")
                    else:
                        print(next(iter(opponents[opponent])), "lost", x, "hit points.")
                    if opponents[opponent][next(iter(opponents[opponent]))]['hp']<=0:
                        print(next(iter(opponents[opponent])), "fainted!")
                        oo = party2[next(iter(party2))]['exp needed to level up']-opponents[opponent][next(iter(opponents[opponent]))]['exp']
                        if oo<=0:
                            if party[next(iter(party2))]['level']<100:
                                print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                                print(next(iter(party2)), "leveled up!")
                                hh = party[next(iter(party2))]['level']+1
                                party[next(iter(party2))]['level']=hh
                                rr = party[next(iter(party2))]['level']-1
                                party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                            else:
                                break
                        else:
                            print(next(iter(party2)), 'gained', opponents[opponent][next(iter(opponents[opponent]))]['exp'], 'exp!')
                            party[next(iter(party2))]['exp needed to level up']=20+5*(rr**2)-oo
                        opponentstatchanges.clear()
                        del opponents[opponent][next(iter(opponents[opponent]))]
                        if len(opponents[opponent])!=0:
                            print(opponent, "sent out %s!" %(next(iter(opponents[opponent]))))
            if len(opponents[opponent])==0:
                break
            elif len(party3)==0:
                break
            else:
                print("%s's %s lv. %s: %s HP"%(name, next(iter(party2)), party2[next(iter(party2))]['level'], party2[next(iter(party2))]['hp']))
                print("%s's %s lv. %s: %s HP"%(opponent, next(iter(opponents[opponent])), opponents[opponent][next(iter(opponents[opponent]))]['level'],opponents[opponent][next(iter(opponents[opponent]))]['hp']))
        elif g == 'Run':
            print("You can't run away from a Pokemon battle!")
        else:
            print("That's not a valid choice")
    if len(party3)!=0:
        print("%s beat %s. %s got $%s."%(name, opponent, name, cash))
        money = money+cash
xx=1
while xx==1:
    battle(rivalname, 100)
    party2 = copy.deepcopy(party)
    if starter == 'Bulbasaur':
        rival['Charmander']=rivalpokemon['Charmander']
        rival['Charmander']['hp']=20
        rivalstarter = 'Charmander'
    elif starter == 'Charmander':
        rival['Squirtle']=rivalpokemon['Squirtle']
        rival['Squirtle']['hp']=20
        rivalstarter = 'Squirtle'
    else:
        rival['Bulbasaur']=rivalpokemon['Bulbasaur']
        rival['Bulbasaur']['hp']=20
        rivalstarter = 'Bulbasaur'