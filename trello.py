import sys
import requests

# Данные авторизации в API Trello  
auth_params = {
	'key': "d626d78e350d790c25500cf8fe93e424",
	'token': "f03c3260620d95a108fb44e14f85cc4174e84390349b97ed406787d7ac5e70d3"
}

# Адрес, на котором расположен API Trello, # Именно туда мы будем отправлять HTTP запросы.  
base_url = "https://api.trello.com/1/{}"  
board_id = "bT3umroM"

#выводим доп.информацию о выполнении запросов
debug_mode = True

def board_id_long(board_id):
	resp = requests.get(base_url.format('boards') + '/' + board_id, params=auth_params)
	if debug_mode:
		print(f"Status {resp.status_code}: {resp.text}")
	resdata = resp.json()
	if debug_mode:
		print(f"Board long ID: {resdata['id']}")
	return resdata['id']

def read():
	""" Получет данные доски
		Выводит доски и их задачи
	"""

	# Получим данные всех колонок на доске:
	resp = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params)
	
	if debug_mode:
		print(f"Status {resp.status_code}: {resp.text}")
	
	column_data = resp.json()

	# Теперь выведем название каждой колонки и всех заданий, которые к ней относятся:
	for column in column_data:
		col_name = column["name"]
		col_cards = []
		# Получим данные всех задач в колонке и перечислим все названия
		task_data = requests.get(base_url.format('lists')+'/'+column['id']+'/cards', params=auth_params).json()
		
		for task in task_data:
			col_cards.append(task['name'])
					
		print(f"{col_name!r}: {len(col_cards)} items")
		if len(col_cards):
			for card in col_cards:
				print(f"\t {card}")	
		else:
			print('\t'+'Нет задач')

def create(name, column_name):
	"""Создает задачу с произвольным названием в одной из колонок"""

	# Получим данные всех колонок на доске      
	column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()

	# Переберём данные обо всех колонках, пока не найдём ту колонку, которая нам нужна      
	for column in column_data:
		if column['name'] == column_name:
			# Создадим задачу с именем _name_ в найденной колонке      
			resp = requests.post(base_url.format('cards'), data={'name': name, 'idList': column['id'], **auth_params})
			
			if debug_mode:
				print(f"Status {resp.status_code}: {resp.text}")
			
			break


def move(name, column_name):
	# Получим данные всех колонок на доске
	resp = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params)
	column_data = resp.json()
	
	if debug_mode:
		print(f"Status {resp.status_code}: {resp.text}")

	# Среди всех колонок нужно найти задачу по имени и получить её id
	task_id = None
	for column in column_data:
		column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()    
		for task in column_tasks:
			if task['name'] == name:
				task_id = task['id']
				break

	# Теперь, когда у нас есть id задачи, которую мы хотим переместить    
	# Переберём данные обо всех колонках, пока не найдём ту, в которую мы будем перемещать задачу
	for column in column_data:
		if column['name'] == column_name:
			# И выполним запрос к API для перемещения задачи в нужную колонку
			resp = requests.put(base_url.format('cards') + '/' + task_id, data={'idList': column['id'], **auth_params})
			if debug_mode:
				print(f"Status {resp.status_code}: {resp.text}")
			break


def add_column(name=''):
	"""Create a new List on a Board"""
	resp = requests.post(base_url.format('lists'), data={'name': name, 'idBoard': board_id_long(board_id), **auth_params})
	print(f"Status {resp.status_code}: {resp.text}")

if __name__ == "__main__":
	if len(sys.argv) <= 2:
		read()
	elif sys.argv[1] == '-create':
		create(sys.argv[2], sys.argv[3])
	elif sys.argv[1] == '-move':
		move(sys.argv[2], sys.argv[3])
	elif sys.argv[1] == '-add_column':
		add_column(sys.argv[2])
