import sys


def call_center(clients_list, recipients_list):
	clients_set = set(clients_list)
	recipients_set = set(recipients_list)

	required_set = clients_set - recipients_set
	required_list = list(required_set)
	
	return required_list


def potential_clients(clients_list, participants_list):
	clients_set = set(clients_list)
	participants_set = set(participants_list)

	required_set = participants_set - clients_set
	required_list = list(required_set)
	
	return required_list


def loyalty_program(clients_list, participants_list):
	clients_set = set(clients_list)
	participants_set = set(participants_list)

	required_set = clients_set - participants_set
	required_list = list(required_set)
	
	return required_list


if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise RuntimeError('Wrong number of arguments')
	task = sys.argv[1]
	tasks = ['call_center', 'potential_clients', 'loyalty_program']
	if task not in tasks:
		raise RuntimeError('Wrong task')

	clients = [
		'andrew@gmail.com',
		'jessica@gmail.com',
		'ted@mosby.com',
		'john@snow.is',
		'bill_gates@live.com',
		'mark@facebook.com',
		'elon@paypal.com',
		'jessica@gmail.com'
	]

	participants = [
		'walter@heisenberg.com',
		'vasily@mail.ru',
		'pinkman@yo.org',
		'jessica@gmail.com',
		'elon@paypal.com',
		'pinkman@yo.org',
		'mr@robot.gov',
		'eleven@yahoo.com'
	]
	
	recipients = [
		'andrew@gmail.com',
		'jessica@gmail.com',
		'john@snow.is'
	]

	required_list = []
	if task == 'call_center':
		required_list = call_center(clients, recipients)
	elif task == 'potential_clients':
		required_list = potential_clients(clients, participants)
	else:
		required_list = loyalty_program(clients, participants)

	print(required_list)
