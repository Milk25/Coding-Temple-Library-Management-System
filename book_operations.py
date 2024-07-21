class Genre:
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_category(self):
        return self.__category

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_category(self, category):
        self.__category = category


class Book(Genre):
    def __init__(self, title, author, isbn, publication_date, genre):
        super().__init__(genre.get_name(), genre.get_description(), genre.get_category())
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__available

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True
