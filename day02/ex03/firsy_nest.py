import sys


class Research:
	def __init__(self, path_to_the_file):
		self.file_path = path_to_the_file
	
	def file_reader(self, has_header=True):
		try:
			with open(self.file_path) as f:
				lines = f.readlines()
			
			if len(lines) < 2:
				raise Exception
			
			res = []
			if has_header:
				lines_without_header = lines[1:]
			else:
				lines_without_header = lines

			lines_strip = [x.strip() for x in lines_without_header]
			for line in lines_strip:
				line_split = line.split(',')
				if len(line_split) != 2:
					raise Exception
				line_split = [int(x) for x in line_split]
				res.append(line_split)
			
			return res

		except Exception:
			return 'Wrong struct to file'

	class Calculations:
		def counts(self, list_of_lists):
			head = 0
			tail = 0
			for el in list_of_lists:
				if el[0] == 1:
					head += 1
				else:
					tail += 1
			
			return head, tail
		
		def fractions(self, head_and_tail):
			summa = head_and_tail[0] + head_and_tail[1]
			head_percent = (head_and_tail[0] / summa) * 100
			tail_percent = (head_and_tail[1] / summa) * 100
			return head_percent, tail_percent


if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise RuntimeError('Wrong number of arguments')
	
	file_path = sys.argv[1]

	r = Research(file_path)
	data = r.file_reader()
	print(data)

	calc = r.Calculations()
	counts = calc.counts(data)
	print(counts[0], counts[1])

	fractions = calc.fractions(counts)
	print(fractions[0], fractions[1])
