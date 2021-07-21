#!/Users/hrema/.brew/bin/python3

import timeit


def loop(emails_list):
	"""
	The function creates a new list in a loop.
	New list contain only gmail addresses.
	Function returns new list.
	"""
	
	gmail_emails = []
	for i in emails_list:
		if 'gmail.com' in i:
			gmail_emails.append(i)
	return gmail_emails


def list_comprehension(emails_list):
	"""
	The function creates a new list using list comprehension.
	New list contain only gmail addresses.
	Function returns new list.
	"""

	gmail_emails = [i for i in emails_list if 'gmail.com' in i]
	return gmail_emails


def func_map(emails_list):
	"""
	The function creates a new iterator using function map().
	New iterator contain only gmail addresses.
	Function returns new iterator.
	"""

	gmail_emails = map(lambda x: x if 'gmail.com' in x else None, emails_list)
	return gmail_emails
	

if __name__ == '__main__':
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

	loop_code = '''loop(emails)'''
	lc_code = '''list_comprehension(emails)'''
	lc_func_map = '''func_map(emails)'''
	count = 90_000_000

	time = []
	loop_time = timeit.timeit(loop_code, number=count, globals=globals())
	time.append(loop_time)
	lc_time = timeit.timeit(lc_code, number=count, globals=globals())
	time.append(lc_time)
	lc_func_map = timeit.timeit(lc_func_map, number=count, globals=globals())
	time.append(lc_func_map)

	sort_time = sorted(time)
	min_time = sort_time[0]

	if min_time == loop_time:
		print('it is better to use a loop')
	elif min_time == lc_time:
		print('it is better to use a list comprehension')
	elif min_time == lc_func_map:
		print('it is better to use a map')

	len_sort_time = len(sort_time)
	for t in range(len_sort_time):
		print(sort_time[t], end='')
		if t + 1 != len_sort_time:
			print(' vs ', end='')
	print()
