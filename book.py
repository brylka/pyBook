class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Książka: {self.title} Autor: {self.author} Rok: {self.year}"
    def change_title(self, new_title):
        self.title = new_title
    def change_author(self, new_author):
        self.author = new_author
    def change_year(self, new_year):
        self.year = new_year
