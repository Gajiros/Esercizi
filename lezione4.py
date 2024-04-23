'''
#8-1
def display_message(par: str) -> str:
    print(par)
string1: str = 'I\'m learning how to make functions.'
display_message(string1)

#8-2
def favorite_book(par: str) -> str:
    print(f'One of my favorite books is {par}.')
book_title: str = 'Harry Potter'
favorite_book(book_title)

#8-3
def make_shirt(size: str, message: str) -> str:
    print(f'The shirt is a size {size} and its message is {message}.\n')
size1: str = 'M'
message1: str = 'idk'
make_shirt(size1, message1)
make_shirt(size = size1, message = message1)
'''
#8-4
def make_shirt_v2(size: str, message: str) -> str:
    if 