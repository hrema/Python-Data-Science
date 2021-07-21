#!/Users/hrema/.brew/bin/python3

import sys
import os
import psutil


def read_file(filename):
	f = open(filename)
	for line in f:
		yield line
	f.close()


if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise RuntimeError('Wrong number of arguments')
	
	gen = read_file(sys.argv[1])

	for g in gen:
		pass

	process = psutil.Process(os.getpid())
	peak_memory = process.memory_info()[0] / (1024 * 1024 * 1024)
	user_time = process.cpu_times()[0]
	system_time = process.cpu_times()[1]

	print(f'Peak Memory Usage = {peak_memory:.3f} GB')
	print(f'User Mode Time + System Mode Time = {user_time + system_time:.2f}s')
