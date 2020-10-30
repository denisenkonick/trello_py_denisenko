Это мой консольный клиент для Trello!  
trello.py
Trello API https://developer.atlassian.com/cloud/trello/rest/api-group-actions/

Usage 

trello.py
Выводит все колонки нашей доски и их задачи

-create [имя задачи] [имя колонки]
Создает задачу в найденной колонке
API метод Create a new Card: POST /1/cards

-move [имя задачи] [имя колонки]
Перемещает задачу в другую колонку.
API метод Update a Card: PUT /1/cards/{id}

-add_column [имя колонки]
Создает колонку в начале доски
API метод Create a new List: POST /1/lists

