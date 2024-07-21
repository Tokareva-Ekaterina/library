from __future__ import annotations
import json
import os


class Library:
    path_json = 'library.json'

    def __init__(self) -> None:
        if not os.path.isfile(self.path_json):
            self.save_data({'books': []})

    @classmethod
    def save_data(cls, data: dict) -> None:
        """
        Метод для записи данных в json-файл

        :param data: Словарь с данными
        """

        with open(cls.path_json, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=3)

    @classmethod
    def load_data(cls) -> dict:
        """
        Метод для загрузки данных из json-файла

        :return: Словарь с данными
        """

        with open(cls.path_json) as file:
            data = json.load(file)
            return data

    def add_book(self, book: Book) -> None:
        """
        Добавляет книгу в json-файл

        :param book: экземпляр класса Book
        """

        data = self.load_data()
        data['books'].append(book.__dict__)
        self.save_data(data)
        print('Книга успешно добавлена')

    def del_book(self, id_book: int) -> None:
        """
        Удаляет книгу из json-файла

        :param id_book: id удаляемой книги
        """

        data = self.load_data()
        for item in data['books']:
            if item['id'] == id_book:
                data['books'].remove(item)
                self.save_data(data)
                print('Книга успешно удалена')
                break
        else:
            print('Книги с таким id не существует')

    def change_status(self, id_book: int, status: str) -> None:
        """
        Изменяет статус книги в json-файле

        :param id_book: id книги
        :param status: новый статус
        """

        data = self.load_data()
        for item in data['books']:
            if item['id'] == id_book:
                item['status'] = status
                self.save_data(data)
                print('Статус успешно изменён')
                break
        else:
            print('Книги с таким id не существует')

    @staticmethod
    def __f_str(item: dict) -> str:
        """
        Формирует f-строку с описанием книги

        :param item: Словарь с информацией о книге
        :return: f-строка с описанием книги
        """

        return f"{item['id']}. \"{item['title']}\", {item['author']}, {item['year']} - {item['status']}"

    def show_books(self) -> None:
        """
        Выводит все книги из json-файла
        """

        data = self.load_data()
        print('Список всех книг:')
        for item in data['books']:
            print(self.__f_str(item))

    def search_book(self, key: str, value: str | int) -> None:
        """
        Ищет книги по критерию в json-файле и выводит их

        :param key: один из ключей - title, author, year
        :param value: значение для поиска, соответствующее ключу
        """

        data = self.load_data()
        print('Список найденных книг:')
        for item in data['books']:
            if str(item[key]).lower() == str(value).lower():
                print(self.__f_str(item))


class Book:
    @staticmethod
    def __get_id() -> int:
        """
        Генерирует id для книги

        :return: id книги
        """

        data = Library.load_data()
        if len(data['books']) == 0:
            __id = 1
        else:
            __id = data['books'][-1]['id'] + 1

        return __id

    def __init__(self, title: str, author: str, year: int) -> None:
        self.id = self.__get_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = 'в наличии'
