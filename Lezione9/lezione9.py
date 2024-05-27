class Book:
    
    def __init__(self, book_id: str, title: str, author: str) -> None:
        
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        
        self.is_borrowed = True
    
    def return_book(self):
        
        self.is_borrowed = False

class Member:
    
    def __init__(self, member_id: str, name: str) -> None:

        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):

        if (book in self.borrowed_books):
            pass
        else: 
            self.borrowed_books.append(book)
            book.borrow()

    def return_book(self, book: Book):

        if (book in self.borrowed_books):   
            self.borrowed_books.remove(book)
            book.return_book()
        
class Library:
    
    def __init__(self) -> None:

        self.books = {}
        self.members = {}
    
    def add_book(self, book_id: str, title: str, author: str):

        book: Book = Book(book_id, title, author)
        self.books.setdefault(book_id, book)

    def register_member(self, member_id: str, name: str):

        member: Member = Member(member_id, name)
        self.members.setdefault(member_id, member)

    def borrow_book(self, member_id: str, book_id: str):

        self.members[member_id].borrow_book(self.books[book_id])
    
    def return_book(self, member_id: str, book_id: str):

        self.members[member_id].return_book(self.books[book_id])
    
    def get_borrowed_books(self, member_id: str) -> list:

        return self.members[member_id].borrowed_books

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

	

['The Great Gatsby']
['1984']

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Check borrowed books after returning
print(library.get_borrowed_books("M001"))
print(library.get_borrowed_books("M002"))