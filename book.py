class Book:
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publication_year(self):
        return self.publication_year

    def get_genre(self):
        return self.genre

    def set_title(self, new_title):
        self.title = new_title

    def set_author(self, new_author):
        self.author = new_author

    def set_publication_year(self, new_year):
        self.publication_year = new_year

    def set_genre(self, new_genre):
        self.genre = new_genre

    def display_book(self):
        print(f"Title: {self.title} \nAuthor: {self.author}  \n")
        print(f"Publication Year : {self.publication_year}\n Genre : {self.genre} \n ")

