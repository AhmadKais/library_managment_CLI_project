from book import Book
from library import Library


def main():
    my_library = Library("My Library")

    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a book")
        print("2. Delete a book")
        print("3. Display all books (filter")
        print("4. Edit a book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publication_year = input("Enter the publication year of the book: ")
            genre = input("Enter the genre of the book: ")

            new_book = Book(title, author, publication_year, genre)
            my_library.add_book(new_book)

        elif choice == '2':
            title = input("Enter the title of the book you want to delete: ")
            author = input("Enter the author of the book you want to delete: ")
            publication_year = input("Enter the publication year of the book you want to delete: ")
            genre = input("Enter the genre of the book you want to delete: ")

            book_to_delete = Book(title, author, publication_year, genre)
            my_library.delete_book(book_to_delete)

        elif choice == '3':
            while True :
                print("enter based on what would you like to print the books:")
                print("1. filter by Genre")
                print("2.filter by autor ")
                print("3. print All")
                print("4. change my mind exit ")
                display_choice = input("Enter your choice: ")
                if display_choice == '1':
                    genre = input("enter the Genre of the books you want to display")
                    my_library.display_books('Genre',genre)
                elif display_choice == '2':
                    author = input("enter the  Author of the books you want to display")
                    my_library.display_books('Author', author)
                elif display_choice == '3':
                    print("ptinting all books")
                    my_library.display_books()
                elif display_choice == '4':
                    print("nothing to print ")
                    break
                else :
                    print("invalid input ")


        elif choice == '4':
            title = input("Enter the title of the book you want to Edit: ")
            author = input("Enter the author of the book you want to Edit: ")
            publication_year = input("Enter the publication year of the book you want to Edit: ")
            genre = input("Enter the genre of the book you want to Edit: ")
            my_library.edit_book(title,author,publication_year,genre)

        elif choice == '5':
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
