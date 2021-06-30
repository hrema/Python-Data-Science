# Задание продполагает написание скриптов sh для загрузки данных из HeadHunter API и дальнейшую их обработку.

ex00: В скрипт аргументом передается название вакансии для запроса curl'ом к HeadHunter API и сохранение ответа с помощью jq в файл hh.json.

ex01: Скрипт преобразует данные из формата json в csv и сохраняет их в файл hh.csv.

ex02: Скрипт сортирует данные из файла hh.csv по дате размещения вакансии и ее id и сохраняет результат в файл hh_sorted.csv.

ex03: Скрипт преобразует данные из колонки "name" файла hh_sorted.csv таким образом, что в колонке остается только позиция (Junior | Middle | Senior). Если позиция не указана - (-). Данные сохраняются в файл hh_position.csv.

ex04: Скрипт сохраняет название позиции и кол-во вакансий по ней в файл hh_uniq_positions.csv.

ex05: partitioner.sh разбивает файл hh_position.csv по датам на одноименные файлы. concatenator.sh собирает файлы в один csv файл.

# Использованные ресурсы:

Серия статей про bash:

https://habr.com/ru/company/ruvds/blog/325522/

https://habr.com/ru/company/ruvds/blog/325928/

https://habr.com/ru/company/ruvds/blog/327530/


Команды bash:

https://losst.ru/komanda-cut-linux

https://losst.ru/komanda-uniq-linux

https://losst.ru/komanda-sort-v-linux

https://losst.ru/gerp-poisk-vnutri-fajlov-v-linux

https://losst.ru/komanda-tail-linux

https://losst.ru/komanda-head-linux

https://losst.ru/kopirovanie-fajlov-v-linux

https://losst.ru/kak-udalit-fajl-cherez-terminal-linux

https://losst.ru/komanda-sed 

https://stedolan.github.io/jq/manual/


Работа с csv файлами в bash:

https://coderoad.ru/10217663/%D0%A0%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0-CSV-%D0%B8-%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D1%82%D0%BE%D0%BB%D0%B1%D1%86%D0%B0-%D0%B2-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D0%B5-%D1%81-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC-bash-sed

https://coderoad.ru/40922219/%D0%9A%D0%B0%D0%BA-%D0%BE%D0%B1%D1%8A%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%82%D1%8C-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8-%D0%B8%D0%B7-csv-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2-%D0%B2-%D0%BE%D0%B4%D0%B8%D0%BD-%D1%84%D0%B0%D0%B9%D0%BB-%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D1%8F-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8-%D0%B7%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B0
