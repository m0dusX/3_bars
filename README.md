# Ближайшие бары

Данный скрипт находит самый большой и маленький бары из JSON файла и выводит полную информацию о них. Также пользователю предлагается ввести свои координаты (широту и долготу). На их основе скрипт рассчитывает самый ближайший бар к пользователю.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py <path to JSON file>
Пример выходных данных: 

Biggest bars in JSON:
1 bar:
...
<json data>
...

Smallest bars in JSON:
1 bar:
...
<json data>
...

Please enter longitude: <your longitude>
Please enter latitude: <your latitude>

Closest bar was found!
...
<json data>
...

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
