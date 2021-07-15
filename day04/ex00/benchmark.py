#!/Users/hrema/.brew/bin/python3


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

	gmail_emails = []


if __name__ == '__main__':
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	print(loop(emails))