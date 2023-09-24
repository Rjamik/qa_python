import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()


def test_add_new_books(collector):
    collector.add_new_book("Мастер и Маргарита")
    assert collector.books_genre == {"Мастер и Маргарита": ""}
    collector.add_new_book("1984")
    assert collector.books_genre == {"Мастер и Маргарита": "", "1984": ""}
    collector.add_new_book("Мальчик, который поймал журавля")
    assert collector.books_genre == {"Мастер и Маргарита": "", "1984": "", "Мальчик, который поймал журавля": ""}

def test_set_book_genre(collector):
    collector.add_new_book("Мастер и Маргарита")
    collector.add_new_book("1984")
    collector.set_book_genre("Мастер и Маргарита", "Фантастика")
    assert collector.books_genre == {"Мастер и Маргарита": "Фантастика", "1984": ""}

def test_get_book_genre(collector):
    collector.add_new_book("1984")
    collector.set_book_genre("1984", "Фантастика")
    assert collector.get_book_genre("1984") == "Фантастика"

def test_get_books_with_specific_genre(collector):
    collector.add_new_book("Мастер и Маргарита")
    collector.add_new_book("1984")
    collector.set_book_genre("Мастер и Маргарита", "Фантастика")
    collector.set_book_genre("1984", "Фантастика")
    assert collector.get_books_with_specific_genre("Фантастика") == ["Мастер и Маргарита", "1984"]

def test_get_books_genre(collector):
    collector.add_new_book("Мастер и Маргарита")
    collector.add_new_book("1984")
    collector.set_book_genre("Мастер и Маргарита", "Фантастика")
    assert collector.get_books_genre() == {"Мастер и Маргарита": "Фантастика", "1984": ""}

def test_get_books_for_children(collector):
    collector.add_new_book("Мастер и Маргарита")
    collector.add_new_book("1984")
    collector.set_book_genre("Мастер и Маргарита", "Фантастика")
    collector.set_book_genre("1984", "Детективы")
    assert collector.get_books_for_children() == ["Мастер и Маргарита"]

def test_add_book_in_favorites(collector):
    collector.add_new_book("1984")
    collector.set_book_genre("1984", "Фантастика")
    collector.add_book_in_favorites("1984")
    assert collector.get_list_of_favorites_books() == ["1984"]

def test_delete_book_from_favorites(collector):
    collector.add_new_book("1984")
    collector.set_book_genre("1984", "Фантастика")
    collector.add_book_in_favorites("1984")
    collector.delete_book_from_favorites("1984")
    assert collector.get_list_of_favorites_books() == []

def test_get_list_of_favorites_books(collector):
    collector.add_new_book("1984")
    collector.set_book_genre("1984", "Фантастика")
    collector.add_book_in_favorites("1984")
    assert collector.get_list_of_favorites_books() == ["1984"]
