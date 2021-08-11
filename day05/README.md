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

## ex02
1) Прочитать файл data/auto.csv и сделать 'ID' столбцом индекса.


2) Подсчитать кол-во наблюдений с помощью метода count(). 


3) Отбросить дубликаты, учитывая столбцы: 'CarNumber', 'Make_n_model', 'Fines'


4) Отбросить все столбцы, в которых более 500 пропусков. Заменить все отсутствующие значения в столбце 'Refund' 
   предыдущим значением в этом столбце для этой ячейки. Заменить все отсутствующие значения в столбце 'Fines' на 
   среднее значение этого столбца.
   

5) Используя метод apply разделить столбец 'Make_n_model' на два: 'Make' и 'Model'. Удалить столбец 'Make_n_model'. 
   Сохранить DataFrame в файл data/auto.json.
   
## ex03
1) Прочитать файл data/auto.json и сделать 'CarNumber' столбцом индекса.


2) Сделать несколько выборок по DataFrame.


3) Сделать агрегаты с 'Make' и 'Model'.


4) Сделать агрегаты с 'CarNumber'.

## ex04:
1) Прочитать файл data/auto.json и с помощью pd.options.display.float_format настроить вывод чисел с плавающей запятой.


2) Нужно создать выборку из DataFrame, содержащую 200 наблюдений и объединить ее с DataFrame в новый DataFrame 
   concat_rows.

   
3) Создать Series year, содержащую рандомные числа в диапозоне [1980 - 2019]. Объединить year и concat_rows в новый 
   DataFrame fines.
   

4) Создать Series surname, содержащую фамилии из файла data/surname.json. Создать DataFrame owners с двумя 
   столбцами: 'CarNumber' и 'SURNAME'. Придумать и добавить 5 наблюдений в fines. Удалить 20 наблюдений из owners, 
   придумать и добавить 3 новых. Разными способами объединить fines и owners.
   

5) Создать сводную таблицу из fines.


6) Сохранить fines и owners в одноименные csv файлы.

## ex05:
1) Прочитать файл data/fines.csv.


2) Сравнить скорость работы различных способ прохождения по DataFrame.


3) Сравнить скорость работы различных способов поиска по индексу DataFrame.


4) Понижение числовых типов данных.


5) Замена типа 'object' на 'category'.


6) Очистка памяти исходного DataFrame.


# Использованные ресурсы:

https://thispointer.com/pandas-skip-rows-while-reading-csv-file-to-a-dataframe-using-read_csv-in-python/

https://pandas.pydata.org/docs/index.html

https://www.codegrepper.com/code-examples/python/extract+month+from+datetime+pandas

https://stackoverflow.com/questions/45751390/pandas-how-to-use-pd-cut

https://www.geeksforgeeks.org/split-a-text-column-into-two-columns-in-pandas-dataframe/

https://stackoverflow.com/questions/12096252/use-a-list-of-values-to-select-rows-from-a-pandas-dataframe

https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html

https://newtechaudit.ru/pandas-merge-join-concatenate/

http://dfedorov.spb.ru/pandas/%D0%A1%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D0%B2%20pandas.html

https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6

https://stackoverflow.com/questions/65842209/how-to-downcast-numeric-columns-in-pandas
