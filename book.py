class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Książka: {self.title} Autor: {self.author} Rok: {self.year}"

book = Book("Wiedźmin", "AS", 2000)
print(book.get_info())