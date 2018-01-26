import random
import copy
#define all the pokemon
allpokemon = {'Dewgong' : {1 : 'Ice Beam', 2: 'Surf', 3: 'Growl', 4: 'Blizzard', 'type1':'water', 'type2':'ice', 'level':54, 'status':'none', 'hp':211, 'attack':131, 'defense':142, 'special attack':131, 'special defense':158, 'speed':131},
'Cloyster' : {1 : 'Hydro Pump', 2:'Ice Beam', 3:'Water Pulse', 4:'Blizzard', 'type1': 'water', 'type2':'ice', 'level':53, 'status':'none', 'hp':165, 'attack':155, 'defense':245, 'special attack':144,'special defense':102, 'speed':129},
'Slowbro' : {1 : 'Surf', 2:'Psychic', 3:'Ice Beam', 4:'Shadow Ball', 'type1': 'water', 'type2':'psychic', 'level':54, 'status':'none', 'hp':217, 'attack':136,'defense':174, 'special attack':163,'special defense':142, 'speed':88},
'Jynx' : {1 : 'Ice Beam', 2:'Psychic', 3:'Shadow Ball', 4:'Energy Ball', 'type1': 'ice', 'type2':'psychic', 'level':56, 'status':'none', 'hp':191, 'attack':113,'defense':96, 'special attack':186,'special defense':164, 'speed':164},
'Lapras' : {1 : 'Surf', 2:'Ice Beam', 3:'Thunderbolt', 4:'Psychic', 'type1': 'water', 'type2':'ice', 'level':56, 'status':'none', 'hp':264, 'attack':152,'defense':147, 'special attack':152,'special defense':164, 'speed':124},
'Onix1' : {1 : 'Earthquake', 2:'Rock Slide', 3:'Tackle', 4:'Rock Slide', 'type1': 'rock', 'type2':'ground', 'level':53, 'status':'none', 'hp':149, 'attack':102,'defense':224, 'special attack':86,'special defense':102, 'speed':129},
'Hitmonchan' : {1 : 'Brick Break', 2:'Fire Punch', 3:'Ice Punch', 4:'Thunder Punch', 'type1': 'fighting', 'type2':'none', 'level':55, 'status':'none', 'hp':171, 'attack':172,'defense':143, 'special attack':95,'special defense':177, 'speed':140},
'Hitmonlee' : {1 : 'Jump Kick', 2:'High Jump Kick', 3:'Stone Edge', 4:'Poison Jab', 'type1': 'fighting', 'type2':'none', 'level':55, 'status':'none', 'hp':171, 'attack':188,'defense':115, 'special attack':95,'special defense':177, 'speed':152},
'Onix2' : {1 : 'Earthquake', 2:'Rock Slide', 3:'Tackle', 4:'Stone Edge', 'type1': 'rock', 'type2':'ground', 'level':56, 'status':'none', 'hp':157, 'attack':108,'defense':236, 'special attack':91,'special defense':108, 'speed':136},
'Machamp' : {1 : 'Cross Chop', 2:'Fire Punch', 3:'Ice Punch', 4:'Thunder Punch', 'type1': 'fighting', 'type2':'none', 'level':58, 'status':'none', 'hp':226, 'attack':210,'defense':152, 'special attack':134,'special defense':158, 'speed':123},
'Gengar1' : {1 : 'Shadow Ball', 2:'Sludge Wave', 3:'Focus Blast', 4:'Thunderbolt', 'type1': 'ghost', 'type2':'poison', 'level':56, 'status':'none', 'hp':185, 'attack':130,'defense':124, 'special attack':203,'special defense':141, 'speed':180},
'Golbat' : {1 : 'Sludge Bomb', 2:'Wing Attack', 3:'Aerial Ace', 4:'Hyper Fang', 'type1': 'water', 'type2':'none', 'level':56, 'status':'none', 'hp':202, 'attack':147,'defense':136, 'special attack':130,'special defense':141, 'speed':158},
'Haunter' : {1 : 'Shadow Ball', 2:'Sludge Wave', 3:'Energy Ball', 4:'Thunderbolt', 'type1': 'ghost', 'type2':'poison', 'level':55, 'status':'none', 'hp':166, 'attack':111,'defense':106, 'special attack':183,'special defense':117, 'speed':161},
'Arbok' : {1 : 'Gunk Shot', 2:'Earthquake', 3:'Aqua Tail', 4:'Fire Fang', 'type1': 'poison', 'type2':'none', 'level':58, 'status':'none', 'hp':192, 'attack':169,'defense':139, 'special attack':134,'special defense':151, 'speed':152},
'Gengar2' : {1 : 'Shadow Ball', 2:'Sludge Wave', 3:'Focus Blast', 4:'Thunderbolt', 'type1': 'ghost', 'type2':'poison', 'level':60, 'status':'none', 'hp':198, 'attack':139,'defense':133, 'special attack':217,'special defense':151, 'speed':193},
'Gyarados' : {1 : 'Waterfall', 2:'Stone Edge', 3:'Earthquake', 4:'Tackle', 'type1': 'water', 'type2':'flying', 'level':58, 'status':'none', 'hp':232, 'attack':204,'defense':151, 'special attack':129,'special defense':175, 'speed':153},
'Dragonair1' : {1 : 'Dragon Pulse', 2:'Thunderbolt', 3:'Flamethrower', 4:'Ice Beam', 'type1': 'dragon', 'type2':'none', 'level':56, 'status':'none', 'hp':186, 'attack':151,'defense':130, 'special attack':136,'special defense':136, 'speed':136},
'Dragonair2' : {1 : 'Dragon Pulse', 2:'Thunderbolt', 3:'Flamethrower', 4:'Ice Beam', 'type1': 'dragon', 'type2':'none', 'level':56, 'status':'none', 'hp':186, 'attack':151,'defense':130, 'special attack':136,'special defense':136, 'speed':136},
'Aerodactyl' : {1 : 'Rock Slide', 2:'Wing Attack', 3:'Earthquake', 4:'Fire Fang', 'type1': 'rock', 'type2':'flying', 'level':60, 'status':'none', 'hp':222, 'attack':187,'defense':139, 'special attack':133,'special defense':151, 'speed':217},
'Dragonite' : {1 : 'Thunder Punch', 2:'Fire Punch', 3:'Wing Attack', 4:'Dragon Claw', 'type1': 'dragon', 'type2':'flying', 'level':62, 'status':'none', 'hp':243, 'attack':229,'defense':181, 'special attack':187,'special defense':187, 'speed':162},
'Venusaur' : {1 : 'Energy Ball', 2:'Sludge Bomb', 3:'Earthquake', 4:'Tackle', 'type1': 'grass', 'type2':'poison', 'level':60, 'status':'none', 'hp':222, 'attack':159,'defense':161, 'special attack':181,'special defense':181, 'speed':157},
'Blastoise' : {1 : 'Surf', 2:'Ice Beam', 3:'Tail Whip', 4:'Water Gun', 'type1': 'water', 'type2':'none', 'level':60, 'status':'none', 'hp':221, 'attack':161,'defense':181, 'special attack':163,'special defense':187, 'speed':155},
'Charizard' : {1 : 'Flamethrower', 2:'Fire Blast', 3:'Aerial Ace', 4:'Wing Attack', 'type1': 'fire', 'type2':'flying', 'level':60, 'status':'none', 'hp':220, 'attack':162,'defense':155, 'special attack':192,'special defense':163, 'speed':181},
'Alakazam' : {1 : 'Psychic', 2:'Shadow Ball', 3:'Focus Blast', 4:'Confusion', 'type1': 'psychic', 'type2':'none', 'level':55, 'status':'none', 'hp':177, 'attack':111,'defense':106, 'special attack':205,'special defense':161, 'speed':188},
'Gengar' : {1 : 'Shadow Ball', 2:'Sludge Wave', 3:'Focus Blast', 4:'Thunderbolt', 'type1': 'ghost', 'type2':'poison', 'level':55, 'status':'none', 'hp':182, 'attack':128,'defense':122, 'special attack':199,'special defense':139, 'speed':177},
'Machamp' : {1 : 'Cross Chop', 2:'Fire Punch', 3:'Ice Punch', 4:'Thunder Punch', 'type1': 'fighting', 'type2':'none', 'level':55, 'status':'none', 'hp':215, 'attack':199,'defense':144, 'special attack':128,'special defense':150, 'speed':117}}
#define rival pokemon
rivalpokemon = {'Venusaur' : {1 : 'Energy Ball', 2:'Sludge Bomb', 3:'Earthquake', 4:'Tackle', 'type1': 'grass', 'type2':'poison', 'level':65, 'status':'none', 'hp':240, 'attack':172,'defense':174, 'special attack':196,'special defense':196, 'speed':170},
'Blastoise' : {1 : 'Surf', 2:'Ice Beam', 3:'Tail Whip', 4:'Water Gun', 'type1': 'water', 'type2':'none', 'level':65, 'status':'none', 'hp':238, 'attack':174,'defense':196, 'special attack':176,'special defense':202, 'speed':167},
'Charizard' : {1 : 'Flamethrower', 2:'Fire Blast', 3:'Aerial Ace', 4:'Wing Attack', 'type1': 'fire', 'type2':'flying', 'level':65, 'status':'none', 'hp':237, 'attack':175,'defense':167, 'special attack':207,'special defense':176, 'speed':196},
'Pidgeot' : {1 : 'Wing Attack', 2:'Tackle', 3:'Aerial Ace', 4:'Growl', 'type1': 'normal', 'type2':'flying', 'level':61, 'status':'none', 'hp':229, 'attack':159,'defense':153, 'special attack':147,'special defense':147, 'speed':185},
'Alakazam' : {1 : 'Psychic', 2:'Shadow Ball', 3:'Focus Blast', 4:'Confusion', 'type1': 'psychic', 'type2':'none', 'level':59, 'status':'none', 'hp':189, 'attack':119,'defense':113, 'special attack':219,'special defense':172, 'speed':202},
'Rhydon' : {1 : 'Stone Edge', 2:'Tackle', 3:'Earthquake', 4:'Rock Slide', 'type1': 'ground', 'type2':'rock', 'level':61, 'status':'none', 'hp':256, 'attack':220,'defense':208, 'special attack':117,'special defense':117, 'speed':111},
'Exeggutor' : {1 : 'Psychic', 2:'Energy Ball', 3:'Sludge Bomb', 4:'none', 'type1': 'grass', 'type2':'psychic', 'level':63, 'status':'none', 'hp':251, 'attack':183,'defense':171, 'special attack':221,'special defense':158, 'speed':133},
'Gyarados' : {1 : 'Waterfall', 2:'Stone Edge', 3:'Earthquake', 4:'Tackle', 'type1': 'water', 'type2':'flying', 'level':63, 'status':'none', 'hp':251, 'attack':221,'defense':163, 'special attack':139,'special defense':190, 'speed':166},
'Arcanine' : {1 : 'Flamethrower', 2:'Aerial Ace', 3:'Ember', 4:'Thunder Fang', 'type1': 'fire', 'type2':'none', 'level':63, 'status':'none', 'hp':245, 'attack':202,'defense':165, 'special attack':190,'special defense':165, 'speed':183}}

