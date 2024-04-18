# Gabriel Jimenez Rosario
# 17/04/2024

print()
print('----------------------------')
print('\n2-3\n')

#2-3
name: str = 'Mario'
message: str = f'Ciao {name}, ti va di imparare un po\' di python insieme'
print(message)
print()
print('----------------------------')
print('\n2-4\n')

# 2-4
name1: str = 'Giulio'
name1_lower: str = name1.lower()
print(name1_lower)
name1_upper: str = name1.upper()
print(name1_upper)
name1_title: str = name1.title()
print(name1_title)
print()
print('----------------------------')
print('\n2-5\n')

#2-5
print('Kobe Bryant once said: \"If you’re afraid to fail,then you’re probably going to fail.\"')
print()
print('----------------------------')
print('\n2-6\n')

#2-6
message: str = "\"If you’re afraid to fail,then you’re probably going to fail.\""
famous_person: str = 'Kobe Bryant'
print(f'{famous_person} once said: {message}')
print()
print('----------------------------')
print('\n2-8\n')

#2-8
filename: str = 'python_notes.txt'
print(filename.removesuffix('.txt'))
print()
print('----------------------------')
print('\n3-1, 3-2\n')

#3.1, 3-2
names: list = ['Valerio', 'Alessio', 'Edoardo']
print(names[0])
print(names[1])
print(names[2])

print(f'Hello {names[0]}, how are you?')
print(f'Hello {names[1]}, how are you?')
print(f'Hello {names[2]}, how are you?')
print()
print('----------------------------')
print('\n3-3\n')

#3-3
mode_trasportation: list = ['motocycles', 'cars', 'airplanes']
print(f'{mode_trasportation[2]} are really fast.')
print(f'{mode_trasportation[1]} are cool.')
print(f'{mode_trasportation[0]} are dangerous.')
print()
print('----------------------------')
print('\n3-4, 3-5, 3-6, 3-7, 3-9\n')

#3-4, 3-5, 3-6, 3-7, 3-9
guest_list: list = ['Kobe Byrant', 'Lebron James', 'Stephen Curry']
print(f'Hi {guest_list[0]} come have dinner tonight, i\'ve also invited other people!')
print(f'Hi {guest_list[1]} come have dinner tonight, i\'ve also invited other people!')
print(f'Hi {guest_list[2]} come have dinner tonight, i\'ve also invited other people!')

print(f'Hi {guest_list[0]}, don\'t worry if you can\' make it tonight.')
guest_list.pop(0)
guest_list.insert(0, 'James Harden')
print(f'Hi {guest_list[0]} come have dinner tonight, i\'ve also invited other people!')
print(f'Hi {guest_list[1]} come have dinner tonight, i\'ve also invited other people!')
print(f'Hi {guest_list[2]} come have dinner tonight, i\'ve also invited other people!')

print(f'Important, i\'ve decided to invite more people because i found a bigger table so you\'re going to receive a new invite')
guest_list.insert(0, 'Jimmy Butler')
guest_list.insert(2, 'Shaq')
guest_list.append('Steve Nash')
print(f'Hi {guest_list[0]} come have dinner tonight, i\'ve also invited other people!')
print(f'Hi {guest_list[1]} come have dinner tonight, i\'ve also invited other people!')
print(f'Hi {guest_list[2]} come have dinner tonight, i\'ve also invited other people!')
print(f'Hi {guest_list[3]} come have dinner tonight, i\'ve also invited other people!')
print(f'Hi {guest_list[4]} come have dinner tonight, i\'ve also invited other people!')
print(f'Hi {guest_list[5]} come have dinner tonight, i\'ve also invited other people!')

print('I\'m sorry, but i can only invite 2 people tonight')
print(f'I\'m sorry {guest_list[0]} but there\'s not enough space for everybody tonight, it\'s ok if we have dinner together another time?')
guest_list.pop(0)
print(f'I\'m sorry {guest_list[0]} but there\'s not enough space for everybody tonight, it\'s ok if we have dinner together another time?')
guest_list.pop(0)
print(f'I\'m sorry {guest_list[0]} but there\'s not enough space for everybody tonight, it\'s ok if we have dinner together another time?')
guest_list.pop(0)
print(f'I\'m sorry {guest_list[0]} but there\'s not enough space for everybody tonight, it\'s ok if we have dinner together another time?')
guest_list.pop(0)
print (f'Hey {guest_list[0]} you\'re still invited to dinner')
print (f'Hey {guest_list[1]} you\'re still invited to dinner')
guest_list.__delitem__(0)
guest_list.__delitem__(0)
print(guest_list)

print(len(guest_list))
print()
print('----------------------------')
print('\n3-8\n')

#3-8
places: list = ['Tokyo', 'Los Angeles', 'China', 'Paris', 'Korea']
print(places)
places_sorted_alp: list = sorted(places)
print(places_sorted_alp)
places_sorted_rev: list = sorted(places, reverse=True)
print(places_sorted_rev)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print()
print('----------------------------')
print('\n3-10\n')

#3-10
list: list = ['Mountains', 'Rivers', 'Countries', 'Cities', 'Languages']
list.pop(0)
list.__delitem__(0)
print(list)
list.insert(0, 'Mountains')
list.append('Rivers')
print(sorted(list))
print(sorted(list, reverse=True))
list.reverse()
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
print()
print('----------------------------')
print('\n6-1, 6-7\n')

