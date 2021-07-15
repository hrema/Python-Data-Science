#!/Users/hrema/.brew/bin/python3

import timeit
import sys


def func_loop(emails):
	'''
	The function creates a new list in a loop.
	New list contain only gmail addresses.
	Function returns new list.
	'''
	
	gmail_emails = []
	for i in emails:
		if 'gmail.com' in i:
			gmail_emails.append(i)
	return gmail_emails


def func_list_comprehension(emails):
	'''
	The function creates a new list using list comprehension.
	New list contain only gmail addresses.
	Function returns new list.
	'''

	gmail_emails = [i for i in emails if 'gmail.com' in i]
	return gmail_emails


def	func_map(emails):
	'''
	The function creates a new list using function map().
	New list contain only gmail addresses.
	Function returns new list.
	'''

	gmail_emails = map(lambda x: x if 'gmail.com' in x else None, emails)
	return gmail_emails


def	func_filter(emails):
	gmail_emails = filter(lambda x: x if 'gmail.com' in x else None, emails)
	return gmail_emails


if __name__ == '__main__':
	if len(sys.argv) != 3:
		exit(1)

	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

	func = 'func_' + sys.argv[1]
	count = int(sys.argv[2])
	str_code = f'''{func}(emails)'''

	time = timeit.timeit(str_code, number=count, globals=globals())
	print(time)
