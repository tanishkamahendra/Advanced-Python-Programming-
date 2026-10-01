class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def register_member(self, member):
        self.members.append(member)
        print("Member registered successfully")

    def borrow_book(self, member, book):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print(member.name, "borrowed", book.title)
        else:
            print("Book is not available")

    def return_book(self, member, book):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(member.name, "returned", book.title)
        else:
            print("This book was not borrowed by the member")


library = Library()

book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Structures", "Robert Brown")

library.add_book(book1)
library.add_book(book2)

member1 = member("Tanishka")
library.register_member(member1)

library.borrow_book(member1, book1)
library.return_book(member1, book1)