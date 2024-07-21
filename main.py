from book_operations import Book, Genre
from user_operations import User
from author_operations import Author

books = []
users = []
authors = []
genres = []

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!\n")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")
        choice = input("Select an option: ")
        if choice == '1':
            book_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            author_menu()
        elif choice == '4':
            genre_menu()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def book_menu():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to main menu")
        choice = input("Select an option: ")
        if choice == '1':
            add_new_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

def user_menu():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to main menu")
        choice = input("Select an option: ")
        if choice == '1':
            add_new_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def author_menu():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to main menu")
        choice = input("Select an option: ")
        if choice == '1':
            add_new_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def genre_menu():
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to main menu")
        choice = input("Select an option: ")
        if choice == '1':
            add_new_genre()
        elif choice == '2':
            view_genre_details()
        elif choice == '3':
            display_all_genres()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def add_new_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    publication_date = input("Enter book publication date: ")
    genre_name = input("Enter book genre: ")
    genre = next((g for g in genres if g.get_name() == genre_name), None)
    if not genre:
        print("Genre not found. Please add the genre first.")
        return
    book = Book(title, author, isbn, publication_date, genre)
    books.append(book)
    print("Book added successfully.")

def borrow_book():
    isbn = input("Enter book ISBN to borrow: ")
    user_id = input("Enter user library ID: ")
    book = next((b for b in books if b.get_isbn() == isbn), None)
    user = next((u for u in users if u.get_library_id() == user_id), None)
    if book and user:
        if book.borrow():
            user.borrow_book(book.get_title())
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")
    else:
        print("Book or user not found.")

def return_book():
    isbn = input("Enter book ISBN to return: ")
    user_id = input("Enter user library ID: ")
    book = next((b for b in books if b.get_isbn() == isbn), None)
    user = next((u for u in users if u.get_library_id() == user_id), None)
    if book and user:
        book.return_book()
        user.return_book(book.get_title())
        print("Book returned successfully.")
    else:
        print("Book or user not found.")

def search_book():
    isbn = input("Enter book ISBN to search: ")
    book = next((b for b in books if b.get_isbn() == isbn), None)
    if book:
        print(f"Title: {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_isbn()}, "
              f"Publication Date: {book.get_publication_date()}, Available: {book.is_available()}")
    else:
        print("Book not found.")

def display_all_books():
    if books:
        for book in books:
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_isbn()}, "
                  f"Publication Date: {book.get_publication_date()}, Available: {book.is_available()}")
    else:
        print("No books available.")

def add_new_user():
    name = input("Enter user name: ")
    library_id = input("Enter user library ID: ")
    user = User(name, library_id)
    users.append(user)
    print("User added successfully.")

def view_user_details():
    library_id = input("Enter user library ID to view details: ")
    user = next((u for u in users if u.get_library_id() == library_id), None)
    if user:
        print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {', '.join(user.get_borrowed_books())}")
    else:
        print("User not found.")

def display_all_users():
    if users:
        for user in users:
            print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {', '.join(user.get_borrowed_books())}")
    else:
        print("No users available.")

def add_new_author():
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    author = Author(name, biography)
    authors.append(author)
    print("Author added successfully.")

def view_author_details():
    name = input("Enter author name to view details: ")
    author = next((a for a in authors if a.get_name() == name), None)
    if author:
        print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")
    else:
        print("Author not found.")

def display_all_authors():
    if authors:
        for author in authors:
            print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")
    else:
        print("No authors available.")

def add_new_genre():
    name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")
    genre = Genre(name, description, category)
    genres.append(genre)
    print("Genre added successfully.")

def view_genre_details():
    name = input("Enter genre name to view details: ")
    genre = next((g for g in genres if g.get_name() == name), None)
    if genre:
        print(f"Name: {genre.get_name()}, Description: {genre.get_description()}, Category: {genre.get_category()}")
    else:
        print("Genre not found.")

def display_all_genres():
    if genres:
        for genre in genres:
            print(f"Name: {genre.get_name()}, Description: {genre.get_description()}, Category: {genre.get_category()}")
    else:
        print("No genres available.")

if __name__ == "__main__":
    main_menu()
