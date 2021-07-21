def typeof(var):
	if isinstance(var, bool):
		return 'bool'
	if isinstance(var, int):
		return 'int'
	if isinstance(var, str):
		return 'str'
	if isinstance(var, float):
		return 'float'
	if isinstance(var, list):
		return 'list'
	if isinstance(var, dict):
		return 'dict'
	if isinstance(var, tuple):
		return 'tuple'
	if isinstance(var, set):
		return 'set'


def data_types():
	var_list = [1, 'Hello', 4.21, True, [1, 2, 3], {'name': 'Alexander'}, (1, 4.21), {1, 2, 3}]
	types_list = list(map(typeof, var_list))
	print('[', ', '.join(types_list), ']', sep='')


if __name__ == '__main__':
	data_types()
