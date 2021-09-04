# SQL и Pandas

## ex00:
1) Скачать базу данных и сохранить ее в подпапку data.


2) Создать подключение к базе данных с помощью библиотеки sqlite3.


3) Получить схему таблицы pageviews.


4) Получить первые 10 строк таблицы pageviews


5) Gолучить подтаблицу, используя только один запрос, где:
- два столбца (uid, datetime);
- столбец uid содержит только данные пользователя (user_ *);
- сортировк по uid в порядке возрастания;
- столбец индекса - datetime;
- datetime преобразуется в DatetimeIndex;
- имя DataFrame - pageviews;


6) Закрыть соединение с базой данных;

# Использованные ресурсы

https://stackoverflow.com/questions/14308467/convert-text-to-numbers-in-sqlite

https://pandas.pydata.org/docs/reference/frame.html

https://stackoverflow.com/questions/2728999/how-to-get-top-5-records-in-sqlite

https://python-scripts.com/sqlite