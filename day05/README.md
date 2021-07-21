# Pandas: работа с Dataframes

## ex00:
1) Нужно считать данные из файла data/feed-views.py функцией read_csv, удалить строки с индексом 2 и 3, и последние 
   2 строчки, установить имена столбцов (datetime, name), установить datetime в качестве столбца индекса.


2) Переименовать datetime в date_time.


3) Сохранить DataFrame в файл data/feed-views-semicolon.log, используя ';' в качестве разделителя.

## ex01:
1) Считать данные из файла ../data/feed-views.log. Присвоить столбцам имена: datetime и name. Преобразовать столбец 
   datetime в datetime64 [ns]. Извлечь год, месяц, день, час, минуту и секунду из значений этого столбца в новые 
   столбцы.


2) Создать новый столбец 'daytime'. Необходимо назначить конкретное время дня, если 'hour' находится в пределах 
   определенного интервала. Назначить индексом столбец 'user'.


3) Рассчитать кол-во элементов в DataFrame. Рассчитать кол-во элементов в категории для каждого времени суток.


4) Рассчитать максимальный 'hour' для 'daytime' == 'evening'. Рассчитать минимальный 'hour' для 'daytime' == 
   'morning'. Посчитать моду для 'hour' и 'daytime'.
   

5) Показать 3 первых 'hour' для 'morning' и 3 последних 'hour' с помощью nsmallest() и nlargest().


6) Вычислить межквартильный размах для 'hour'.

# Использованные ресурсы:

https://thispointer.com/pandas-skip-rows-while-reading-csv-file-to-a-dataframe-using-read_csv-in-python/

https://pandas.pydata.org/docs/index.html

https://www.codegrepper.com/code-examples/python/extract+month+from+datetime+pandas

https://stackoverflow.com/questions/45751390/pandas-how-to-use-pd-cut

https://www.geeksforgeeks.org/split-a-text-column-into-two-columns-in-pandas-dataframe/
