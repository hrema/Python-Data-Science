def	sort_dict():
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

	dict_from_list = dict(list_of_tuples)
	sorted_tuple = sorted(dict_from_list.items(), key=lambda item: (-int(item[1]), item[0]))
	sorted_dict_from_list = {k: v for k, v in sorted_tuple}
	for k in sorted_dict_from_list.keys():
		print(k)
	

if __name__ == '__main__':
	sort_dict()