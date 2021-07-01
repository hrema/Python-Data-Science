class Must_read:
	def	read_file(self, file_path):
		with open(file_path) as f:
			print(f.read())

if __name__ == "__main__":
	mr = Must_read()
	mr.read_file("data.csv")
