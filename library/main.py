import sys
from books import Library
from storage import Storage
from library_manager import LibraryManager

def main():
    storage = Storage()
    library = storage.load()
    manager = LibraryManager(library, storage)
    manager.show_menu()

if __name__ == "__main__":
    main()



