import time

#8-1
def display_message(par: str):
    print(par)
string1: str = 'I\'m learning how to make functions.'
display_message(string1)

#8-2
def favorite_book(par: str):
    print(f'One of my favorite books is {par}.')
book_title: str = 'Harry Potter'
favorite_book(book_title)

#8-3
def make_shirt(size: str, message: str):
    print(f'The shirt is a size {size} and its message is {message}.\n')
size1: str = 'M'
message1: str = 'idk'
make_shirt(size1, message1)
make_shirt(size = size1, message = message1)

#8-4
def make_shirt_v2(size: str = 'L', message: str = 'I love Python'):
        print(f'The shirt is a size {size} and its message is {message}.')
size1: str = 'M'
size2: str = 'S'
message1: str = 'Idk what to write'
make_shirt_v2()
make_shirt_v2(size1)
make_shirt_v2(size2, message1)

#8-5
def describe_city(city: str, country: str = 'Italy'):
    print(f'{city} is in {country}.')
city1: str = 'Rome'
city2: str = 'Florence'
city3: str = 'Berlin'
describe_city(city1)
describe_city(city2)
describe_city(city3)

#8-6
def city_country(city: str, country: str) -> str:
    return(f'{city}, {country}.')
city1: str = 'Rome'
country1: str = 'Italy'
city2: str = 'Florence'
country2: str = 'Italy'
city3: str = 'Milan'
country3: str = 'Italy'
pair1: str = city_country(city1, country1)
pair2: str = city_country(city2, country2)
pair3: str = city_country(city3, country3)
print(pair1)
print(pair2)
print(pair3)

#8-7
def make_album(artist: str, album: str, n_songs: int = None) -> dict:
    result: dict = {'artist': artist,'album': album,'n_songs': n_songs}
    return result    
artist1: str = 'Videoclub'
artist2: str = 'Post Malone'
artist3: str = 'Drake'
artist4: str = 'Illit'
album1: str = 'Euphories'
album2: str = 'Stoney'
album3: str = 'Views'
album4: str = 'Super Real Me'
n_songs1: int = 4
art_alb1: dict = make_album(artist1, album1)
art_alb2: dict = make_album(artist2, album2)
art_alb3: dict = make_album(artist3, album3)
art_alb4: dict = make_album(artist4, album4, n_songs1)
print(art_alb1)
print(art_alb2)
print(art_alb3)
print(art_alb4)

#8-8
x: int = 0
while(x < 2):
    x += 1
    artist5: str = input('Type an artist\'s name: ')
    album5: str = input('Type the album\'s name: ')
    art_alb5: dict = make_album(artist5, album5)
    print(art_alb5)

#8-9, 8-10, 8-11
def show_messages(text: list):
    for read in text:
        print(read)
        sent_messages: list = [text2 for text2 in text]
    print(text)
    print('These messages have been sent:', sent_messages)
text1: list = ['1', '2', '3']
text2: list = text1
show_messages(text1)
show_messages(text2)

#8-12
def list_items(*items: str):
    print('The items in the list are: ', end = '')
    for read in items:
        print(read, ', ', end = '')
    print('')
list_items('hamburger', 'tomato', 'salad')
list_items('hamburger', 'tomato')
list_items('hamburger', 'tomato', 'salad', 'ketchup')

#8-13
def build_profile(first_name: str, last_name: str, age: int, hair_color: str, weight: int) -> str:
    profile: str = f"{first_name} {last_name}, age {age}, hair {hair_color}, weight {weight}"
    return profile
profilo1: str = build_profile("Gabriel", "Jimenez", 19, "black", 85)
print(profilo1)

#8-14
def make_car(manufacturer: str, model: str, **kwargs: dict) -> dict:
    car_info: dict = {'manufacturer': manufacturer, 'model': model}
    car_info.update(kwargs)
    return car_info
car: dict = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

#Bubble Sort
def BubbleSort(list: list) -> list:
    for i in range(len(list)):
        swap_flag: bool = False
        for j in range(len(list) - i - 1):
            if (list[j] > list[j + 1]):
                swap_flag = True
                temp: int = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
            continue
        if (swap_flag == False):
            return list
        continue
    return list
start: int = time.time()
list1: list = [n for n in range(0, 10001
                                )]
list_sorted = BubbleSort(list1)
print(list_sorted)
print(time.time() - start)
