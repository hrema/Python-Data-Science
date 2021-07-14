# Введение в Python: управление пакетами и виртуальная среда

## ex00:
Нужно создать виртуальное окружение с ником в качестве имени и написать скрипт, который будет выводить 'virtual env' этого окружения.

## ex01:
Необходимо установить в виртуальную среду termgraph и с помощью скрипта pies_bars.sh нарисовать график.

ex02: Нужно написать скрипт, который скачает две библиотеки и сохранить все скачанные библиотеки виртуального окружения в файл requirements.txt. Также скрипт архивирует папку виртуального окружения.

ex03: Нужно написать Python скрипт, который в качестве аргумента принимает тикер акции компании и поле таблицы Financials (Income Statement). Скрипт возвращает данные переданного поля (по годам).

ex04: Работа с профайлингом программы с помощью cProfile и pstats.

profiling-sleep.txt содержит результат профилирования financial.py с sleep(5) в коде программы, отсортированный по совокупному времени работы функций.

profiling-tottime.txt содержит результат профилирования financial.py без sleep(5) в коде программы, отсортированный по совокупному времени работы функций.

profiling-http.txt содержит результат профилирования financial-enhanced.py, отличающийся от financial.py исполбзованием urllib.requests, отсортированный по совокупному времени работы функций.

profiling-ncalls.txt содержит результат профилирования financial-enhanced.py, отсортированный по кол-ву вызовов функций.

pstats-cumulative.txt содержит результат работы скрипта pstats_script.py.

ex05: Требуется провести модульное тестирование ex03/financial.py

# Использованные ресурсы:
https://docs.python.org/3/library/venv.html
https://github.com/mkaz/termgraph/blob/main/data/ex4.dat
https://docs.python.org/3/library/os.html
https://pypi.org/project/beautifulsoup4/
https://pypi.org/project/pytest/
https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from
https://janakiev.com/blog/python-shell-commands/
https://www.dummies.com/programming/python/how-to-delete-a-file-in-python/
https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory-in-python
https://overcoder.net/q/388553
https://egorovegor.ru/python-beautifulsoup-scraping/
https://pythonworld.ru/moduli/modul-json.html
https://python-scripts.com/sleep
https://python-scripts.com/cprofile-code-profiling
https://overcoder.net/q/6115/
https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse
https://webformyself.com/python-urllib-request-i-urlopen/
https://docs.python.org/3/library/profile.html
https://progi.pro/kak-importirovat-modul-iz-drugoy-papki-v-python-4937122
https://coderlessons.com/tutorials/python-technologies/uznaite-pytest/pytest-kratkoe-rukovodstvo
