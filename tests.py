import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_positive_result(self, collector):

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_invalid_name_dictionary_is_empty(self, collector):

        # Пытаемся добавить книги с невалидными именами: пустым именем и именем длиннее 40 символов
        collector.add_new_book('')
        collector.add_new_book('A' * 41)

        # Проверяем, что книга не добавится в словарь
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_added_book_has_no_genre_genre_is_empty(self, collector):
        collector.add_new_book('1984')

        # Проверяем, что у добавленной книги нет жанра
        assert collector.get_book_genre('1984') == ''

    def test_set_book_genre_added_book_with_genre_positive_result(self, collector):

        # Добавляем книгу в словарь, задаем жанр, входящий в список genre
        collector.add_new_book('Рассказы о Шерлоке Холмсе')
        collector.set_book_genre('Рассказы о Шерлоке Холмсе', 'Детективы')

        # с помощью метода get_book_genre проверяем, что жанр верный
        assert collector.get_book_genre('Рассказы о Шерлоке Холмсе') == 'Детективы'

    def test_set_book_genre_book_is_not_on_the_list_genre_is_none(self, collector):

        # Пытаемся задать жанр книге, не добавленной в список книг
        collector.set_book_genre('Неизвестная книга', 'Мультфильмы')

        # Проверяем, что жанр не установился
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre_add_two_books_with_different_genres_one_book_as_a_result(self, collector):
        # добавляем 2 книги, указав жанр
        collector.add_new_book('Двенадцать стульев')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        # вызываем метод get_books_with_specific_genre только для комедии
        comedy_book = collector.get_books_with_specific_genre('Комедии')

        # Проверяем, что в выводе будет только 1 фильм: Двенадцать стульев
        assert comedy_book == ['Двенадцать стульев']

    def test_add_book_in_favorites_add_book_positive_result(self, collector):
        # Добавляем новую книгу, затем добавляем в список избранных
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')

        # Проверяем, что книга есть в списке избранных
        assert '1984' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book_positive_result(self, collector):
        # Добавляем новую книгу, затем добавляем в список избранных
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        # Удаляем книгу из избранных
        collector.delete_book_from_favorites('1984')

        # проверяем, что книги нет в списке избранных
        assert '1984' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_list_is_empty_by_default(self, collector):
        # Проверяем, что список избранных пуст по умолчанию
        assert collector.get_list_of_favorites_books() == []

    # Передали в декоратор тестовые данные для проверки определения книг для детей
    @pytest.mark.parametrize(
        "books_and_genres, expected_children_books",
        [
            ({'Дюна': 'Фантастика', 'Дракула': 'Ужасы'}, ['Дюна']),  # Подходит только Дюна
            ({'Красная шапочка': 'Мультфильмы', 'Рождество Эркюля Пуаро': 'Детективы', 'Дневник Бриджит Джонс': 'Комедии'}, ['Красная шапочка', 'Дневник Бриджит Джонс'])  # Рождество Эркюля Пуаро не подходит
        ]
    )
    def test_get_books_for_children_add_some_books_and_check_list_for_children_positive_result(self, collector, books_and_genres, expected_children_books):
        # Передаем параметры декоратора в функцию
        for name, genre in books_and_genres.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        result = collector.get_books_for_children()

        # Проверяем, что в списке только книги для детей
        assert result == expected_children_books
