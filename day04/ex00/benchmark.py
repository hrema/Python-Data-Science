#!/Users/hrema/.brew/bin/python3

import timeit


def loop(emails):
	'''
	The function creates a new list in a loop with only gmail addresses and returns this list.
	'''
	
	gmail_emails = []
	for i in emails:
		if 'gmail.com' in i:
			gmail_emails.append(i)
	return gmail_emails


def list_comprehension(emails):
	'''
	The function creates a new list using list comprehension only gmail addresses and returns this list.
	'''

	gmail_emails = [i for i in emails if 'gmail.com' in i]
	return gmail_emails


if __name__ == '__main__':
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	
	loop_code = '''loop(emails)'''
	lc_code = '''list_comprehension(emails)'''
	count = 90_000_000
	
	loop_time = timeit.timeit(loop_code, number=count, globals=globals())
	lc_time = timeit.timeit(lc_code, number=count, globals=globals())

	if lc_time <= loop_time:
		print('it is better to use a list comprehension')
	else:
		print('it is better to use a loop')
	
	print(min(lc_time, loop_time), 'vs', max(lc_time, loop_time))
