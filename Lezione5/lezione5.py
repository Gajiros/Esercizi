#1
def create_playlist(playlist_name: str, *songs: str) -> dict:    
    playlist: dict = {playlist_name: {*songs}}
    return playlist
playlist1: str = 'ciao'
song1: str = '123'
song2: str = '456'
playlist2: str = 'byebye'
song3: str = '789' 
#print(create_playlist(playlist1, song1, song2))
#print(create_playlist(playlist2, song3))
def add_like(playlist: dict, playlist_name: str, feedback: bool) -> dict:
    if playlist_name in playlist:
        playlist[playlist_name] = f'liked: {feedback}'
    return playlist
pl1: dict = create_playlist(playlist1, song1, song2)
#print(add_like(pl1, playlist1, True))
#2
def add_book(author: str, *books: str) -> dict:
    books: dict = {author: [*books]}
    return books
author1: str = 'dada'
book1: str = 'lala'
book2: str = 'pypy'
author2: str = 'tyty'
book3: str = 'oioi'
#print(add_book(author1, book1, book2))
#print(add_book(author2, book3))

#3
