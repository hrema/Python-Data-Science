#!/Users/hrema/.brew/bin/python3

import collections
import timeit
import random


def my_counter(num_list):
	"""
	The function creates a dictionary in which the keys are numbers,
	and the values are their number in the list.
	"""

	counter = dict()

	for num in num_list:
		if num in counter:
			counter[num] += 1
		else:
			counter[num] = 0
	
	return counter


def top10_in_my_counter(num_list):
	"""
	Function returns the top 10 most common numbers
	where the keys are the numbers and
	the values are the counts,
	the input is the list.
	"""

	counter = my_counter(num_list)
	list_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
	top10_list_counter = dict(list_counter[:10])
	return top10_list_counter


def std_counter(num_list):
	"""
	The function creates a Counter object from a list and returns it.
	"""
	
	c = collections.Counter(num_list)
	return c


def top10_in_std_counter(num_list):
	"""
	The function creates a Counter object from a list and returns top 10 most common numbers.
	"""

	c = collections.Counter(num_list)
	top10 = c.most_common(10)
	return top10


if __name__ == '__main__':
	random_num_list = [random.randint(0, 100) for _ in range(1_000_000)]

	str_my_counter = '''my_counter(random_num_list)'''
	str_top10_in_my_counter = '''top10_in_my_counter(random_num_list)'''
	str_std_counter = '''std_counter(random_num_list)'''
	str_top10_in_std_counter = '''top10_in_std_counter(random_num_list)'''

	time_my_counter = timeit.timeit(str_my_counter, number=1, globals=globals())
	print(f'my function: {time_my_counter}')
	time_std_counter = timeit.timeit(str_std_counter, number=1, globals=globals())
	print(f'Counter: {time_std_counter}')
	time_top10_in_my_counter = timeit.timeit(str_top10_in_my_counter, number=1, globals=globals())
	print(f'my top: {time_top10_in_my_counter}')
	time_top10_in_std_counter = timeit.timeit(str_top10_in_std_counter, number=1, globals=globals())
	print(f"Counter's top: {time_top10_in_std_counter}")
