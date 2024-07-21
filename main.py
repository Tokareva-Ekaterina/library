from library import Library, Book


def print_menu() -> None:
    """
    Выводит меню для пользователя
    """

    print('\nВведите номер одной из команд:')
    print('1. Добавить книгу')
    print('2. Удалить книгу')
    print('3. Найти книгу')
    print('4. Отобразить все книги')
    print('5. Изменить статус книги')
    print('6. Выход')


def add_book(library: Library) -> None:
    """
    Обрабатывает пользовательский ввод и добавляет соответствующую книгу

    :param library: экземпляр класса Library
    """

    title = input('Введите название книги: ').strip()
    author = input('Введите автора книги: ').strip()
    try:
        year = int(input('Введите год издания: '))
        library.add_book(Book(title, author, year))
    except:
        print('Год должен быть целым числом')


def del_book(library: Library) -> None:
    """
    Обрабатывает пользовательский ввод и удаляет соответствующую книгу

    :param library: экземпляр класса Library
    """

    try:
        id_book = int(input('Введите id книги: '))
        library.del_book(id_book)
    except:
        print('id должен быть целым числом')


def search_book(library: Library) -> None:
    """
    Обрабатывает пользовательский ввод и ищет соответствующиие книги

    :param library: экземпляр класса Library
    """

    print('Книгу можно искать по названию, автору или году')
    key = input('Введите одну из команд: title, author, year\n').strip().lower()
    if key not in ('title', 'author', 'year'):
        print('Неверная команда')
    else:
        value = input(f'Введите значение для поиска по полю {key}\n').strip()
        try:
            if key == 'year':
                value = int(value)
            library.search_book(key, value)
        except:
            print('Год должен быть целым числом')


def show_books(library: Library) -> None:
    """
    Выводит все книги

    :param library: экземпляр класса Library
    """

    library.show_books()


def change_status(library: Library) -> None:
    """
    Обрабатывает пользовательский ввод и изменяет статус соответствующей книги

    :param library: экземпляр класса Library
    """

    try:
        id_book = int(input('Введите id книги: '))
        status = input('Введите статус книги (в наличии, выдана): ').strip().lower()
        if status not in ('в наличии', 'выдана'):
            print('Некорректный статус')
        else:
            library.change_status(id_book, status)
    except:
        print('id должен быть целым числом')


lib = Library()
print('Добро пожаловать в систему управления библиотекой!')
option = 0
while True:
    print_menu()
    try:
        option = int(input('\nКоманда: '))
    except:
        option = 0

    if option == 1:
        add_book(lib)
    elif option == 2:
        del_book(lib)
    elif option == 3:
        search_book(lib)
    elif option == 4:
        show_books(lib)
    elif option == 5:
        change_status(lib)
    elif option == 6:
        break
    else:
        print('Неверная команда')
