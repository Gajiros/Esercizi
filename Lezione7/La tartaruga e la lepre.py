import random

def abilities_t(ability: int, position_t: int) -> int:
    if (1 <= ability <= 5):
        position_t += 3 
    elif (6 <= ability <= 7):
        position_t -= 6
        if (position_t < 0):
            position_t = 1
    else:
        position_t += 1
    return position_t

def abilities_h(ability: int, position_h: int):
    if (1 <= ability <= 2):
        position_h = position_h
    elif (3 <= ability <= 4):
        position_h += 9
    elif (ability == 5):
        position_h -= 12
        if (position_h < 0):
            position_h = 1
    elif (6 <= ability <= 8):
        position_h += 1
    else:
        position_h -= 2
        if (position_h < 0):
            position_h = 1
    return position_h

lenght_route: int = 69
route: list = ['TH'] + ['_'] * lenght_route
position_t: int = 0
position_h: int = 0
clock: int = 0

print('BANG !!!!! AND THEY\'RE OFF !!!!!')
while (clock != 999999999999):
    route[position_t] = '_'
    route[position_h] = '_'
    ability_t: int = random.randint(1, 10)
    ability_h: int = random.randint(1, 10)
    position_t = abilities_t(ability_t, position_t)
    position_h = abilities_h(ability_h, position_h)
    
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
    print(route)
    
    clock += 1