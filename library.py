from book import Book


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def get_library_name(self):
        return self.library_name

    def get_library_books(self):
        return self.books

    def set_library_name(self, new_name):
        self.library_name = new_name

    # iterate over all the books and see whether the book already exists or not
    def add_book(self, new_book: Book):
        for book in self.books:
            if new_book.get_genre() == book.get_genre() and new_book.get_title() == book.get_title() and new_book.get_author() == book.get_author() and new_book.get_publication_year() == book.get_publication_year():
                print("Book Already exists in the Library !!")
                return
        self.books.append(new_book)

    # iterate all over the books and see if the book is in the library or not
    def delete_book(self, book_to_remove):
        for book in self.books:
            if book_to_remove.get_genre() == book.get_genre() and book_to_remove.get_title() == book.get_title() and book_to_remove.get_author() == book.get_author() and book_to_remove.get_publication_year() == book.get_publication_year():
                self.books.remove(book_to_remove)
                return
        print("The book you are trying to remove does not exist !!!")

    def find_book(self, title, author, publication_year, genre):
        for book in self.books:
            if genre == book.get_genre() and title == book.get_title() and author == book.get_author() and publication_year == book.get_publication_year():
                return book
        print("The book you are trying to modify does not exist !!!")
        return -1

    def edit_book(self, title, author, publication_year, genre):
        book_to_edit = self.find_book(title, author, publication_year, genre)
        if book_to_edit != -1:
            print("What would you like to edit")
            while True:
                print("\n type what part you want to modify")
                print("1. Title")
                print("2. Author")
                print("3. Publication Year")
                print("4. Genre")
                print("5. None ( exit )")
                choice = input("Enter your choice: ")
                if choice == "1":
                    new_title = input("enter a new_title for the book")
                    book_to_edit.set_title(new_title)
                elif choice == "2":
                    new_author = input("enter a new_Author for the book")
                    book_to_edit.set_title(new_author)
                elif choice == "4":
                    new_genre = input("enter a new_genre for the book")
                    book_to_edit.set_title(new_genre)
                elif choice == "3":
                    new_publication_year = input("enter a new_publication_year for the book")
                    book_to_edit.set_title(new_publication_year)
                elif choice == "5":
                    print("done modifing")
                    break
                else :
                    print("you need to enter a number between 1 to 5")

    def display_books(self, filter_type=None, book_filter=None):
        print(f"The Libraries Name : {self.library_name} ")
        print()  # empty line
        i = 1
        for book in self.books:
            if filter_type == 'Genre':
                if book.get_genre() == book_filter:
                    print(f" book : {i}")
                    book.display_book()
            elif filter_type == 'Author':
                if book.get_author() == book_filter:
                    print(f" book : {i}")
                    book.display_book()
            else:
                print(f" book : {i}")
                book.display_book()
            i += 1
