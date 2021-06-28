if __name__ == "__main__":
	with open("ds.csv") as file:
		lines = file.readlines()
	
	for line in range(0, len(lines)):
		tmp = lines[line].split('"')
		for i in range(0, len(tmp)):
			if (i != 5): # пропуск стобца name
				tmp[i] = tmp[i].replace(",", "\t")
		lines[line] = ''.join(tmp)

	with open("ds.tsv", "w") as file:
		file.writelines(lines)
