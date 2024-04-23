
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

#5-1
x: int = 0
while (x < 10):
    x += 1
    car: str = input('Scrivi una di queste auto (Audi, Mercedes, Lamborghini, Fiat): ')
    if (car == 'Audi'):
        print('Is car == "Audi"? i predict True')
        print(car == 'Audi')
        print('Is car == "Audi"? i predict False')
        print(car != 'Audi')
    elif (car == 'Fiat'):
        print('Is car == "Fiat"? i predict True')
        print(car == 'Fiat')
        print('Is car == "Fiat"? i predict False')
        print(car != 'Fiat')
    elif (car == 'Mercedes'):
        print('Is car == "Mercedes"? i predict True')
        print(car == 'Mercedes')
        print('Is car == "Mercedes"? i predict False')
        print(car != 'Mercedes')
    elif (car == 'Lamborghini'):
        print('Is car == "Lamborghini"? i predict True')
        print(car == 'Lamborghini')
        print('Is car == "Lamborghini"? i predict False')
        print(car != 'Lamborghini')

#5-2
x: int = 0
while (x < 2):
    x += 1
    input1: str = input('Type a string: ')
    input2: str = input('Type another string: ')
    print('\n')
    if ((input1 == input2) or (input1 != input2)):
        print('I predict the strings are equal.')
        print(input1 == input2)
        print('I predict the strings are different.')
        print(input1 != input2, '\n')
        
x: int = 0
while (x < 2):
    x += 1
    input1: str = input('Type a number: ')
    input2: str = input('Type another number: ')
    print('\n')
    if ((input1 == input2) or (input1 != input2)):
        print('I predict the numbers are equal.')
        print(input1 == input2)
        print('I predict the numbers are different.')
        print(input1 != input2, '\n')

x: int = 0
list_numbers: list = [1, 2]
while (x < 1):
    x += 1
    if ((list_numbers[0] == 1) or (list_numbers[1] == 1)):
        print('There is a 1 in the list.')
        print(list_numbers[0] == 1) or (list_numbers[1] == 1)
        print('There isn\'t a 1 in the list.')
        print(list_numbers[0] != 1) and (list_numbers[1] != 1)
  
x: int = 0
while (x < 1):
    x += 1
    if ((list_numbers[0] != 3) or (list_numbers[1] != 3)):
        print('There isn\'t a 3 in the list.')
        print(list_numbers[0] != 3 or (list_numbers[1] != 3))
        print('There is a 3 in the list.')
        print(list_numbers[0] == 3 or (list_numbers[1] == 3))

#5-3
alien_color: str = 'red'
if (alien_color == 'green'):
    print('The player just earned 5 points.')
elif (alien_color == 'yellow'):
    print('The player just earned 5 points.')
elif (alien_color == 'red'):
    print('The player just earned 5 points.')
alien_color: str = 'purple'
if (alien_color == 'green'):
    print('The player just earned 5 points.')
elif (alien_color == 'yellow'):
    print('The player just earned 5 points.')
elif (alien_color == 'red'):
    print('The player just earned 5 points.')
else:
    print()

#5-4
x: int = 0
while (x < 2):
    x += 1
    alien_color: str = input('Choose the color of the alien you want to shoot: ')
    if (alien_color == 'green'):
        print('The player just earned 5 points for shooting the alien.')
    else:
        print('The player just earned 10 point.')

#5-5
x: int = 0
while (x < 3):
    x += 1
    alien_color: str = input('Choose the color of the alien you want to shoot: ')
    if (alien_color == 'green'):
        print('The player just earned 5 points.')
    elif (alien_color == 'red'):
        print('The player just earned 15 points.')
    elif (alien_color == 'yellow'):
        print('The player just earned 10 points.')

#5-6
x: int = 0
while (x < 6):
    x += 1
    age: int = int(input('Choose the age of the person: '))
    if (age < 2):
        print('The person is a baby.')
    elif ((age >= 2) and (age < 4)):
        print('The person is a toddler.')
    elif ((age >= 4) and (age < 13)):
        print('The person is a kid.')
    elif ((age >= 13) and (age < 20)):
        print('The person is a teenager.')
    elif ((age >= 20) and (age < 65)):
        print('The person is an adult.')
    elif (age >= 65):
        print('The person is an elder.')

#5-7
favorite_fruits: list = ['banana', 'apple', 'pear']
for a in favorite_fruits:
    if (a == 'banana'):
        print('You really like bananas.')
    elif (a == 'apple'):
        print('You really like apples')
    elif (a == 'pear'):
        print('You really like pears')

#5-8, 5-9
usernames: list = ['admin', 'jaden', 'emma', 'noah', 'sophia']
for username in usernames:
    if (username == 'admin'):
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.capitalize()}, thank you for logging in again.")

usernames = []
if (usernames):
    if (username == 'admin'):
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.capitalize()}, thank you for logging in again.")
else:
    print('We need to find some users!')

#5-10
current_users: list = ['Gabriel', 'Alessio', 'Francesco', 'Light', 'L']
current_users_lower: list = [read.lower() for read in current_users]
new_users: list = ['Gabriel', 'Alessio', 'Simone', 'Federico', 'Edoardo']
for a in new_users:
    for b in current_users:
        if (a == b):
            print('The username is taken. Choose another one.')
        else:
            None   

#5-11
numbers: list = range(1, 10)
for a in numbers:
    if (a == 1):
        print('1st')
    elif (a == 2):
        print('2nd')
    elif (a == 3):
        print('3rd')
    else:
        print(f'{a}th')