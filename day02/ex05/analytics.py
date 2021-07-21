from random import randint


class Research:
	def __init__(self, file_path):
		self.file_path = file_path
	
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
		def __init__(self, data):
			self.data = data

		def counts(self):
			head = 0
			tail = 0
			for el in self.data:
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

	class Analytics(Calculations):
		def pred_random(self, pred):
			predictions = []
			for i in range(0, pred):
				num = randint(0, 1)
				if num == 1:
					predictions.append([1, 0])
				else:
					predictions.append([0, 1])
				
			return predictions

		def pred_last(self, data):
			return data[-1]

		def save_file(self, data, name, form):
			try:
				with open(f'{name}.{form}', 'w') as f:
					f.write(data)
			except Exception:
				raise RuntimeError('Wrong path of file')
