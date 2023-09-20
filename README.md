1.test_add_new_books:  
  1)Сначала добавляем книгу "Мастер и Маргарита" и проверяем, что её добавили в словарь books_genre. 
  2)Затем добавляем книгу "1984" и проверяем, что она также была добавлена в словарь. 
  3)Наконец, добавляем книгу "Мальчик, который поймал журавля" (41 символ в названии) и проверяем, что она не добавилась в словарь, так как ограничение на длину названия не позволяет этого.


2.test_set_book_genre: 
  1)Добавляем книги "Мастер и Маргарита" и "1984" 
  2)Устанавливаем жанр "Фантастика" для "Мастер и Маргарита". 
  3)Проверяем,что жанр был успешно установлен, и словарь books_genre обновился соответствующим образом.


3.test_get_book_genre: 
  1)Добавляем книгу "1984" с жанром "Фантастика", а затем с помощью данного метода проверяем, что установленный жанр корректно возвращается.


4.test_get_books_with_specific_genre:
  1)Добавляем книги "Мастер и Маргарита" и "1984" с жанром "Фантастика". 
  2)Затем вызываем метод с аргументом "Фантастика" и проверяем, что обе книги возвращаются в результате.

5.test_get_books_genre: 
  1)Добавляем книги "Мастер и Маргарита" и "1984" 
  2)Выставляем жанр "Фантастика" для "Мастер и Маргарита". 
  3)Вызываем метод get_books_genre и проверяем, что он возвращает корректный словарь books_genre.

6.test_get_books_for_children:
  1)Добавляем книги "Мастер и Маргарита" и "1984" с жанрами "Фантастика" и "Детективы" соответственно. 
  2)Затем вызываем метод get_books_for_children и проверяем, что он возвращает список книг, подходящих для детей (в данном случае только "Мастер и Маргарита").

7.test_add_book_in_favorites:
  1)Добавляем книгу "1984" с жанром "Фантастика" 
  2)Она добавляется в список "избранное". 
  3)Вызывается метод get_list_of_favorites_books и проверяется, что список содержит только книгу "1984".

8.test_delete_book_from_favorites: 
  1)Добавляем книгу "1984" с жанром "Фантастика".
  2)Затем  добавляем её в список "избранное". 
  3)Удаляем её из списка "избранное". 
  4)Вызывается метод get_list_of_favorites_books и проверяется, что список избранного пуст.

9.test_get_list_of_favorites_books:
  1)Добавляем книгу "1984" с жанром "Фантастика".
  2)Она добавляется в список "избранное". 
  3)Вызывается метод get_list_of_favorites_books и проверяется, что возвращенный список содержит только книгу "1984".
