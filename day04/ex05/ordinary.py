#!/Users/hrema/.brew/bin/python3

import sys
import psutil
import os


def read_file(filename):
	with open(filename) as f:
		lines_from_f = f.readlines()
	
	return lines_from_f


if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise RuntimeError('Wrong number of arguments')
	
	lines = read_file(sys.argv[1])

	for line in lines:
		pass

	process = psutil.Process(os.getpid())
	peak_memory = process.memory_info()[0] / (1024 * 1024 * 1024)
	user_time = process.cpu_times()[0]
	system_time = process.cpu_times()[1]

	print(f'Peak Memory Usage = {peak_memory:.3f} GB')
	print(f'User Mode Time + System Mode Time = {user_time + system_time:.2f}s')
