class LibraryBook:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def display_book_info(self):
        print("Book:", self.book_name)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

book1 = LibraryBook("Python Basics", "ABC", 500)
book2 = LibraryBook("Data Science", "XYZ", 700)
book3 = LibraryBook("Machine Learning", "PQR", 900)

book1.display_book_info()
book2.display_book_info()
book3.display_book_info()