#define the moves
allmoves = {'Hydro Pump' : {'type':'water', 'category':'special', 'bp':120, 'effect':'none', 'accuracy':80},
'Surf' : {'type':'water', 'category':'special', 'bp':70, 'effect':'none', 'accuracy':100},
'Blizzard' : {'type':'ice', 'category':'special', 'bp':40, 'effect':'none', 'accuracy':100},
'Water Pulse' : {'type':'water', 'category':'special', 'bp':60, 'effect':'none', 'accuracy':100},
'Psychic' : {'type':'psychic', 'category':'special', 'bp':80, 'effect':'none', 'accuracy':100},
'Ice Beam' : {'type':'ice', 'category':'special', 'bp':80, 'effect':'none', 'accuracy':100},
'Growl' : {'type':'normal', 'category':'status', 'effect':'lowerattackby1', 'accuracy':100},
'Shadow Ball' : {'type':'ghost', 'category':'special','bp':80, 'effect':'none', 'accuracy':100},
'Energy Ball' : {'type':'grass', 'category':'special','bp':80, 'effect':'none', 'accuracy':100},
'Thunderbolt' : {'type':'electric', 'category':'special', 'bp':80, 'effect':'none', 'accuracy':100},
'Tackle' : {'type':'normal', 'category':'physical', 'bp':40, 'effect':'none', 'accuracy':100},
'Tail Whip' : {'type':'normal', 'category':'status', 'effect':'lowerdefenseby1', 'accuracy':100},
'Cross Chop' : {'type':'fighting', 'category':'physical', 'bp':120, 'effect':'none', 'accuracy':100},
'Fire Punch' : {'type':'fire', 'category':'physical', 'bp':75, 'effect':'10%burn', 'accuracy':100},
'Ember' : {'type':'fire', 'category':'special', 'bp':40, 'effect':'10%burn', 'accuracy':100},
'Thunder Punch' : {'type':'electric', 'category':'physical', 'bp':75, 'effect':'none', 'accuracy':100},
'Ice Punch' : {'type':'ice', 'category':'physical', 'bp':75, 'effect':'none', 'accuracy':100},
'Earthquake' : {'type':'ground', 'category':'physical', 'bp':100, 'effect':'none', 'accuracy':100},
'Rock Slide' : {'type':'rock', 'category':'physical', 'bp':80, 'effect':'none', 'accuracy':90},
'Stone Edge' : {'type':'rock', 'category':'physical', 'bp':100, 'effect':'none', 'accuracy':80},
'Aqua Tail' : {'type':'water', 'category':'physical', 'bp':90, 'effect':'none', 'accuracy':90},
'Sludge Wave' : {'type':'poison', 'category':'special', 'bp':90, 'effect':'none', 'accuracy':100},
'Sludge Bomb' : {'type':'poison', 'category':'special', 'bp':80, 'effect':'none', 'accuracy':100},
'Focus Blast' : {'type':'fighting', 'category':'special', 'bp':120, 'effect':'none', 'accuracy':75},
'Wing Attack' : {'type':'flying', 'category':'physical','bp':60, 'effect':'none', 'accuracy':100},
'Aerial Ace' : {'type':'flying', 'category':'physical', 'bp':60, 'effect':'none', 'accuracy':100},
'Jump Kick' : {'type':'fighting', 'category':'physical', 'bp':100, 'effect':'none', 'accuracy':90},
'Brick Break' : {'type':'fighting', 'category':'physical', 'bp':75, 'effect':'none', 'accuracy':100},
'High Jump Kick' : {'type':'fighting', 'category':'physical', 'bp':120, 'effect':'none', 'accuracy':75},
'Dragon Claw' : {'type':'dragon', 'category':'physical', 'bp':80, 'effect':'none', 'accuracy':100},
'Flamethrower' : {'type':'fire', 'category':'special', 'bp':80, 'effect':'10%burn', 'accuracy':100},
'Fire Blast' : {'type':'fire', 'category':'special', 'bp':120, 'effect':'10%burn', 'accuracy':80},
'Confusion' : {'type':'psychic', 'category':'special', 'bp':40, 'effect':'none', 'accuracy':100},
'Hyper Fang' : {'type':'normal', 'category':'physical', 'bp':80, 'effect':'none', 'accuracy':90},
'Gunk Shot' : {'type':'poison', 'category':'physical','bp':120, 'effect':'none', 'accuracy':80},
'Fire Fang' : {'type':'fire', 'category':'physical', 'bp':65, 'effect':'10%burn', 'accuracy':95},
'Thunder Fang' : {'type':'electric', 'category':'physical', 'bp':65, 'effect':'none', 'accuracy':95},
'Poison Jab' : {'type':'poison', 'category':'physical', 'bp':80, 'effect':'none', 'accuracy':100},
'Waterfall' : {'type':'water', 'category':'physical', 'bp':80, 'effect':'none', 'accuracy':100}}
team = {"Charizard":allpokemon["Charizard"], "Venusaur":allpokemon["Venusaur"], "Blastoise":allpokemon["Blastoise"], "Alakazam":allpokemon["Alakazam"], "Gengar":allpokemon["Gengar"],"Machamp":allpokemon["Machamp"]}
money = 99999
#get name
class Player(object):
    def __init__(self, name):
        self.name = name
player = Player(input("What is your name?\n"))
#get rival name
rivalname = input("What is your rival's name?\n")
rival = {}
#define statchanges
pokemonstatchanges = []
opponentstatchanges = []
#define items/bag
bag = {}
shop = {"Max Potion":{"Cost": 2500},
"Full Restore":{"Cost": 3000},
"Full Heal":{"Cost":600},
"Revive":{"Cost":1500}}
#define starter
starter = input("Which starter do you want? Bulbasaur, Charmander, or Squirtle?\n")
starter = starter.title()
t = 5
while t == 5:
    if starter == 'Bulbasaur':
        rival['Pidgeot']=rivalpokemon['Pidgeot']
        rival['Alakazam']=rivalpokemon['Alakazam']
        rival['Rhydon']=rivalpokemon['Rhydon']
        rival['Exeggutor']=rivalpokemon['Exeggutor']
        rival['Gyarados']=rivalpokemon['Gyarados']
        rival['Charizard']=rivalpokemon['Charizard']
        break
    elif starter == 'Charmander':
        rival['Pidgeot']=rivalpokemon['Pidgeot']
        rival['Alakazam']=rivalpokemon['Alakazam']
        rival['Rhydon']=rivalpokemon['Rhydon']
        rival['Arcanine']=rivalpokemon['Arcanine']
        rival['Exeggutor']=rivalpokemon['Exeggutor']
        rival['Blastoise']=rivalpokemon['Blastoise']
        break
    elif starter == 'Squirtle':
        rival['Pidgeot']=rivalpokemon['Pidgeot']
        rival['Alakazam']=rivalpokemon['Alakazam']
        rival['Rhydon']=rivalpokemon['Rhydon']
        rival['Gyarados']=rivalpokemon['Gyarados']
        rival['Arcanine']=rivalpokemon['Arcanine']
        rival['Venusaur']=rivalpokemon['Venusaur']
        break
    else:
        print("That is not a valid starter")
        starter = input("Choose a starter.\n")
        starter=starter.title()
print("You found a cheat code so you skipped to the Elite Four instead of doing actual Pokemon stuff.")
#define ai teams
opponents = {rivalname:rival,
"Lorelei" : {"Dewgong":allpokemon["Dewgong"], "Cloyster":allpokemon["Cloyster"], "Slowbro":allpokemon["Slowbro"], "Jynx":allpokemon["Jynx"], "Lapras":allpokemon["Lapras"]},
"Bruno" : {"Onix":allpokemon["Onix1"], "Hitmonchan":allpokemon["Hitmonchan"], "Hitmonlee":allpokemon["Hitmonlee"], "Onix":allpokemon["Onix2"], "Machamp":allpokemon["Machamp"]},
"Agatha" : {"Gengar":allpokemon["Gengar1"], "Golbat":allpokemon["Golbat"], "Haunter":allpokemon["Haunter"], "Arbok":allpokemon["Arbok"], "Gengar":allpokemon["Gengar2"]},
"Lance" : {"Gyarados":allpokemon["Gyarados"], "Dragonair":allpokemon["Dragonair1"], "Dragonair":allpokemon["Dragonair2"], "Aerodactyl":allpokemon["Aerodactyl"], "Dragonite":allpokemon["Dragonite"]}}
opponents2 = copy.deepcopy(opponents)
#def buying stuff
rr = 5
while rr == 5:
    qq = input("Do you want to buy anything from the shop before you battle?\n")
    qq = qq.title()
    if qq == "Yes":
        ss=2
        while ss != "Exit":
            print(shop)
            print("Money:", money)
            ss = input("What item would you like to buy or exit?\n")
            ss = ss.title()
            if ss == "Exit":
                break
            else:
                if ss in shop:
                    money = money - shop[ss]["Cost"]
                    if money<0:
                        print("You don't have enough money!")
                        money = money + shop[ss]["Cost"]
                    else:
                        print("You bought %s." %(ss))
                        if ss not in bag:
                            bag[ss]=1
                        else:
                            g = bag[ss]+1
                            bag[ss]=g
                        print(bag)
                else:
                    print("That is not a valid item")
    elif qq == "No":
        break
    else:
        print("Pick yes or no.")

