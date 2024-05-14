import random

def abilities_t(ability: int, position_t: int, weather: str) -> int:
    
    if (1 <= ability <= 5):
        position_t += 3 
    elif (6 <= ability <= 7):
        position_t -= 6
        if (position_t < 0):
            position_t = 0
    else:
        position_t += 1
    if (weather == 'pioggia'):
        position_t -= 1
        if (position_t < 0):
            position_t = 0
    return position_t

def abilities_h(ability: int, position_h: int, weather: str) -> int:
    
    if (1 <= ability <= 2):
        position_h = position_h
    elif (3 <= ability <= 4):
        position_h += 9
    elif (ability == 5):
        position_h -= 12
        if (position_h < 0):
            position_h = 0
    elif (6 <= ability <= 8):
        position_h += 1
    else:
        position_h -= 2
        if (position_h < 0):
            position_h = 0
    if (weather == 'pioggia'):
        position_h -= 2
        if (position_h < 0):
            position_h = 0
    return position_h

def positions(route: list):
    
    print(route)

length_route: int = 69
route: list = ['TH'] + ['_'] * length_route
position_t: int = 0
position_h: int = 0
tick: int = 0
weather_change: list = range(0, 99999999, 10)

print('BANG !!!!! AND THEY\'RE OFF !!!!!')
while (tick != 999999999999):
    for read in weather_change:
        if (tick == read):
            weather: str = random.choice(['soleggiato', 'pioggia'])
            #print(weather)
    route[position_t] = '_'
    route[position_h] = '_'
    ability_t: int = random.randint(1, 10)
    ability_h: int = random.randint(1, 10)
    position_t = abilities_t(ability_t, position_t, weather)
    position_h = abilities_h(ability_h, position_h, weather)
        
    if (position_t >= 69):
        print("TORTOISE WINS! || VAY!!!")
        break
    elif (position_h >= 69):
        print("HARE WINS! || YUCH!!!")
        break
    elif (position_t >= 69) and (position_h >= 69):
        print("IT'S A TIE.")
        break

    if (route[position_t] == '_'):
        route[position_t] = 'T'
    elif (route[position_t] == 'H'):
        print('OUCH!!!')
        route[position_t] = 'TH'

    if (route[position_h] == '_'):
        route[position_h] = 'H'
    elif (route[position_h] == 'T'):
        print('OUCH!!!')
        route[position_h] = 'TH'
    positions(route)
    tick += 1
