import unittest

from books import Library, Book
from storage import Storage

class TestLibrary(unittest.TestCase):
    
    def setUp(self):
        """Подготовка библиотеки для тестов"""
        self.library = Library()
        self.book1 = Book("Война и мир", "Лев Толстой", 1863)
        self.book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1928)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        """Тестирование добавления книги"""
        book3 = Book("Братья Карамазовы", "Федор Достоевский", 1878)
        self.library.add_book(book3)
        self.assertEqual(len(self.library.books), 3)
        self.assertEqual(self.library.books[-1].title, "Братья Карамазовы")

    def test_remove_book(self):
        """Тестирование удаления книги"""
        result = self.library.remove_book(self.book1.id)
        self.assertTrue(result)
        self.assertEqual(len(self.library.books), 1)

    def test_remove_book_not_found(self):
        """Тестирование удаления несуществующей книги"""
        result = self.library.remove_book(2000)
        self.assertFalse(result)

    def test_search_books(self):
        """Тестирование поиска книги"""
        results = self.library.search_books("Лев Толстой")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Война и мир")

    def test_change_status(self):
        """Тестирование изменения статуса книги"""
        self.library.change_status(self.book1.id, "выдана")
        self.assertEqual(self.book1.status, "выдана")

    def test_invalid_status(self):
        """Тестирование попытки изменить статус на неправильный"""
        result = self.library.change_status(self.book1.id, "неизвестно")
        self.assertFalse(result)

    def test_save_load(self):
        """Тестирование сохранения и загрузки библиотеки"""
        storage = Storage("test_library.json")
        storage.save(self.library)
        loaded_library = storage.load()
        self.assertEqual(len(loaded_library.books), 2)
        self.assertEqual(loaded_library.books[0].title, "Война и мир")

if __name__ == "__main__":
    unittest.main()
