#!/Users/hrema/.brew/bin/python3

import sys
import timeit
from functools import reduce

def	func_loop(number):
	summa = 0

	for i in range(number + 1):
		summa = summa + i * i
	return summa


def func_reduce(number):
	square_list = [i * i for i in range(number + 1)]
	return (reduce(lambda x_prev, x: x_prev + x, square_list))

if __name__ == '__main__':
	if len(sys.argv) != 4:
		raise RuntimeError("Wrong number of arguments")

	func = 'func_' + sys.argv[1]
	count = int(sys.argv[2])
	number = int(sys.argv[3])

	str_code = f'''{func}(number)'''
	time = timeit.timeit(str_code, number=count, globals=globals())
	print(time)
