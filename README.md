# qa_python

## test_add_new_book_add_two_books_positive_result
	Добавление книг. Метод возвращает корректную длину словаря

## test_add_new_book_invalid_name_dictionary_is_empty
	Обработка исключений. Добавление книг с невалидными именами

## test_set_book_genre_added_book_has_no_genre_genre_is_empty
	Добавление книги без указания жанра. Вывод пустой

## test_set_book_genre_added_book_with_genre_positive_result
	Добавление книги с указанием жанра. Метод возвращает корректный жанр

## test_set_book_genre_book_is_not_on_the_list_genre_is_none
	Жанр не устанавливается книге, не добавленной в словарь

## test_get_books_with_specific_genre_add_two_books_with_different_genres_one_book_as_a_result
	Вывод книги с заданным жанром при добавлении в словарь нескольких книг с разными жанрами
	Вывод содержит только ту книгу, жанр которой запрашивался

## test_add_book_in_favorites_add_book_positive_result
	Добавление книги в список избранных

## test_delete_book_from_favorites_delete_book_positive_result
	Удаление книги из списка избранных

## test_get_list_of_favorites_books_empty
	По умолчанию список избраннных книг пуст 

## test_get_books_for_children_add_some_books_and_check_list_for_children_positive_result
	Книги с возрастным рейтингом отсутствуют в списке книг для детей

