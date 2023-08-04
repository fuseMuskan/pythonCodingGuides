class Book:
    def __init__(self, title, author, ISBN, genre, availability) -> None:
        self._title = title
        self._author = author
        self._ISBN = ISBN
        self._genre = genre
        self._availability = availability

    def get_book_details(self):
        return f'Title: {self._title}\nAuthor: {self._author}\nISBN: {self._ISBN}\nGenre: {self._genre}\nAvailiability: {self._availability}\n'

class LibraryCatalog:
    def __init__(self) -> None:
        self._book_list = []
    
    def store_book(self, book):
        self._book_list.append(book)
        print("book stored")

    def get_all_books(self):
        return self._book_list



class BorrowBook:
    def __init__(self) -> None:
        self._borrow_books = []
    
    def borrow_book(self,book):
        self._borrow_books.append(book)
        print("book borrowed")
    
    def get_borrow_book(self):
        return self._borrow_books
        


b1 = Book("science","albert",123,'course',True)
b2 = Book("physic","einstine",11,'course',True)



lib = LibraryCatalog()
lib.store_book(b1)
lib.store_book(b2)
all_book = lib.get_all_books()

#getting all books
for b in all_book:
    print(b.get_book_details())

borrow = BorrowBook()
borrow.borrow_book(b1)
borrow.borrow_book(b2)

# all_borrowed_books
all_borrow_book = borrow.get_borrow_book()
for book in all_borrow_book:
    print(book.get_book_details())