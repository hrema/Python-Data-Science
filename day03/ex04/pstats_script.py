#!/Users/hrema/Desktop/Python-Data-Science/day03/ex00/hrema/bin/python

import os
import pstats
import sys
import cProfile


if __name__ == '__main__':
	if len(sys.argv) != 3:
		raise RuntimeError('Wrong number of arguments')

	cProfile.run(f'financial.main({sys.argv})', filename='tmp')

	with open('pstats-cumulative.txt', 'w') as f:
		p = pstats.Stats('tmp', stream=f)
		p.strip_dirs().sort_stats('cumtime').print_stats()

	os.remove('tmp')
