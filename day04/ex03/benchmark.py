#!/Users/hrema/.brew/bin/python3

import sys
import timeit
from functools import reduce

def	func_loop(number):
	summa = 0

	for i in range(1, number + 1):
		summa = summa + i * i
	return summa


def func_reduce(number):
	summa = reduce(lambda x_prev, x: x_prev + x * x, range(1, number + 1), 0)
	return summa


if __name__ == '__main__':
	if len(sys.argv) != 4:
		raise RuntimeError("Wrong number of arguments")

	func = 'func_' + sys.argv[1]
	count = int(sys.argv[2])
	number = int(sys.argv[3])

	str_code = f'''{func}(number)'''
	time = timeit.timeit(str_code, number=count, globals=globals())
	print(time)
