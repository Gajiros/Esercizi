class Book:

    def __init__(self, title: str, author: str) -> None:
        
        self.title = title
        self.author = author
        self.isBorrowed = False

class Library:

    def __init__(self) -> None:
        
        self.books = []

    def addBook(self, book: Book):

        self.books.append(book)
        print('The book has been added.')

    def borrowBook(self, title: str):

        flag: bool = False
        for book in self.books:

            if ((book.title == title) and (book.isBorrowed == False)):

                flag = True
                book.isBorrowed = True
                print('The book is available and has been booked.')
                break
        
        if (flag == False):

            print('The book is not available.')

    def returnBook(self, title: str):

        flag: bool = False
        for book in self.books:

            if (book.title == title):

                flag = True
                book.isBorrowed = False
                print('The book has been returned.')
                break
        
        if (flag == False):

            print('There is not a book with this title.')

    def showBooks(self):

        flag: bool = False
        list1: list = []
        for book in self.books:

            if (book.isBorrowed == False):
                
                flag = True
                list1.append(book.title)
            
        if (flag == False):

            print('There are no books available.')
        
        else:

            print(list1)

#library1: Library = Library()

#book1: Book = Book('gesu e la madonna', 'giuseppe')
#book2: Book = Book('un tradimento della madonna', 'valerio')

#library1.addBook(book1)
#library1.addBook(book2)

#library1.borrowBook('gesu e la madonna')
#library1.returnBook('gesu e la madonna')
#library1.showBooks()

class MovieCatalog:

    def __init__(self) -> None:
        
        self.movies = {}
    
    def add_movie(self, director_name: str, movies: list):

        for movie in movies:

            if (director_name in self.movies):

                self.movies[director_name].append(movie)

            else:    
            
                self.movies.update({director_name: [movie]})

    def remove_movie(self, director_name: str, movie: str):

        self.movies[director_name].remove(movie)
        if (self.movies[director_name] == []):

            print('The director has no more movies in the catalog do you want to remove it too? Say y or n: ', end = '')
            choice: str = input()
            if (choice == 'y'):

                self.movies.pop(director_name)

    def list_directors(self):
        
        print('Directors: ')
        for director in self.movies:

            print(director)

    def get_movies(self, director_name: str):

        print('Movies:')
        for movie in self.movies[director_name]:

                print(movie)
    
    def search_movies_by_title(self):

        pass



#catalog1: MovieCatalog = MovieCatalog()
#catalog1.add_movie('valeriozzo', ['un tradimento della madonna'])
#catalog1.add_movie('valeriozzo', ['un tradimento della madonna 2: LA VENDETTA DI DIO!'])
#catalog1.remove_movie('valeriozzo', 'un tradimento della madonna')
#catalog1.list_directors()
#catalog1.get_movies('valeriozzo')
#catalog1.remove_movie('valeriozzo', 'un tradimento della madonna 2: LA VENDETTA DI DIO!')
#catalog1.list_directors()

class Veicolo:
    
    def __init__(self, marca: str, modello: str, anno: int):
        
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def descrivi_veicolo(self):
        
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}')
    
class Auto(Veicolo):
    
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
        
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrivi_veicolo(self):

        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}')

class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, tipo: str):
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self):
        
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}')