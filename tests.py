import unittest
from main import BooksCollector

class TestBooksCollector(unittest.TestCase):

    def setUp(self):
        self.collector = BooksCollector()

    def test_add_new_books(self):
        self.collector.add_new_book("Мастер и Маргарита")
        self.assertEqual(self.collector.books_genre, {"Мастер и Маргарита": ""})
        self.collector.add_new_book("1984")
        self.assertEqual(self.collector.books_genre, {"Мастер и Маргарита": "", "1984": ""})
        self.collector.add_new_book("Мальчик, который поймал журавля")
        self.assertEqual(self.collector.books_genre, {"Мастер и Маргарита": "", "1984": "", "Мальчик, который поймал журавля": ""})

    def test_set_book_genre(self):
        self.collector.add_new_book("Мастер и Маргарита")
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        self.assertEqual(self.collector.books_genre, {"Мастер и Маргарита": "Фантастика", "1984": ""})

    def test_get_book_genre(self):
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("1984", "Фантастика")
        self.assertEqual(self.collector.get_book_genre("1984"), "Фантастика")

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book("Мастер и Маргарита")
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        self.collector.set_book_genre("1984", "Фантастика")
        self.assertEqual(self.collector.get_books_with_specific_genre("Фантастика"), ["Мастер и Маргарита", "1984"])

    def test_get_books_genre(self):
        self.collector.add_new_book("Мастер и Маргарита")
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        self.assertEqual(self.collector.get_books_genre(), {"Мастер и Маргарита": "Фантастика", "1984": ""})

    def test_get_books_for_children(self):
        self.collector.add_new_book("Мастер и Маргарита")
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        self.collector.set_book_genre("1984", "Детективы")
        self.assertEqual(self.collector.get_books_for_children(), ["Мастер и Маргарита"])

    def test_add_book_in_favorites(self):
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("1984", "Фантастика")
        self.collector.add_book_in_favorites("1984")
        self.assertEqual(self.collector.get_list_of_favorites_books(), ["1984"])

    def test_delete_book_from_favorites(self):
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("1984", "Фантастика")
        self.collector.add_book_in_favorites("1984")
        self.collector.delete_book_from_favorites("1984")
        self.assertEqual(self.collector.get_list_of_favorites_books(), [])

    def test_get_list_of_favorites_books(self):
        self.collector.add_new_book("1984")
        self.collector.set_book_genre("1984", "Фантастика")
        self.collector.add_book_in_favorites("1984")
        self.assertEqual(self.collector.get_list_of_favorites_books(), ["1984"])


if __name__ == '__main__':
    unittest.main()