#defining type chart
def firemove():
    global type
    if team2[next(iter(team2))]['type1'] == 'grass':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'grass':
        type = 4
    elif team2[next(iter(team2))]['type1'] == 'bug':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'ice':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'ice':
        type = 1
    elif team2[next(iter(team2))]['type1'] == 'dragon':
        type = .5
    elif team2[next(iter(team2))]['type1'] == 'rock':
        if team2[next(iter(team2))]['type2'] == 'water':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type1'] == 'water':
        if team2[next(iter(team2))]['type2'] == 'ice':
            type = 1
        else:
            type = .5
    elif team2[next(iter(team2))]['type2'] == 'rock':
        type = .5
    else:
        type = 1
def grassmove():
    global type
    if team2[next(iter(team2))]['type1'] == 'water':
        if team2[next(iter(team2))]['type2'] == 'poison':
            type = 1
        elif team2[next(iter(team2))]['type2'] == 'flying':
            type = 1
        elif team2[next(iter(team2))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif team2[next(iter(team2))]['type1'] == 'ground':
        if team2[next(iter(team2))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif team2[next(iter(team2))]['type2'] == 'ground':
        if team2[next(iter(team2))]['type2'] == 'poison':
            type = 1
        elif team2[next(iter(team2))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif team2[next(iter(team2))]['type1'] == 'rock':
        type = 1
    elif team2[next(iter(team2))]['type1'] == 'bug':
        if team2[next(iter(team2))]['type2'] == 'poison':
            type = .25
        elif team2[next(iter(team2))]['type'] == 'flying':
            type = .25
        elif team2[next(iter(team2))]['type2'] == 'grass':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type1'] == 'dragon':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type1'] == 'fire':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type2'] == 'flying':
        if team2[next(iter(team2))]['type1'] == 'poison':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type1'] == 'grass':
        if team2[next(iter(team2))]['type2'] == 'poison':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type1'] == 'poison':
        type = .5
    else:
        type = 1
def watermove():
    global type
    if team2[next(iter(team2))]['type1'] == 'fire':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'ground':
        if team2[next(iter(team2))]['type2'] == 'rock':
            type = 4
        else:
            type = 2
    elif team2[next(iter(team2))]['type2'] == 'ground':
        if team2[next(iter(team2))]['type1'] == 'rock':
            type = 4
        else:
            type = 2
    elif team2[next(iter(team2))]['type1'] == 'rock':
        if team2[next(iter(team2))]['type2'] == 'water':
            type = 1
        else:
            type = 2
    elif team2[next(iter(team2))]['type1'] == 'dragon':
        type = .5
    elif team2[next(iter(team2))]['type1'] == 'grass':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'grass':
        type = .5
    elif team2[next(iter(team2))]['type1'] == 'water':
        type = .5
    else:
        type = 1
def icemove():
    global type
    if team2[next(iter(team2))]['type1'] == 'dragon':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = 4
        else:
            type = 2
    elif team2[next(iter(team2))]['type2'] == 'flying':
        if team2[next(iter(team2))]['type1'] == 'fire':
            type = 1
        elif team2[next(iter(team2))]['type1'] == 'water':
            type = 1
        elif team2[next(iter(team2))]['type1'] == 'ice':
            type = 1
    elif team2[next(iter(team2))]['type1'] == 'grass':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'grass':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'ground':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'ground':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'ice':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = 1
        else:
            type = 0.5
    elif team2[next(iter(team2))]['type1'] == 'water':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = 1
        elif team2[next(iter(team2))]['type2'] == 'ice':
            type = 0.25
        else:
            type = 0.5
    elif team2[next(iter(team2))]['type2'] == 'water':
        type = 0.5
    elif team2[next(iter(team2))]['type1'] == 'fire':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = 1
        else:
            type = 0.5
    else:
        type = 1
def groundmove():
    global type
    if team2[next(iter(team2))]['type2'] == 'flying':
        type = 0
    elif team2[next(iter(team2))]['type1'] == 'electric':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'fire':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'poison':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'poison':
        if team2[next(iter(team2))]['type1'] == 'bug':
            type = 1
        elif team2[next(iter(team2))]['type1'] == 'grass':
            type = 1
    elif team2[next(iter(team2))]['type1'] == 'rock':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'rock':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'bug':
        if team2[next(iter(team2))]['type2'] == 'grass':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type1'] == 'grass':
        type = .5
    else:
        type = 1
def electricmove():
    global type
    if team2[next(iter(team2))]['type1'] == 'ground':
        type = 0
    elif team2[next(iter(team2))]['type1'] == 'water':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = 4
        else:
            type = 2
    elif team2[next(iter(team2))]['type2'] == 'water':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'flying':
        if team2[next(iter(team2))]['type1'] == 'electric':
            type = 1
        elif team2[next(iter(team2))]['type1'] == 'dragon':
            type = 1
        else:
            type = 2
    elif team2[next(iter(team2))]['type1'] == 'dragon':
        type = .5
    elif team2[next(iter(team2))]['type1'] == 'electric':
        type = .5
    elif team2[next(iter(team2))]['type1'] == 'grass':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'grass':
        type = .5
    else:
        type = 1
def flyingmove():
    global type
    if team2[next(iter(team2))]['type1'] == 'bug':
        if team2[next(iter(team2))]['type2'] == 'grass':
            type = 4
        else:
            type = 2
    elif team2[next(iter(team2))]['type2'] == 'grass':
        type = 4
    elif team2[next(iter(team2))]['type1'] == 'fighting':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'fighting':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'electric':
        type = .5
    elif team2[next(iter(team2))]['type1'] == 'rock':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'rock':
        type = .5
    else:
        type = 1
def ghostmove():
    global type
    if team2[next(iter(team2))]['type1'] == 'normal':
        type = 0
    elif team2[next(iter(team2))]['type1'] == 'ghost':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'psychic':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'psychic':
        type = 2
    else:
        type = 1
def rockmove():
    global type
    if team2[next(iter(team2))]['type1'] == 'fire':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = 4
        else:
            type = 2
    elif team2[next(iter(team2))]['type2'] == 'flying':
        if team2[next(iter(team2))]['type1'] == 'bug':
            type = 4
        elif team2[next(iter(team2))]['type1'] == 'ice':
            type = 4
        else:
            type = 2
    elif team2[next(iter(team2))]['type1'] == 'bug':
        type  = 2
    elif team2[next(iter(team2))]['type1'] == 'ice':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'ice':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'ground':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'ground':
        type = .5
    elif team2[next(iter(team2))]['type1'] == 'fighting':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'fighting':
        type = .5
    else:
        type = 1
def poisonmove():
    global type
    if team2[next(iter(team2))]['type1'] == 'grass':
        if team2[next(iter(team2))]['type1'] == 'poison':
            type = 1
        else:
            type = 2
    elif team2[next(iter(team2))]['type2'] == 'grass':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'ghost':
        type = .25
    elif team2[next(iter(team2))]['type1'] == 'ground':
        if team2[next(iter(team2))]['type2'] == 'rock':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type2'] == 'ground':
        if team2[next(iter(team2))]['type1'] == 'rock':
            type = .25
        elif team2[next(iter(team2))]['type1'] == 'poison':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type1'] == 'rock':
        type = .5
    elif team2[next(iter(team2))]['type1'] == 'poison':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'poison':
        type = .5
    else:
        type = 1
def psychicmove():
    global type
    if team2[next(iter(team2))]['type1'] == 'fighting':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'fighting':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'poison':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'poison':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'psychic':
        type =.5
    elif team2[next(iter(team2))]['type2'] == 'psychic':
        type = .5
    else:
        type = 1
def bugmove():
    global type
    if team2[next(iter(team2))]['type1'] == 'grass':
        if team2[next(iter(team2))]['type1'] == 'poison':
            type = 1
        else:
            type = 2
    elif team2[next(iter(team2))]['type2'] == 'grass':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'psychic':
        type = 2
    elif team2[next(iter(team2))]['type2'] == 'psychic':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'fighting':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'fighting':
        type = .5
    elif team2[next(iter(team2))]['type1'] == 'fire':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type1'] == 'ghost':
        type = .25
    elif team2[next(iter(team2))]['type1'] == 'poison':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type2'] == 'poison':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'flying':
        type = .5
    else:
        type = 1
def fightingmove():
    global type
    if team2[next(iter(team2))]['type1'] == 'ghost':
        type = 0
    elif team2[next(iter(team2))]['type1'] == 'rock':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = 1
        else:
            type = 2
    elif team2[next(iter(team2))]['type2'] == 'rock':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'ice':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = 1
        elif team2[next(iter(team2))]['type2'] == 'psychic':
            type = 1
        else:
            type = 2
    elif team2[next(iter(team2))]['type2'] == 'ice':
        type = 2
    elif team2[next(iter(team2))]['type1'] == 'normal':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = 1
        else:
            type = 2
    elif team2[next(iter(team2))]['type1'] == 'bug':
        if team2[next(iter(team2))]['type2'] == 'flying':
            type = .25
        elif team2[next(iter(team2))]['type2'] == 'poison':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type1'] == 'psychic':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'psychic':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'flying':
        if team2[next(iter(team2))]['type1'] == 'poison':
            type = .25
        else:
            type = .5
    elif team2[next(iter(team2))]['type1'] == 'poison':
        type = .25
    elif team2[next(iter(team2))]['type2'] == 'poison':
        type = .5
    else:
        type = 1
def normalmove():
    global type
    if team2[next(iter(team2))]['type1'] == 'ghost':
        type = 0
    elif team2[next(iter(team2))]['type1'] == 'rock':
        type = .5
    elif team2[next(iter(team2))]['type2'] == 'rock':
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
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'ice':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = 1
        else:
            type = 0.5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'water':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = 1
        elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'ice':
            type = 0.25
        else:
            type = 0.5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'water':
        type = 0.5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'fire':
        if opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'flying':
            type = 1
        else:
            type = 0.5
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
def psychicmoveopponent(opponent):
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
def bugmoveopponent(opponent):
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
def fightingmoveopponent(opponent):
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
    elif opponents[opponent][next(iter(opponents[opponent]))]['type1'] == 'psychic':
        type = .5
    elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == 'psychic':
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

#define status moves
def userstatusmove(move,opponent):
    print(next(iter(team2)), "used", move)
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
            print('The defense of', next(iter(team2)), 'cannot be raised any higher.')
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
            print('The defense of', next(iter(team2)), 'cannot be raised any higher.')
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
            print('The attack of', next(iter(team2)), 'was raised.')
        elif pokemonstatchanges.count('lowerattackby1')>1:
            pokemonstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(team2)), 'was raised.')
        elif pokemonstatchanges.count('raiseattackby1')==6:
            print('The attack of', next(iter(team2)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raiseattackby1')
            print('The attack of', next(iter(team2)), 'was raised.')
    elif allmoves[move]['effect']=='raiseattackby2':
        if pokemonstatchanges.count('lowerattackby1')==1:
            pokemonstatchanges.remove('lowerattackby1')
            pokemonstatchanges.append('raiseattackby1')
            print('The attack of', next(iter(team2)), 'was sharply raised.')
        elif pokemonstatchanges.count('lowerattackby1')>1:
            pokemonstatchanges.remove('lowerattackby1')
            pokemonstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(team2)), 'was sharply raised.')
        elif pokemonstatchanges.count('raiseattackby1')==6:
            print('The attack of', next(iter(team2)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raiseattackby1')
            pokemonstatchanges.append('raiseattackby1')
            print('The attack of', next(iter(team2)), 'was sharply raised.')
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
            print('The speed of', next(iter(team2)), 'was raised.')
        elif pokemonstatchanges.count('lowerspeedby1')>1:
            pokemonstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(team2)), 'was raised.')
        elif pokemonstatchanges.count('raisespeedby1')==6:
            print('The speed of', next(iter(team2)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespeedby1')
            print('The speed of', next(iter(team2)), 'was raised.')
    elif allmoves[move]['effect']=='raisespeedby2':
        if pokemonstatchanges.count('lowerspeedby1')==1:
            pokemonstatchanges.remove('lowerspeedby1')
            pokemonstatchanges.append('raisespeedby1')
            print('The speed of', next(iter(team2)), 'was sharply raised.')
        elif pokemonstatchanges.count('lowerspeedby1')>1:
            pokemonstatchanges.remove('lowerspeedby1')
            pokemonstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(team2)), 'was sharply raised.')
        elif pokemonstatchanges.count('raisespeedby1')==6:
            print('The speed of', next(iter(team2)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespeedby1')
            pokemonstatchanges.append('raisespeedby1')
            print('The speed of', next(iter(team2)), 'was sharply raised.')
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
            print('The special attack of', next(iter(team2)), 'was raised.')
        elif pokemonstatchanges.count('lowerspecialattackby1')>1:
            pokemonstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(team2)), 'was raised.')
        elif pokemonstatchanges.count('raisespecialattackby1')==6:
            print('The special attack of', next(iter(team2)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespecialattackby1')
            print('The special attack of', next(iter(team2)), 'was raised.')
    elif allmoves[move]['effect']=='raisespecialattackby2':
        if pokemonstatchanges.count('lowerspecialattackby1')==1:
            pokemonstatchanges.remove('lowerspecialattackby1')
            pokemonstatchanges.append('raisespecialattackby1')
            print('The special attack of', next(iter(team2)), 'was sharply raised.')
        elif pokemonstatchanges.count('lowerspecialattackby1')>1:
            pokemonstatchanges.remove('lowerspecialattackby1')
            pokemonstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(team2)), 'was sharply raised.')
        elif pokemonstatchanges.count('raisespecialattackby1')==6:
            print('The special attack of', next(iter(team2)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespecialattackby1')
            pokemonstatchanges.append('raisespecialattackby1')
            print('The special attack of', next(iter(team2)), 'was sharply raised.')
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
            print('The special defense of', next(iter(team2)), 'was raised.')
        elif pokemonstatchanges.count('lowerspecialdefenseby1')>1:
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team2)), 'was raised.')
        elif pokemonstatchanges.count('raisespecialdefenseby1')==6:
            print('The special defense of', next(iter(team2)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespecialdefenseby1')
            print('The special defense of', next(iter(team2)), 'was raised.')
    elif allmoves[move]['effect']=='raisespecialdefenseby2':
        if pokemonstatchanges.count('lowerspecialdefenseby1')==1:
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            pokemonstatchanges.append('raisespecialdefenseby1')
            print('The special defense of', next(iter(team2)), 'was sharply raised.')
        elif pokemonstatchanges.count('lowerspecialdefenseby1')>1:
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team2)), 'was sharply raised.')
        elif pokemonstatchanges.count('raisespecialdefenseby1')==6:
            print('The special defense of', next(iter(team2)), 'cannot be raised any higher.')
        else:
            pokemonstatchanges.append('raisespecialdefenseby1')
            pokemonstatchanges.append('raisespecialdefenseby1')
            print('The special defense of', next(iter(team2)), 'was sharply raised.')

