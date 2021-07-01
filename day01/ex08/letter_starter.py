import sys

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		raise RuntimeError("Wrong number of arguments")
	
	email = sys.argv[1]
	filename = "employees.tsv"

	with open(filename) as f:
		lines = f.readlines()
	
	lines_strip = [x.strip() for x in lines]
	info_list = [x.split('\t') for x in lines_strip[1:]]
	
	desired_name = ""
	for info in info_list:
		if (info[2] == email):
			desired_name = info[0]
			break
	
	if (desired_name == ""):
		print("No such this e-mail")
	else:
		print(f'Dear {desired_name}, welcome to our team. '
				'We are sure that it will be a pleasure to work with you. '
				'That’s a precondition for the professionals that our company hires.')
