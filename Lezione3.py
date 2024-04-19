'''
#4-1, 4-11
fav_pizza: list = ['Margherita', 'Diavola', 'Ortolana']
for output in fav_pizza:
    print(output, 'is one of my favorite type of pizza.\n')
print(f'{fav_pizza[0]}, {fav_pizza[1]} and {fav_pizza[2]} are my favorite pizzas.\n')

import copy
friend_pizzas: list = copy.deepcopy(fav_pizza)
fav_pizza.append('Marinara')
friend_pizzas.append('Napoli')
print('My favorite pizzas are: ', end='')
for read in fav_pizza:
    if (read != fav_pizza[-1]):
        print(read, end=', ')
    else:
        print(read)
        print('\n')
print('My favorite pizzas are: ', end='')
for read in friend_pizzas:
    if (read != friend_pizzas[-1]):
        print(read, end=', ')
    else:
        print(read)
        print('\n')
print('My favorite pizzas are: ', end='')

#4-2
animals: list = ['Cat', 'Dog', 'Rabbit']
for output in animals:
    print(output, 'is a nice pet.\n')
print(f'{animals[0]}s, {animals[1]}s and {animals[2]}s are good pets.\n')

#4-3
for numbers in range(1, 21):
    print(numbers)

#4-4
numbers: list = (range(1, 1000001))
for read in numbers:
    print(read)

#4-5
numbers2: list = (range(1, 1000001))
print(min(numbers2))
print(max(numbers2))
print(sum(numbers2))

#4-6
odd_numbers: list = (range(1, 21, 2))
for read in odd_numbers:
    print(read)

#4-7
multiple_3: list = (range(3, 31, 3))
for read in multiple_3:
    print(read)

#4-8
cubes2: list = range(1, 11)
for i in cubes2:
    print(i ** 3)

#4-9, 4-10
cubes: list = [numbers ** 3 for numbers in range(1, 11)]
for read in cubes:
    print(read)

print('The first three items in the list are: ', cubes[0], ',', cubes[1], ',', cubes[2])
print(cubes[0:3])
print('The three items in the middle of the list are: ', cubes[4], ',', cubes[5], ',', cubes[6])
print(cubes[4:7])
print('The last three items in the list are: ', cubes[-3], ',', cubes[-2], ',', cubes[-1])
print(cubes[-3:])
'''
#5-1
x: int = 0
while (x < 10):
    print('Scrivi una di queste auto (Audi, Mercedes, Lamborghini, Fiat): ')
    auto: str = None
    input(auto)
    if (auto == 'Audi'):
        
    x += 1