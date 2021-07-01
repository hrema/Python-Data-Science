class Research:
	def	file_reader(self):
		with open("data.csv") as f:
			return f.read()

if __name__ == "__main__":
	print(Research().file_reader())