def opponentstatusmove(opponent, opponentmove):
    print(next(iter(opponents[opponent])), 'used', opponentmove)
    if allmoves[opponentmove]['effect']=='lowerdefenseby1':
        if pokemonstatchanges.count('raisedefenseby1')==1:
            pokemonstatchanges.remove('raisedefenseby1')
            print('The defense of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('raisedefenseby1')>1:
            pokemonstatchanges.remove('lowerdefenseby1')
            print('The defense of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('lowerdefenseby1')==6:
            print('The defense of', next(iter(team2)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerdefenseby1')
            print('The defense of', next(iter(team2)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerdefenseby2':
        if pokemonstatchanges.count('raisedefenseby1')==1:
            pokemonstatchanges.remove('raisedefenseby1')
            pokemonstatchanges.append('lowerdefenseby1')
            print('The defense of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raisedefenseby1')>1:
            pokemonstatchanges.remove('raisedefenseby1')
            pokemonstatchanges.remove('raisedefenseby1')
            print('The defense of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('lowerdefenseby1')==6:
            print('The defense of', next(iter(team2)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerdefenseby1')
            pokemonstatchanges.append('lowerdefenseby1')
            print('The defense of', next(iter(team2)), 'was sharply lowered.')
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
            print('The attack of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('raiseattackby1')>1:
            pokemonstatchanges.remove('lowerattackby1')
            print('The attack of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('lowerattackby1')==6:
            print('The attack of', next(iter(team2)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerattackby1')
            print('The attack of', next(iter(team2)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerattackby2':
        if pokemonstatchanges.count('raiseattackby1')==1:
            pokemonstatchanges.remove('raiseattackby1')
            pokemonstatchanges.append('lowerattackby1')
            print('The attack of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raiseattackby1')>1:
            pokemonstatchanges.remove('raiseattackby1')
            pokemonstatchanges.remove('raiseattackby1')
            print('The attack of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('lowerattackby1')==6:
            print('The attack of', next(iter(team2)), 'cannot be lowered any further')
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
            print('The attack of', next(iter(team2)), 'was sharply raised.')
    elif allmoves[opponentmove]['effect']=='lowerspeedby1':
        if pokemonstatchanges.count('raisespeedby1')==1:
            pokemonstatchanges.remove('raisespeedby1')
            print('The speed of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('raisespeedby1')>1:
            opponentstatchanges.remove('lowerspeedby1')
            print('The speed of', next(iter(team2)), 'was lowered.')
        elif opponentstatchanges.count('lowerspeedby1')==6:
            print('The speed of', next(iter(team2)), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerspeedby1')
            print('The speed of', next(iter(team2)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerspeedby2':
        if pokemonstatchanges.count('raisespeedby1')==1:
            pokemonstatchanges.remove('raisespeedby1')
            opponentstatchanges.append('lowerspeedby1')
            print('The speed of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raisespeedby1')>1:
            pokemonstatchanges.remove('raisespeedby1')
            pokemonstatchanges.remove('raisespeedby1')
            print('The speed of', next(iter(team2)), 'was sharply lowered.')
        elif opponentstatchanges.count('lowerspeedby1')==6:
            print('The speed of', next(iter(team2)), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerspeedby1')
            opponentstatchanges.append('lowerspeedby1')
            print('The speed of', next(iter(team2)), 'was sharply lowered.')
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
            print('The special attack of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('raisespecialattackby1')>1:
            pokemonstatchanges.remove('lowerspecialattackby1')
            print('The special attack of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('lowerspecialattackby1')==6:
            print('The special attack of', next(iter(team2)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerspecialattackby1')
            print('The special attack of', next(iter(team2)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerspecialattackby2':
        if pokemonstatchanges.count('raisespecialattackby1')==1:
            pokemonstatchanges.remove('raisespecialattackby1')
            pokemonstatchanges.append('lowerspecialattackby1')
            print('The special attack of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raisespecialattackby1')>1:
            pokemonstatchanges.remove('raisespecialattackby1')
            pokemonstatchanges.remove('raisespecialattackby1')
            print('The special attack of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('lowerspecialattackby1')==6:
            print('The special attack of', next(iter(team2)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerspecialattackby1')
            pokemonstatchanges.append('lowerspecialattackby1')
            print('The special attack of', next(iter(team2)), 'was sharply lowered.')
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
            print('The special defense of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('raisespecialdefenseby1')>1:
            pokemonstatchanges.remove('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('lowerspecialdefenseby1')==6:
            print('The special defense of', next(iter(team2)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team2)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerspecialdefenseby2':
        if pokemonstatchanges.count('raisespecialdefenseby1')==1:
            pokemonstatchanges.remove('raisespecialdefenseby1')
            pokemonstatchanges.append('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raisespecialdefenseby1')>1:
            pokemonstatchanges.remove('raisespecialdefenseby1')
            pokemonstatchanges.remove('raisespecialdefenseby1')
            print('The special defense of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('lowerspecialdefenseby1')==6:
            print('The special defense of', next(iter(team2)), 'cannot be lowered any further')
        else:
            pokemonstatchanges.append('lowerspecialdefenseby1')
            pokemonstatchanges.append('lowerspecialdefenseby1')
            print('The special defense of', next(iter(team2)), 'was sharply lowered.')
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
    elif allmoves[opponentmove]['effect']=='lowerevasionby1':
        if pokemonstatchanges.count('raiseevasionby1')==1:
            pokemonstatchanges.remove('raiseevasionby1')
            print('The evasion of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('raiseevasionby1')>1:
            opponentstatchanges.remove('lowerevasionby1')
            print('The evasion of', next(iter(team2)), 'was lowered.')
        elif opponentstatchanges.count('lowerevasionby1')==6:
            print('The evasion of', next(iter(team2)), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerevasionby1')
            print('The evasion of', next(iter(team2)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='lowerevasionby2':
        if pokemonstatchanges.count('raiseevasionby1')==1:
            pokemonstatchanges.remove('raiseevasionby1')
            opponentstatchanges.append('lowerevasionby1')
            print('The evasion of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raiseevasionby1')>1:
            pokemonstatchanges.remove('raiseevasionby1')
            pokemonstatchanges.remove('raiseevasionby1')
            print('The evasion of', next(iter(team2)), 'was sharply lowered.')
        elif opponentstatchanges.count('lowerevasionby1')==6:
            print('The evasion of', next(iter(team2)), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('lowerevasionby1')
            opponentstatchanges.append('lowerevasionby1')
            print('The evasion of', next(iter(team2)), 'was sharply lowered.')
    elif allmoves[opponentmove]['effect']=='raiseevasionby1':
        if opponentstatchanges.count('lowerevasionby1')==1:
            pokemonstatchanges.remove('lowerevasionby1')
            print('The evasion of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('lowerevasionby1')>1:
            opponentstatchanges.remove('lowerevasionby1')
            print('The evasion of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('raiseevasionby1')==6:
            print('The evasion of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raiseevasionby1')
            print('The evasion of', next(iter(opponents[opponent])), 'was raised.')
    elif allmoves[opponentmove]['effect']=='raiseevasionby2':
        if opponentstatchanges.count('lowerevasionby1')==1:
            opponentstatchanges.remove('lowerevasionby1')
            opponentstatchanges.append('raiseevasionby1')
            print('The evasion of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('lowerevasionby1')>1:
            opponentstatchanges.remove('lowerevasionby1')
            opponentstatchanges.remove('lowerevasionby1')
            print('The evasion of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('raiseevasionby1')==6:
            print('The evasion of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raiseevasionby1')
            opponentstatchanges.append('raiseevasionby1')
            print('The evasion of', next(iter(opponents[opponent])), 'was sharply raised.')
    elif allmoves[opponentmove]['effect']=='loweraccuracyby1':
        if pokemonstatchanges.count('raiseaccuracyby1')==1:
            pokemonstatchanges.remove('raiseaccuracyby1')
            print('The accuracy of', next(iter(team2)), 'was lowered.')
        elif pokemonstatchanges.count('raiseaccuracyby1')>1:
            opponentstatchanges.remove('loweraccuracyby1')
            print('The accuracy of', next(iter(team2)), 'was lowered.')
        elif opponentstatchanges.count('loweraccuracyby1')==6:
            print('The accuracy of', next(iter(team2)), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('loweraccuracyby1')
            print('The accuracy of', next(iter(team2)), 'was lowered.')
    elif allmoves[opponentmove]['effect']=='loweraccuracyby2':
        if pokemonstatchanges.count('raiseaccuracyby1')==1:
            pokemonstatchanges.remove('raiseaccuracyby1')
            opponentstatchanges.append('loweraccuracyby1')
            print('The accuracy of', next(iter(team2)), 'was sharply lowered.')
        elif pokemonstatchanges.count('raiseaccuracyby1')>1:
            pokemonstatchanges.remove('raiseaccuracyby1')
            pokemonstatchanges.remove('raiseaccuracyby1')
            print('The accuracy of', next(iter(team2)), 'was sharply lowered.')
        elif opponentstatchanges.count('loweraccuracyby1')==6:
            print('The accuracy of', next(iter(team2)), 'cannot be lowered any further')
        else:
            opponentstatchanges.append('loweraccuracyby1')
            opponentstatchanges.append('loweraccuracyby1')
            print('The accuracy of', next(iter(team2)), 'was sharply lowered.')
    elif allmoves[opponentmove]['effect']=='raiseaccuracyby1':
        if opponentstatchanges.count('loweraccuracyby1')==1:
            pokemonstatchanges.remove('loweraccuracyby1')
            print('The accuracy of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('loweraccuracyby1')>1:
            opponentstatchanges.remove('loweraccuracyby1')
            print('The accuracy of', next(iter(opponents[opponent])), 'was raised.')
        elif opponentstatchanges.count('raiseaccuracyby1')==6:
            print('The accuracy of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raiseaccuracyby1')
            print('The accuracy of', next(iter(opponents[opponent])), 'was raised.')
    elif allmoves[opponentmove]['effect']=='raiseaccuracyby2':
        if opponentstatchanges.count('loweraccuracyby1')==1:
            opponentstatchanges.remove('loweraccuracyby1')
            opponentstatchanges.append('raiseaccuracyby1')
            print('The accuracy of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('loweraccuracyby1')>1:
            opponentstatchanges.remove('loweraccuracyby1')
            opponentstatchanges.remove('loweraccuracyby1')
            print('The accuracy of', next(iter(opponents[opponent])), 'was sharply raised.')
        elif opponentstatchanges.count('raiseaccuracyby1')==6:
            print('The accuracy of', next(iter(opponents[opponent])), 'cannot be raised any higher.')
        else:
            opponentstatchanges.append('raiseaccuracyby1')
            opponentstatchanges.append('raiseaccuracyby1')
            print('The accuracy of', next(iter(opponents[opponent])), 'was sharply raised.')

#define attacking moves
def userdamage(opponent, move):
    basea=allmoves[move]['accuracy']
    basea=allmoves[move]['accuracy']
    if pokemonstatchanges.count('raiseaccuracyby1') >= 1:
        uu = pokemonstatchanges.count('raiseaccuracyby1')
        if uu == 1:
            acc=1.5
        elif uu == 2:
            acc=2
        elif uu == 3:
            acc=2.5
        elif uu == 4:
            acc=3
        elif uu == 5:
            acc=3.5
        else:
            acc=4
    elif pokemonstatchanges.count('loweraccuracyby1') >= 1:
        uu = pokemonstatchanges.count('loweraccuracyby1')
        if uu == 1:
            acc=2/3
        elif uu == 2:
            acc=.5
        elif uu == 3:
            acc=.4
        elif uu == 4:
            acc=1/3
        elif uu == 5:
            acc=2/7
        else:
            acc=.25
    else:
        acc=1
    if opponentstatchanges.count('raiseevasionby1') >= 1:
        xx = opponentstatchanges.count('raiseevasionby1')
        if xx == 1:
            evas=1.5
        elif xx == 2:
            evas=2
        elif xx == 3:
            evas=2.5
        elif xx == 4:
            evas=3
        elif xx == 5:
            evas=3.5
        else:
            evas=4
    elif opponentstatchanges.count('lowerevasionby1') >= 1:
        uu = opponentstatchanges.count('lowerevasionby1')
        if uu == 1:
            acc=2/3
        elif uu == 2:
            acc=.5
        elif uu == 3:
            acc=.4
        elif uu == 4:
            acc=1/3
        elif uu == 5:
            acc=2/7
        else:
            acc=.25
    else:
        evas=1
    p=basea*(acc/evas)
    moveaccuracy = random.randint(1, 100)
    if moveaccuracy>p:
        print("%s used %s, but it missed!"%(next(iter(team2)), move))
    else:
        level = team2[next(iter(team2))]['level']
        power = allmoves[move]['bp']
        if allmoves[move]['category']=='physical':
            if pokemonstatchanges.count('raiseattackby1') > 1:
                t = pokemonstatchanges.count('raiseattackby1')
                c = team2[next(iter(team2))]['attack']
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
                    b=4
                a=b*c
            elif pokemonstatchanges.count('lowerattackby1') > 1:
                t = pokemonstatchanges.count('lowerattackby1')
                c = team2[next(iter(team2))]['attack']
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
                a = team2[next(iter(team2))]['attack']
        else:
            if pokemonstatchanges.count('raisespecialattackby1') > 1:
                t = pokemonstatchanges.count('raisespecialattackby1')
                c = team2[next(iter(team2))]['special attack']
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
                    b=4
                a=b*c
            elif pokemonstatchanges.count('lowerspecialattackby1') > 1:
                t = pokemonstatchanges.count('lowerspecialattackby1')
                c = team2[next(iter(team2))]['special attack']
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
                a = team2[next(iter(team2))]['special attack']
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
                    b=4
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
                    b=4
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
        if team2[next(iter(team2))]['type1'] == allmoves[move]['type']:
            stab = 1.5
        elif team2[next(iter(team2))]['type2'] == allmoves[move]['type']:
            stab = 1.5
        else:
            stab = 1
        if team2[next(iter(team2))]['status']=='burn':
                    burn = .5
        else:
            burn = 1
        modifier =  crit*rand*stab*type*burn
        global damage
        damage = ((((((2*level)/5)+2)*power*(a/d))/50)+2)*modifier
        print(next(iter(team2)), 'used', move)
        if type>1:
            print("It's super effective!")
        elif type==0:
            print("It had no effect!")
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
    basea=allmoves[opponentmove]['accuracy']
    if opponentstatchanges.count('raiseaccuracyby1') >= 1:
        uu = opponentstatchanges.count('raiseaccuracyby1')
        if uu == 1:
            acc=1.5
        elif uu == 2:
            acc=2
        elif uu == 3:
            acc=2.5
        elif uu == 4:
            acc=3
        elif uu == 5:
            acc=3.5
        else:
            acc=4
    elif opponentstatchanges.count('loweraccuracyby1') >= 1:
        uu = opponentstatchanges.count('loweraccuracyby1')
        if uu == 1:
            acc=2/3
        elif uu == 2:
            acc=.5
        elif uu == 3:
            acc=.4
        elif uu == 4:
            acc=1/3
        elif uu == 5:
            acc=2/7
        else:
            acc=.25
    else:
        acc=1
    if pokemonstatchanges.count('raiseevasionby1') >= 1:
        xx = pokemonstatchanges.count('raiseevasionby1')
        if xx == 1:
            evas=1.5
        elif xx == 2:
            evas=2
        elif xx == 3:
            evas=2.5
        elif xx == 4:
            evas=3
        elif xx == 5:
            evas=3.5
        else:
            evas=4
    elif pokemonstatchanges.count('lowerevasionby1')>=1:
        uu = pokemonstatchanges.count('lowerevasionby1')
        if uu == 1:
            acc=2/3
        elif uu == 2:
            acc=.5
        elif uu == 3:
            acc=.4
        elif uu == 4:
            acc=1/3
        elif uu == 5:
            acc=2/7
        else:
            acc=.25
    else:
        evas=1
    p=basea*(acc/evas)
    moveaccuracy = random.randint(1, 100)
    if moveaccuracy>p:
        print("%s used %s, but it missed!"%(next(iter(opponents[opponent])), opponentmove))
    else:
        level = opponents[opponent][next(iter(opponents[opponent]))]['level']
        power = allmoves[opponentmove]['bp']
        if allmoves[opponentmove]['category']=='physical':
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
                    b=4
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
        if allmoves[opponentmove]['category']=='physical':
            if pokemonstatchanges.count('raisedefenseby1') > 1:
                t = pokemonstatchanges.count('raisedefenseby1')
                c = team2[next(iter(team2))]['defense']
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
                    b=4
                d=b*c
            elif pokemonstatchanges.count('lowerdefenseby1') > 1:
                t = pokemonstatchanges.count('lowerdefenseby1')
                c = team2[next(iter(team2))]['defense']
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
                d = team2[next(iter(team2))]['defense']
        else:
            if pokemonstatchanges.count('raisespecialdefenseby1') > 1:
                t = pokemonstatchanges.count('raisespecialdefenseby1')
                c = team2[next(iter(team2))]['special defense']
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
                    b=4
                d=b*c
            elif pokemonstatchanges.count('lowerspecialdefenseby1') > 1:
                t = pokemonstatchanges.count('lowerspecialdefenseby1')
                c = team2[next(iter(team2))]['special defense']
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
                d = team2[next(iter(team2))]['special defense']
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
        if opponents[opponent][next(iter(opponents[opponent]))]['type1'] == allmoves[opponentmove]['type']:
            stab = 1.5
        elif opponents[opponent][next(iter(opponents[opponent]))]['type2'] == allmoves[opponentmove]['type']:
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
        elif type==0:
            print("It had no effect!")
        elif type<1:
            print("It's not very effective!")
        o = int(damage)
        if team2[next(iter(team2))]['hp']-o<0:
            o=team2[next(iter(team2))]['hp']
        if o>1:
            print(next(iter([next(iter(team2))])), "lost", o, "hit points!")
            x = team2[next(iter(team2))]['hp']-o
            team2[next(iter(team2))]['hp'] = x
        else:
            print(next(iter([next(iter(team2))])), "lost", o, "hit point!")
            x = team2[next(iter(team2))]['hp']-o
            team2[next(iter(team2))]['hp'] = x
        if allmoves[opponentmove]['effect']=='10%burn':
            h = random.randint(1,10)
            h=1
            if h == 1:
                if team2[next(iter(team2))]=='none':
                    print(next(iter(team2)), "was burned!")
                    team2[next(iter(team2))]='burn'

#define switching
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
        team2.clear()
        team2[q]=a
        team2[b]=c
        team2[d]=e
        team2[f]=g
        team2[h]=i
        team2[j]=k
    global v
    v = 7

global team2
team2 = copy.deepcopy(team)
global party
party = [list(team2.keys())[0], list(team2.keys())[1], list(team2.keys())[2],list(team2.keys())[3],list(team2.keys())[4], list(team2.keys())[5]]
party2 = copy.deepcopy(party)
global party3
party3=copy.deepcopy(party2)

#define battling
def battle(opponent, cash):
    print(opponent, "has challenged you to battle!")
    print(opponent, "sent out %s!" %(next(iter(opponents[opponent]))))
    print(player.name, "sent out %s!" %(next(iter(team2))))
    while len(opponents[opponent])!=0:
        g = input("Battle\nBag\nSwitch\nRun\n")
        g = g.title()
        if g == "Bag":
            print(bag)
            global q
            global w
            global money
            item = input("Which item would you like to use?\n")
            item = item.title()
            v=1
            while v == 1:
                if item == "Max Potion":
                    print(party)
                    aa=input("Which Pokemon would you like to heal up?\n")
                    aa=aa.title()
                    u=1
                    while u==1:
                        if team2[aa]['hp']==0:
                            print(aa, "has already fainted!")
                        elif team2[aa]['hp']==team[aa]['hp']:
                            print("It will have no effect!")
                        elif aa not in team2:
                            print(aa, "is not a Pokemon in your party!")
                        else:
                            bb=team[aa]['hp']-team2[aa]['hp']
                            print(aa, "was healed up by",bb, "HP")
                            g = bag[item]-1
                            bag[item]=g
                            if g == 0:
                                del bag[item]
                            team2[aa]['hp']=team[aa]['hp']
                            u=2
                            m = random.randint(1,4)
                            while opponents[opponent][next(iter(opponents[opponent]))][m]=='none':
                                m = random.randint(1,4)
                            opponentmove=opponents[opponent][next(iter(opponents[opponent]))][m]
                            if allmoves[opponentmove]['category']== 'status':
                                opponentstatusmove(opponent,opponentmove)
                            else:
                                opponentdamage(opponent,opponentmove)
                                if team2[next(iter(team2))]['hp']<=0:
                                    print(next(iter(team2)), "fainted!")
                                    pokemonstatchanges.clear()
                                    w=list(team2.keys()).index(next(iter(team2)))
                                    del party3[w]
                                    if len(party3)==0:
                                        print("You blacked out")
                                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                        money = money/2
                                        break
                                    else:
                                        print(party)
                                        v = 5
                                        while v == 5:
                                            q=input("Which Pokemon would you like to send out?\n")
                                            q=q.title()
                                            if q not in team2:
                                                print("That is not a valid Pokemon")
                                            elif team2[q]['hp']<=0:
                                                print(q, "has no strength to battle.")
                                            else:
                                                w = list(team2.keys()).index(q)
                                                shifting()
                                                v=7
                        u=2
                    v=2
                elif item == "Revive":
                    print(party)
                    aa=input("Which Pokemon would you like to heal up?\n")
                    aa=aa.title()
                    u=1
                    while u==1:
                        if team2[aa]['hp']==0:
                            print(aa, "was revived!")
                            g = bag[item]-1
                            bag[item]=g
                            if g == 0:
                                del bag[item]
                            w=team[aa]['hp']/2
                            team2[aa]['hp']=int(w)
                            m = random.randint(1,4)
                            while opponents[opponent][next(iter(opponents[opponent]))][m]=='none':
                                m = random.randint(1,4)
                            opponentmove=opponents[opponent][next(iter(opponents[opponent]))][m]
                            if allmoves[opponentmove]['category']== 'status':
                                opponentstatusmove(opponent,opponentmove)
                            else:
                                opponentdamage(opponent,opponentmove)
                                if team2[next(iter(team2))]['hp']<=0:
                                    print(next(iter(team2)), "fainted!")
                                    pokemonstatchanges.clear()
                                    w=list(team2.keys()).index(next(iter(team2)))
                                    del party3[w]
                                    if len(party3)==0:
                                        print("You blacked out")
                                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                        money = money/2
                                        break
                                    else:
                                        print(party)
                                        v = 5
                                        while v == 5:
                                            q=input("Which Pokemon would you like to send out?\n")
                                            q=q.title()
                                            if q not in team2:
                                                print("That is not a valid Pokemon")
                                            elif team2[q]['hp']<=0:
                                                print(q, "has no strength to battle.")
                                            else:
                                                w = list(team2.keys()).index(q)
                                                shifting()
                                                v=7
                        elif team2[aa]['hp']==team[aa]['hp']:
                            print("It will have no effect!")
                        else:
                            print(aa, "is not a Pokemon in your party!")
                        u=2
                    v=2
                elif item == "Full Heal":
                    print(party)
                    aa=input("Which Pokemon would you like to heal up?\n")
                    aa=aa.title()
                    u=1
                    while u==1:
                        if team2[aa]['status']!='none':
                            print(aa, "was healed!")
                            g = bag[item]-1
                            bag[item]=g
                            if g == 0:
                                del bag[item]
                            team2[aa]['status']='none'
                            m = random.randint(1,4)
                            while opponents[opponent][next(iter(opponents[opponent]))][m]=='none':
                                m = random.randint(1,4)
                            opponentmove=opponents[opponent][next(iter(opponents[opponent]))][m]
                            if allmoves[opponentmove]['category']== 'status':
                                opponentstatusmove(opponent,opponentmove)
                            else:
                                opponentdamage(opponent,opponentmove)
                                if team2[next(iter(team2))]['hp']<=0:
                                    print(next(iter(team2)), "fainted!")
                                    pokemonstatchanges.clear()
                                    w=list(team2.keys()).index(next(iter(team2)))
                                    del party3[w]
                                    if len(party3)==0:
                                        print("You blacked out")
                                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                        money = money/2
                                        break
                                    else:
                                        print(party)
                                        v = 5
                                        while v == 5:
                                            q=input("Which Pokemon would you like to send out?\n")
                                            q=q.title()
                                            if q not in team2:
                                                print("That is not a valid Pokemon")
                                            elif team2[q]['hp']<=0:
                                                print(q, "has no strength to battle.")
                                            else:
                                                w = list(team2.keys()).index(q)
                                                shifting()
                                                v=7
                        elif team2[aa]['status']=='none':
                            print("It will have no effect!")
                        else:
                            print(aa, "is not a Pokemon in your party!")
                        u=2
                    v=2
                elif item == "Full Restore":
                    print(party)
                    aa=input("Which Pokemon would you like to heal up?\n")
                    aa=aa.title()
                    u=1
                    while u==1:
                        if team2[aa]['hp']!=team[aa]['hp']:
                            print(aa, "was healed!")
                            g = bag[item]-1
                            bag[item]=g
                            if g == 0:
                                del bag[item]
                            team2[aa]['status']='none'
                            team2[aa]['hp']=team[aa]['hp']
                            m = random.randint(1,4)
                            while opponents[opponent][next(iter(opponents[opponent]))][m]=='none':
                                m = random.randint(1,4)
                            opponentmove=opponents[opponent][next(iter(opponents[opponent]))][m]
                            if allmoves[opponentmove]['category']== 'status':
                                opponentstatusmove(opponent,opponentmove)
                            else:
                                opponentdamage(opponent,opponentmove)
                                if team2[next(iter(team2))]['hp']<=0:
                                    print(next(iter(team2)), "fainted!")
                                    pokemonstatchanges.clear()
                                    w=list(team2.keys()).index(next(iter(team2)))
                                    del party3[w]
                                    if len(party3)==0:
                                        print("You blacked out")
                                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                        money = money/2
                                        break
                                    else:
                                        print(party)
                                        v = 5
                                        while v == 5:
                                            q=input("Which Pokemon would you like to send out?\n")
                                            q=q.title()
                                            if q not in team2:
                                                print("That is not a valid Pokemon")
                                            elif team2[q]['hp']<=0:
                                                print(q, "has no strength to battle.")
                                            else:
                                                w = list(team2.keys()).index(q)
                                                shifting()
                                                v=7
                        elif team2[aa]['status']!='none':
                            print(aa, "was healed!")
                            g = bag[item]-1
                            bag[item]=g
                            if g == 0:
                                del bag[item]
                            while u==1:
                                if team2[aa]['hp']!=team[aa]['hp']:
                                    print(aa, "was healed!")
                                    team2[aa]['status']='none'
                                    team2[aa]['hp']==team[aa]['hp']
                                    m = random.randint(1,4)
                                    while opponents[opponent][next(iter(opponents[opponent]))][m]=='none':
                                        m = random.randint(1,4)
                                    opponentmove=opponents[opponent][next(iter(opponents[opponent]))][m]
                                    if allmoves[opponentmove]['category']== 'status':
                                        opponentstatusmove(opponent,opponentmove)
                                    else:
                                        opponentdamage(opponent,opponentmove)
                                        if team2[next(iter(team2))]['hp']<=0:
                                            print(next(iter(team2)), "fainted!")
                                            pokemonstatchanges.clear()
                                            w=list(team2.keys()).index(next(iter(team2)))
                                            del party3[w]
                                            if len(party3)==0:
                                                print("You blacked out")
                                                print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                                money = money/2
                                                break
                                            else:
                                                print(party)
                                                v = 5
                                                while v == 5:
                                                    q=input("Which Pokemon would you like to send out?\n")
                                                    q=q.title()
                                                    if q not in team2:
                                                        print("That is not a valid Pokemon")
                                                    elif team2[q]['hp']<=0:
                                                        print(q, "has no strength to battle.")
                                                    else:
                                                        w = list(team2.keys()).index(q)
                                                        shifting()
                                                        v=7
                                elif team2[aa]['hp']==team[aa]['hp']:
                                    print("It will have no effect!")
                                elif team2[aa]['status']=='none':
                                    print("It will have no effect!")
                                else:
                                    print(aa, "is not a Pokemon in your party!")
                        u=2
                    v=2
                elif item == "Back":
                    break
                else:
                    print("That is not an item in your bag.")
            if team2[next(iter(team2))]['status']=='burn':
                x=team2[next(iter(team2))]['hp']*0.0625
                x=int(x)
                if team2[next(iter(team2))]['hp']-x<0:
                    x=team2[next(iter(team2))]
                i = team2[next(iter(team2))]['hp']-x
                team2[next(iter(team2))]['hp']=i
                print(next(iter(team2)), "was hurt by the burn")
                if x==1:
                    print(next(iter(team2)), "lost", x, "hit point.")
                else:
                    print(next(iter(team2)), "lost", x, "hit points.")
                if team2[next(iter(team2))]['hp']<=0:
                    print(next(iter(team2)), "fainted!")
                    pokemonstatchanges.clear()
                    w=list(team2.keys()).index(next(iter(team2)))
                    del party3[w]
                    if len(party3)==0:
                        print("You blacked out")
                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                        money=money/2
                        break
                    else:
                        print(party)
                        v = 5
                        while v == 5:
                            q=input("Which Pokemon would you like to send out?\n")
                            q=q.title()
                            if q not in team2:
                                print("That is not a valid Pokemon")
                            elif team2[q]['hp']<=0:
                                print(q, "has no strength to battle.")
                            else:
                                w = list(team2.keys()).index(q)
                                shifting()
                                v=7
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
                    opponentstatchanges.clear()
                    del opponents[opponent][next(iter(opponents[opponent]))]
            print("Your %s: %s HP"%(next(iter(team2)), team2[next(iter(team2))]['hp']))
            print("%s's %s: %s HP"%(opponent, next(iter(opponents[opponent])), opponents[opponent][next(iter(opponents[opponent]))]['hp']))
        elif g == "Switch":
            print(party)
            v = 5
            while v == 5:
                q = input("Which would Pokemon would you like to send out?\n")
                q=q.title()
                if q == next(iter(team2)):
                    print(q, "is already on the field!")
                    q = input("Which Pokemon would you like to send out?\n")
                    q=q.title()
                elif q == "Back":
                    break
                elif q not in team2:
                    print("That is not a Pokemon on your team.")
                elif team2[q]['hp']<=0:
                    print(q, "has no strength to battle.")
                else:
                    print("Good job %s! Go %s!"%(next(iter(team2)), q))
                    w = list(team2.keys()).index(q)
                    shifting()
                    m = random.randint(1,4)
                    while opponents[opponent][next(iter(opponents[opponent]))][m]=='none':
                        m = random.randint(1,4)
                    opponentmove=opponents[opponent][next(iter(opponents[opponent]))][m]
                    if allmoves[opponentmove]['category']== 'status':
                        opponentstatusmove(opponent,opponentmove)
                        v=7
                    else:
                        opponentdamage(opponent,opponentmove)
                        if team2[next(iter(team2))]['hp']<=0:
                            print(next(iter(team2)), "fainted!")
                            pokemonstatchanges.clear()
                            w=list(team2.keys()).index(next(iter(team2)))
                            del party3[w]
                            if len(party3)==0:
                                print("You blacked out")
                                print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                money = money/2
                                break
                            else:
                                print(party)
                                v = 5
                                while v == 5:
                                    q=input("Which Pokemon would you like to send out?\n")
                                    q=q.title()
                                    if q not in team2:
                                        print("That is not a valid Pokemon")
                                    elif team2[q]['hp']<=0:
                                        print(q, "has no strength to battle.")
                                    else:
                                        w = list(team2.keys()).index(q)
                                        shifting()
                                        v=7
                        else:
                            v = 7
            if team2[next(iter(team2))]['status']=='burn':
                x=team2[next(iter(team2))]['hp']*0.0625
                x=int(x)
                if team2[next(iter(team2))]['hp']-x<0:
                    x=team2[next(iter(team2))]
                i = team2[next(iter(team2))]['hp']-x
                team2[next(iter(team2))]['hp']=i
                print(next(iter(team2)), "was hurt by the burn")
                if x==1:
                    print(next(iter(team2)), "lost", x, "hit point.")
                else:
                    print(next(iter(team2)), "lost", x, "hit points.")
                if team2[next(iter(team2))]['hp']<=0:
                    print(next(iter(team2)), "fainted!")
                    pokemonstatchanges.clear()
                    w=list(team2.keys()).index(next(iter(team2)))
                    del party3[w]
                    if len(party3)==0:
                        print("You blacked out")
                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                        money=money/2
                        break
                    else:
                        print(party)
                        v = 5
                        while v == 5:
                            q=input("Which Pokemon would you like to send out?\n")
                            q=q.title()
                            if q not in team2:
                                print("That is not a valid Pokemon")
                            elif team2[q]['hp']<=0:
                                print(q, "has no strength to battle.")
                            else:
                                w = list(team2.keys()).index(q)
                                shifting()
                                v=7
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
                    opponentstatchanges.clear()
                    del opponents[opponent][next(iter(opponents[opponent]))]
                    v = 7
            print("Your %s: %s HP"%(next(iter(team2)), team2[next(iter(team2))]['hp']))
            print("Opponent's %s: %s HP"%(next(iter(opponents[opponent])), opponents[opponent][next(iter(opponents[opponent]))]['hp']))
        elif g == "Battle":
            print(team2[next(iter(team2))][1],"\n",team2[next(iter(team2))][2],"\n",team2[next(iter(team2))][3],"\n",team2[next(iter(team2))][4])
            global move
            move =input("Which move would you like to use?\n")
            move=move.title()
            j = 5
            while j==5:
                if move == team2[next(iter(team2))][1]:
                    break
                elif move == team2[next(iter(team2))][2]:
                    break
                elif move == team2[next(iter(team2))][3]:
                    break
                elif move == team2[next(iter(team2))][4]:
                    break
                else:
                    print("That is not a valid move.")
                    move = input("Which move would you like to use?\n")
                    move=move.title()
            m = random.randint(1,4)
            while opponents[opponent][next(iter(opponents[opponent]))][m]=='none':
                m = random.randint(1,4)
            opponentmove=opponents[opponent][next(iter(opponents[opponent]))][m]
            if team2[next(iter(team2))]['speed']>opponents[opponent][next(iter(opponents[opponent]))]['speed']:
                if allmoves[move]['category']=='status':
                    userstatusmove(move, opponent)
                    if opponents[opponent][next(iter(opponents[opponent]))]['hp']>0:
                        if allmoves[opponentmove]['category']=='status':
                            opponentstatusmove(opponent,opponentmove)
                        else:
                            opponentdamage(opponent,opponentmove)
                            if team2[next(iter(team2))]['hp']<=0:
                                print(next(iter(team2)), "fainted!")
                                pokemonstatchanges.clear()
                                w=list(team2.keys()).index(next(iter(team2)))
                                del party3[w]
                                if len(party3)==0:
                                    print("You blacked out")
                                    print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                    money=money/2
                                    break
                                else:
                                    print(party)
                                    v = 5
                                    while v == 5:
                                        q=input("Which Pokemon would you like to send out?\n")
                                        q=q.title()
                                        if q not in team2:
                                            print("That is not a valid Pokemon")
                                        elif team2[q]['hp']<=0:
                                            print(q, "has no strength to battle.")
                                        else:
                                            w = list(team2.keys()).index(q)
                                            shifting()
                                            v=7
                else:
                    userdamage(opponent,move)
                    if opponents[opponent][next(iter(opponents[opponent]))]['hp']>0:
                        if allmoves[opponentmove]['category']=='status':
                            opponentstatusmove(opponent,opponentmove)
                        else:
                            opponentdamage(opponent,opponentmove)
                            if team2[next(iter(team2))]['hp']<=0:
                                print(next(iter(team2)), "fainted!")
                                pokemonstatchanges.clear()
                                w=list(team2.keys()).index(next(iter(team2)))
                                del party3[w]
                                if len(party3)==0:
                                    print("You blacked out")
                                    print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                    money=money/2
                                    break
                                else:
                                    print(party)
                                    v = 5
                                    while v == 5:
                                        q=input("Which Pokemon would you like to send out?\n")
                                        q=q.title()
                                        if q not in team2:
                                            print("That is not a valid Pokemon")
                                        elif team2[q]['hp']<=0:
                                            print(q, "has no strength to battle.")
                                        else:
                                            w = list(team2.keys()).index(q)
                                            shifting()
                                            v=7
                    else:
                        print(next(iter(opponents[opponent])), "fainted!")
                        opponentstatchanges.clear()
                        del opponents[opponent][next(iter(opponents[opponent]))]
            elif team2[next(iter(team2))]['speed']==opponents[opponent][next(iter(opponents[opponent]))]['speed']:
                speedtie=random.randint(1,2)
                if speedtie==1:
                    if allmoves[move]['category']=='status':
                        userstatusmove(move, opponent)
                        if opponents[opponent][next(iter(opponents[opponent]))]['hp']>0:
                            if allmoves[opponentmove]['category']=='status':
                                opponentstatusmove(opponent,opponentmove)
                            else:
                                opponentdamage(opponent,opponentmove)
                                if team2[next(iter(team2))]['hp']<=0:
                                    print(next(iter(team2)), "fainted!")
                                    pokemonstatchanges.clear()
                                    w=list(team2.keys()).index(next(iter(team2)))
                                    del party3[w]
                                    if len(party3)==0:
                                        print("You blacked out")
                                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                        money=money/2
                                        break
                                    else:
                                        print(party)
                                        v = 5
                                        while v == 5:
                                            q=input("Which Pokemon would you like to send out?\n")
                                            q=q.title()
                                            if q not in team2:
                                                print("That is not a valid Pokemon")
                                            elif team2[q]['hp']<=0:
                                                print(q, "has no strength to battle.")
                                            else:
                                                w = list(team2.keys()).index(q)
                                                shifting()
                                                v=7
                    else:
                        userdamage(opponent,move)
                        if opponents[opponent][next(iter(opponents[opponent]))]['hp']>0:
                            if allmoves[opponentmove]['category']=='status':
                                opponentstatusmove(opponent, opponentmove)
                            else:
                                opponentdamage(opponent,opponentmove)
                                if team2[next(iter(team2))]['hp']<=0:
                                    print(next(iter(team2)), "fainted!")
                                    pokemonstatchanges.clear()
                                    w=list(team2.keys()).index(next(iter(team2)))
                                    del party3[w]
                                    print(party3)
                                    if len(party3)==0:
                                        print("You blacked out")
                                        print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                        money=money/2
                                        break
                                    else:
                                        print(party)
                                        v = 5
                                        while v == 5:
                                            q=input("Which Pokemon would you like to send out?\n")
                                            q = q.title()
                                            if q not in team2:
                                                print("That is not a valid Pokemon")
                                            elif team2[q]['hp']<=0:
                                                print(q, "has no strength to battle.")
                                            else:
                                                w = list(team2.keys()).index(q)
                                                shifting()
                                                v=7
                        else:
                            print(next(iter(opponents[opponent])), "fainted!")
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
                        if team2[next(iter(team2))]['hp']>0:
                            if allmoves[move]['category']=='status':
                                userstatusmove(move,opponent)
                            else:
                                userdamage(opponent,move)
                                if opponents[opponent][next(iter(opponents[opponent]))]['hp']<=0:
                                    print(next(iter(opponents[opponent])), "fainted!")
                                    opponentstatchanges.clear()
                                    del opponents[opponent][next(iter(opponents[opponent]))]
                        else:
                            print(next(iter(team2)), "fainted!")
                            print("dab")
                            pokemonstatchanges.clear()
                            w=list(team2.keys()).index(next(iter(team2)))
                            del party3[w]
                            if len(party3)==0:
                                print("You blacked out")
                                print("You quickly went back to the Pokemon Center to heal your Pokemon")
                                money=money/2
                                break
                            else:
                                print(party)
                                v = 5
                                while v == 5:
                                    q=input("Which Pokemon would you like to send out?\n")
                                    q=q.title()
                                    if q not in team2:
                                        print("That is not a valid Pokemon")
                                    elif team2[q]['hp']<=0:
                                        print(q, "has no strength to battle.")
                                    else:
                                        w = list(team2.keys()).index(q)
                                        shifting()
                                        v=7
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
                    if team2[next(iter(team2))]['hp']>0:
                        if allmoves[move]['category']=='status':
                            userstatusmove(move,opponent)
                        else:
                            userdamage(opponent,move)
                            if opponents[opponent][next(iter(opponents[opponent]))]['hp']<=0:
                                print(next(iter(opponents[opponent])), "fainted!")
                                opponentstatchanges.clear()
                                del opponents[opponent][next(iter(opponents[opponent]))]
                    else:
                        print(next(iter(team2)), "fainted!")
                        pokemonstatchanges.clear()
                        w=list(team2.keys()).index(next(iter(team2)))
                        del party3[w]
                        if len(party3)==0:
                            print("You blacked out")
                            print("You quickly went back to the Pokemon Center to heal your Pokemon")
                            money=money/2
                            break
                        else:
                            print(party)
                            v = 5
                            while v == 5:
                                q=input("Which Pokemon would you like to send out?\n")
                                q=q.title()
                                if q not in team2:
                                    print("That is not a valid Pokemon")
                                elif team2[q]['hp']<=0:
                                    print(q, "has no strength to battle.")
                                else:
                                    w = list(team2.keys()).index(q)
                                    shifting()
                                    v=7
            if len(party3)!=0:
                if team2[next(iter(team2))]['status']=='burn':
                    x=team2[next(iter(team2))]['hp']*0.0625
                    x=int(x)
                    if team2[next(iter(team2))]['hp']-x<0:
                        x=team2[next(iter(team2))]
                    i = team2[next(iter(team2))]['hp']-x
                    team2[next(iter(team2))]['hp']=i
                    print(next(iter(team2)), "was hurt by the burn")
                    if x==1:
                        print(next(iter(team2)), "lost", x, "hit point.")
                    else:
                        print(next(iter(team2)), "lost", x, "hit points.")
                    if team2[next(iter(team2))]['hp']<=0:
                        print(next(iter(team2)), "fainted!")
                        pokemonstatchanges.clear()
                        w=list(team2.keys()).index(next(iter(team2)))
                        del party3[w]
                        if len(party3)==0:
                            print("You blacked out")
                            print("You quickly went back to the Pokemon Center to heal your Pokemon")
                            money=money/2
                            break
                        else:
                            print(party)
                            v = 5
                            while v == 5:
                                q=input("Which Pokemon would you like to send out?\n")
                                q=q.title()
                                if q not in team2:
                                    print("That is not a valid Pokemon")
                                elif team2[q]['hp']<=0:
                                    print(q, "has no strength to battle.")
                                else:
                                    w = list(team2.keys()).index(q)
                                    shifting()
                                    v=7
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
                        opponentstatchanges.clear()
                        del opponents[opponent][next(iter(opponents[opponent]))]
                        if len(opponents[opponent])!=0:
                            print(opponent, "sent out %s!" %(next(iter(opponents[opponent]))))
            if len(opponents[opponent])==0:
                break
            elif len(party3)==0:
                break
            else:
                print("%s's %s lv. %s: %s HP"%(player.name, next(iter(team2)), team2[next(iter(team2))]['level'], team2[next(iter(team2))]['hp']))
                print("%s's %s lv. %s: %s HP"%(opponent, next(iter(opponents[opponent])), opponents[opponent][next(iter(opponents[opponent]))]['level'],opponents[opponent][next(iter(opponents[opponent]))]['hp']))
        elif g == 'Run':
            print("You can't run away from a Pokemon battle!")
        else:
            print("That's not a valid choice")
    if len(party3)!=0:
        print("%s beat %s. %s got $%s."%(player.name, opponent, player.name, cash))
        money = money+cash
#define the battles
battle("Lorelei", 100)
if len(party3)!=0:
    battle("Bruno", 100)
    if len(party3)!=0:
        battle("Agatha", 100)
        if len(party3)!=0:
            battle("Lance", 100)
            if len(party3)!=0:
                battle(rivalname, 100)
                if len(party3)!=0:
                    print("You're now the champion. GG")