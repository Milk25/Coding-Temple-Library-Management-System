class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def set_name(self, name):
        self.__name = name

    def set_biography(self, biography):
        self.__biography = biography
