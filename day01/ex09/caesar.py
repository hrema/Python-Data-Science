import sys


def decode_symbol(c, shift_number):
	new_c = ord(c) + shift_number
	if (ord(c) >= ord('A')) and (ord(c) <= ord('Z')):
		if new_c > ord('Z'):
			new_c = ord('A') + (new_c % ord('Z') - 1)
	elif (ord(c) >= ord('a')) and (ord(c) <= ord('z')):
		if new_c > ord('z'):
			new_c = ord('a') + (new_c % ord('z') - 1)
	else:
		new_c = ord(c)
	return chr(new_c)


def encode_symbol(c, shift_number):
	new_c = ord(c) - shift_number
	if (ord(c) >= ord('A')) and (ord(c) <= ord('Z')):
		if new_c < ord('A'):
			new_c = ord('Z') - (ord('A') - new_c - 1)
	elif (ord(c) >= ord('a')) and (ord(c) <= ord('z')):
		if new_c < ord('a'):
			new_c = ord('z') - (ord('a') - new_c - 1)
	else:
		new_c = ord(c)
	return chr(new_c)


def is_ascii(s):
	return all(ord(c) < 128 for c in s)


if __name__ == '__main__':
	if len(sys.argv) != 4:
		raise RuntimeError('Wrong number of arguments')
	
	task = sys.argv[1]
	string = sys.argv[2]
	shift = int(sys.argv[3])
	
	if not (task == 'encode' or task == 'decode'):
		raise RuntimeError('Wrong task')
	if not is_ascii(string):
		raise RuntimeError('String is not ascii')

	caesar_list = []
	if task == 'encode':
		for symbol in string:
			new_symbol = decode_symbol(symbol, shift)
			caesar_list.append(new_symbol)
	else:
		for symbol in string:
			new_symbol = encode_symbol(symbol, shift)
			caesar_list.append(new_symbol)

	caesar_string = ''.join(caesar_list)
	print(caesar_string)
