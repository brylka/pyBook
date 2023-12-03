import unittest
from book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Wiedźmin", "Sapkowski", 2000)
    def test_get_info(self):
        text_correct = "Książka: Wiedźmin Autor: Sapkowski Rok: 2000"
        text_result = self.book.get_info()
        self.assertEqual(text_correct, text_result)

if __name__ == '__main__':
    unittest.main()