#6.1, 6-7
person: dict = {'first_name': 'Gabriel', 'last_name': 'Jimenez', 'age': 19, 'city': 'Rome'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

person2: dict = {'first_name': 'Francesco', 'last_name': 'Milesi', 'age': 20, 'city': 'Alpignano'}
person3: dict = {'first_name': 'Gianmarco', 'last_name': 'Dell\'uomo', 'age': 18, 'city': 'Sabaudia'}
people_dict: list = [person, person2, person3]
print(people_dict[0]['first_name'])
print(people_dict[0]['last_name'])
print(people_dict[0]['age'])
print(people_dict[0]['city'], '\n')
print(people_dict[1]['first_name'])
print(people_dict[1]['last_name'])
print(people_dict[1]['age'])
print(people_dict[1]['city'], '\n')
print(people_dict[2]['first_name'])
print(people_dict[2]['last_name'])
print(people_dict[2]['age'])
print(people_dict[2]['city'], '\n')
print()
print('----------------------------')
print('\n6-2, 6-10\n')

#6-2, 6-10
fav_numbers: dict = {'Gabriel': 4, 'Alessandro': 20, 'Leonardo': 9, 'Alessio': 10, 'Francesco': 13}
print('Gabriel:', fav_numbers['Gabriel'])
print('Alessandro:', fav_numbers['Alessandro'])
print('Leonardo:', fav_numbers['Leonardo'])
print('Alessio:', fav_numbers['Alessio'])
print('Francesco:', fav_numbers['Francesco'])

fav_numbers['Gabriel'] = [4, 2]
fav_numbers['Alessandro'] = [20, 101]
fav_numbers['Leonardo'] = [9, 15]
fav_numbers['Alessio'] = [10, 85]
fav_numbers['Francesco'] = [13, 99]
print('Gabriel:', fav_numbers['Gabriel'][0], ',', fav_numbers['Gabriel'][1])
print('Alessandro:', fav_numbers['Alessandro'][0], ',', fav_numbers['Alessandro'][1])
print('Leonardo:', fav_numbers['Leonardo'][0], ',', fav_numbers['Leonardo'][1])
print('Alessio:', fav_numbers['Alessio'][0], ',', fav_numbers['Alessio'][1])
print('Francesco:', fav_numbers['Francesco'][0], ',', fav_numbers['Francesco'][1])
print()
print('----------------------------')
print('\n6-3\n')

#6-3
glossary: list = {'pop': 'scoppiare', 'insert': 'inserire', 'print': 'stampare', 'list': 'lista', 'dictionary': 'dizionario'}
print(' pop\n', ' \\\\\n', glossary['pop'], '\n')
print(' insert\n', ' \\\\\n', glossary['insert'], '\n')
print(' print\n', ' \\\\\n', glossary['print'], '\n')
print(' list\n', ' \\\\\n', glossary['list'], '\n')
print(' dictionary\n', ' \\\\\n', glossary['dictionary'], '\n')
print()
print('----------------------------')
print('\n6-8\n')

#6-8
pet1: dict = {'owner': 'Gabriel', 'kind': 'parrot'}
pet2: dict = {'owner': 'Leonardo', 'kind': 'cat'}
pet3: dict = {'owner': 'Francesco', 'kind': 'rabbit'}
pet4: dict = {'owner': 'Gianmarco', 'kind': 'dog'}
pets: list = [pet1, pet2, pet3, pet4]
print(pets[0]['owner'])
print(pets[0]['kind'], '\n')
print(pets[1]['owner'])
print(pets[1]['kind'], '\n')
print(pets[2]['owner'])
print(pets[2]['kind'], '\n')
print(pets[3]['owner'])
print(pets[3]['kind'], '\n')
print()
print('----------------------------')
print('\n6-9\n')

#6-9
favorite_places: dict = {'Francesco': 'Torino', 'Gianmarco': 'Roma', 'Gabriel': 'Siena'}
print('Francesco: ', favorite_places['Francesco'])
print('Gianmarco: ', favorite_places['Gianmarco'])
print('Gabriel: ', favorite_places['Gabriel'])
print()
print('----------------------------')
print('\n6-11, 6-12\n')

#6-11, 6-12(formatting)
cities: dict = {'Rome': {'country': 'Italy', 'population': '3 million', 'fact': 'has more fountains than any other city on the planet.'}, 'Paris': {'country': 'France', 'population': '2 milion', 'fact': 'not it\'s original name.'}, 'Berlin': {'country': 'Germany', 'population': '3.6 milion', 'fact': 'is the greenest city in Europe.'}}
print('Rome', 'is the capital city of', cities['Rome']['country'], 'and has almost', cities['Rome']['population'], 'residents, it also', cities['Rome']['fact'], '\n')
print('Paris', 'is the capital city of', cities['Paris']['country'], ', has almost', cities['Paris']['population'], 'residents, it\'s also', cities['Paris']['fact'], '\n')
print('Berlin', 'is the capital city of', cities['Berlin']['country'], ', has almost', cities['Berlin']['population'], 'residents and', cities['Berlin']['fact'], '\n')
