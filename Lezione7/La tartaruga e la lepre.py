import random

def abilities_t(ability: int, position_t: int, weather: str, stamina: int) -> int:
    
    if (1 <= ability <= 5):
        if ((stamina - 5) >= 0):
            position_t += 3
        else:
            stamina += 10                
    elif (6 <= ability <= 7):
        if ((stamina - 10) >= 0):
            position_t -= 6
            if (position_t < 0):
                position_t = 0
        else:
            stamina += 10
    else:
        if ((stamina - 3) >= 0):
            position_t += 1
        else:
            stamina += 10
    if (weather == 'pioggia'):
        position_t -= 1
        if (position_t < 0):
            position_t = 0
    return position_t

def abilities_h(ability: int, position_h: int, weather: str, stamina: int) -> int:
    
    if (1 <= ability <= 2):
        position_h = position_h
        if ((stamina + 10) <= 100):
            stamina += 10
        else:
            stamina = 100
    elif (3 <= ability <= 4):
        if ((stamina - 15) >= 0):
            position_h += 9
    elif (ability == 5):
        if ((stamina - 20) >= 0):
            position_h -= 12
            if (position_h < 0):
                position_h = 0
    elif (6 <= ability <= 8):
        if ((stamina - 5) >= 0):
            position_h += 1
    else:
        if ((stamina - 8) >= 0):
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
stamina_t: int = 100
stamina_h: int = 100

print('BANG !!!!! AND THEY\'RE OFF !!!!!')
while (tick != 999999999):
    for read in weather_change:
        if (tick == read):
            weather: str = random.choice(['soleggiato', 'pioggia'])
            #print(weather)
    route[position_t] = '_'
    route[position_h] = '_'
    ability_t: int = random.randint(1, 10)
    ability_h: int = random.randint(1, 10)
    position_t = abilities_t(ability_t, position_t, weather, stamina_t)
    position_h = abilities_h(ability_h, position_h, weather, stamina_h)
        
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
