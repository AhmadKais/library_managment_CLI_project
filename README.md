# Library Management System

This is a simple Library Management System consisting of two classes: `Book` and `Library`, and a main program to interact with them.

## Book Class

The `Book` class represents a book with its title, author, publication year, and genre. It has the following methods:

- `__init__(self, title, author, publication_year, genre)`: Initializes a book object with the provided details.
- `get_title(self)`: Returns the title of the book.
- `get_author(self)`: Returns the author of the book.
- `get_publication_year(self)`: Returns the publication year of the book.
- `get_genre(self)`: Returns the genre of the book.
- `set_title(self, new_title)`: Updates the title of the book.
- `set_author(self, new_author)`: Updates the author of the book.
- `set_publication_year(self, new_year)`: Updates the publication year of the book.
- `set_genre(self, new_genre)`: Updates the genre of the book.
- `display_book(self)`: Displays the details of the book.

## Library Class

The `Library` class manages a collection of books. It has the following methods:

- `__init__(self, library_name)`: Initializes a library object with a name.
- `get_library_name(self)`: Returns the name of the library.
- `get_library_books(self)`: Returns a list of all books in the library.
- `set_library_name(self, new_name)`: Updates the name of the library.
- `add_book(self, new_book)`: Adds a new book to the library.
- `delete_book(self, book_to_remove)`: Deletes a book from the library.
- `find_book(self, title, author, publication_year, genre)`: Finds a book in the library.
- `edit_book(self, title, author, publication_year, genre)`: Edits the details of a book in the library.
- `display_books(self, filter_type=None, book_filter=None)`: Displays all books in the library, optionally filtered by genre or author.

## Main Program

The main program provides a simple interface for managing the library. It allows users to add, delete, edit, and display books in the library.

### Running the Program

To run the program, execute the `main()` function in `main.py`.

```bash
python main.py
