# Введение в ООП Python

ex00: Необходимо создать класс, который будет читать и выводить на консоль содержимое файл data.csv.

ex01: Необходимо тело класса из предыдущего упражнения перенести в метод file_reader(), который возвращает содержимое файла data.scv

ex02: Необходимо создать класс, конструктор которого принимает путь к файлу. Метод класса file_reader() читает файл, который был передан в конструктор, проверяет его на правильность структуры и возвращает его содержимое.

ex03: Требуется создать вложенный класс Calculations, у которого будет два метода counts() и fractions(). Функция file_reader() возвращает данные из файла data.csv без заголовка в формате список списков. Counts() принимает результат работы функци file_reader() и возвращает количество head и tail. Fractions() возвращает процентное соотношение head и tail, полученных функцией counts().

ex04: Требуется написать класс Analytics, который наследуется от Calculations, с двумя методами: pred_random() и pred_last(). Pred_random() принимает число, равное количеству пердсказаний которое она вернет. Pred_last() возвращает последний элемент данных, которые вернула file_reader().

ex05: Нужно перенести всю логику в файл make_report.py, в файле config.py должна лежать шаблонная строка и параметр количества предсказаний. Все классы из предыдущего упражнения должны лежать в файле analytics.py.

# Использованные ресурсы:
https://python-scripts.com/python-class
https://pythonru.com/osnovy/obrabotka-iskljuchenij-python-blok-try-except-blok-finally
https://www.geeksforgeeks.org/inner-class-in-python/
https://shultais.education/blog/python-f-strings
https://stackoverflow.com/questions/42497625/how-to-postpone-defer-the-evaluation-of-f-strings
https://ru.stackoverflow.com/questions/414593/
https://gist.github.com/devStepsize/b1b795309a217d24566dcc0ad136f784
