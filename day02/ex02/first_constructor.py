import sys


class Research:
	def __init__(self, file_path):
		self.file_path = file_path
	
	def file_reader(self):
		try:
			with open(self.file_path) as f:
				lines = f.readlines()
			
			if len(lines) < 2:
				raise Exception
			for line in lines:
				if len(line.split(',')) != 2:
					raise Exception

			return ''.join(lines)
		except Exception:
			return("Wrong struct to file")


if __name__ == "__main__":
	if (len(sys.argv) != 2):
		raise RuntimeError("Wrong number of arguments")
	
	file_path = sys.argv[1]
	r = Research(file_path)
	print(r.file_reader())
