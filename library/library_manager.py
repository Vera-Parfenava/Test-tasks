import sys
from books import Library, Book
from storage import Storage
from constants import MENU, ERROR_MESSAGES, PROMPTS, SUCCESS_MESSAGES

class LibraryManager:
    def __init__(self, library: Library, storage: Storage):
        self.library = library
        self.storage = storage

    def get_int_input(self, prompt: str, error_message: str) -> int:
        """ Функция для безопасного ввода числового значения с обработкой ошибок """
        while True:
            user_input = input(prompt)
            try:
                return int(user_input)
            except ValueError:
                print(error_message)

    def handle_add_book(self):
        """ Обрабатывает добавление книги в библиотеку """
        title = input(PROMPTS['title'])
        author = input(PROMPTS['author'])
        year = self.get_int_input(PROMPTS['year'], ERROR_MESSAGES['invalid_year'])
        book = Book(title, author, year)
        self.library.add_book(book)
        print(ERROR_MESSAGES['book_added'].format(title=book.title))

    def handle_remove_book(self):
        """ Обрабатывает удаление книги из библиотеки """
        book_id = self.get_int_input(PROMPTS['id_to_remove'], ERROR_MESSAGES['invalid_id'])
        if self.library.remove_book(book_id):
            print(ERROR_MESSAGES['book_removed'].format(book_id=book_id))
        else:
            print(ERROR_MESSAGES['book_not_found'])

    def handle_search_books(self):
        """ Обрабатывает поиск книг по запросу """
        query = input(PROMPTS['query'])
        results = self.library.search_books(query)
        if results:
            for book in results:
                print(book)
        else:
            print(ERROR_MESSAGES['no_books_found'])

    def handle_display_books(self):
        """ Отображает все книги в библиотеке """
        self.library.display_books()

    def handle_change_status(self):
        """ Обрабатывает изменение статуса книги """
        book_id = self.get_int_input(PROMPTS['id_to_change_status'], ERROR_MESSAGES['invalid_id'])
        status = input(PROMPTS['status'])
        if not self.library.change_status(book_id, status):
            print(ERROR_MESSAGES['book_not_found'])

    def show_menu(self):
        """ Отображает главное меню и обрабатывает выбор пользователя """
        menu = {
            '1': self.handle_add_book,
            '2': self.handle_remove_book,
            '3': self.handle_search_books,
            '4': self.handle_display_books,
            '5': self.handle_change_status,
            '6': self.exit_program
        }

        while True:
            print("\nМеню:")
            for key, value in MENU.items():
                print(f"{key}. {value}")

            choice = input("Выберите действие (1-6): ")

            action = menu.get(choice)
            if action:
                action()
            else:
                print("Неверный выбор, попробуйте снова.")

    def exit_program(self):
        """ Выход из программы и сохранение данных """
        self.storage.save(self.library)
        print(SUCCESS_MESSAGES['save'])
        sys.exit(0)