def	convert_list_to_map():
	list_of_tuples = [
		('Russia', '25'),
		('France', '132'),
		('Germany', '132'),
		('Spain', '178'),
		('Italy', '162'),
		('Portugal', '17'),
		('Finland', '3'),
		('Hungary', '2'),
		('The Netherlands', '28'),
		('The USA', '610'),
		('The United Kingdom', '95'),
		('China', '83'),
		('Iran', '76'),
		('Turkey', '65'),
		('Belgium', '34'),
		('Canada', '28'),
		('Switzerland', '26'),
		('Brazil', '25'),
		('Austria', '14'),
		('Israel', '12')
	]

	dict_tuples = dict()
	for t in list_of_tuples:
		if t[1] not in dict_tuples.keys():
			dict_tuples[t[1]] = [t[0]]
		else:
			dict_tuples[t[1]].append(t[0])
	
	for key, v in dict_tuples.items():
		if (len(v) > 1):
			for i in v:
				print(key, ":", i)
		else:
			print(key, ":", v[0])

if __name__ == "__main__":
	convert_list_to_map()
