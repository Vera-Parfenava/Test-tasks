import json
from typing import List

class Book:
    def __init__(self, title: str, author: str, year: int, status: str = "в наличии") -> None:
        """
        Инициализация книги.
        """
        self.id = None  # id будет присваиваться позже
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.
        """
        return f"ID: {self.id}; Название: {self.title}; Автор: {self.author}; Год: {self.year}; Статус: {self.status}"

class Library:
    def __init__(self) -> None:
        """
        Инициализация библиотеки.
        """
        self.books: List[Book] = []  # Список всех книг
        self.next_id = 1  # Следующий доступный ID для книги

    def add_book(self, book: Book) -> None:
        """
        Добавляет книгу в библиотеку.
        """
        book.id = self.next_id
        self.books.append(book)
        self.next_id += 1

    def remove_book(self, book_id: int) -> bool:
        """
        Удаляет книгу из библиотеки по ID.
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return True
        return False

    def search_books(self, query: str) -> List[Book]:
        """
        Ищет книги по запросу (по названию, автору или году).
        """
        result = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query == str(book.year):
                result.append(book)
        return result

    def display_books(self) -> None:
        """
        Отображает все книги в библиотеке.
        """
        if not self.books:
            print("Нет книг в библиотеке.")
        for book in self.books:
            print(book)

    def change_status(self, book_id: int, status: str) -> bool:
        """
        Изменяет статус книги на 'в наличии' или 'выдана'.
        """
        if status not in ["в наличии", "выдана"]:
            print("Неверный статус. Доступные статусы: 'в наличии', 'выдана'.")
            return False
        for book in self.books:
            if book.id == book_id:
                book.status = status
                return True
        return False

