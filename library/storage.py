import json
from books import Library, Book

class Storage:
    def __init__(self, filename: str = 'library.json') -> None:
        """
        Инициализация класса для работы с файлами.
        """
        self.filename = filename

    def save(self, library: Library) -> None:
        """
        Сохраняет данные библиотеки в файл.
        """
        data = {
            'books': [
                {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'year': book.year,
                    'status': book.status
                } for book in library.books
            ]
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self) -> Library:
        """
        Загружает данные библиотеки из файла.
        """
        library = Library()
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for book_data in data.get('books', []):
                    book = Book(book_data['title'], book_data['author'], book_data['year'], book_data['status'])
                    book.id = book_data['id']
                    library.add_book(book)
        except FileNotFoundError:
            pass  # Если файла нет, создаем пустую библиотеку
        return library
