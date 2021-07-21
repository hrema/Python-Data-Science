#!/Users/hrema/Desktop/Python-Data-Science/day03/ex00/hrema/bin/python


# ----- Program ----- #

from bs4 import BeautifulSoup
import sys
import requests
import re
import json


def price_formatting(price):
	"""
	Takes a float or int price, formats it, and returns the price converted to string.
	"""

	sign = 1
	if price < 0:
		sign = -1
		price *= -1
	price //= 1000
	price = int(price)
	price = list(str(price))
	for i in range(-3, -(len(price) + 1), -4):
		price.insert(i, ',')
	if sign == -1:
		price.insert(0, '-')
	price = ''.join(price)
	return price


def str_to_camel_style(string):
	"""
	Convert string to camel styles. "Hello World" -> "HelloWorld"
	"""

	field_camel = string.split(' ')
	field_camel = [x.replace(x[0], x[0].upper()) for x in field_camel]
	field_camel = ''.join(field_camel)
	return field_camel


def get_price(fundamental_indicators, indicator_field, period, quarter=0):
	"""
	The function takes a table field, formats it camel style.
	Finds the price of this field in a quarter, formats the price, and returns its string representation.
	"""

	if 'Available to' in indicator_field:
		indicator_field = indicator_field.replace('Available to', 'Availto', 1)
	if '&' in indicator_field:
		indicator_field = indicator_field.replace('&', 'And')

	field_camel = str_to_camel_style(indicator_field)

	price = fundamental_indicators.get(period + field_camel)
	if price is None:
		return '-'

	if period == 'trailing' and quarter != 0:
		raise RuntimeError('Wrong quarter')

	if len(price) > 0:
		if price[quarter] is None:
			return '-'
		price = price[quarter]['reportedValue']['raw']
	else:
		return '-'

	if 'EPS' in field_camel:
		return f'{price:.2f}'

	price = price_formatting(price)
	return price


def create_tuple_field(fundamental_indicators, indicator_field):
	list_field = list()
	list_field.append(indicator_field)
	list_field.append(get_price(fundamental_indicators, indicator_field, 'trailing'))
	for i in range(3, -1, -1):
		list_field.append(get_price(fundamental_indicators, indicator_field, 'annual', i))
	return tuple(list_field)


def get_response(ticker_name):
	url = f'https://finance.yahoo.com/quote/{ticker_name}/financials?p={ticker_name}'

	resp = requests.get(url, headers={'User-Agent': 'Custom'})
	if resp.status_code != 200:
		raise RuntimeError(f'Server returned {resp.status_code}')
	if resp.url != url:
		raise RuntimeError('Wrong ticker name')

	return resp


if __name__ == '__main__':
	if len(sys.argv) != 3:
		raise RuntimeError('Wrong number of arguments')

	ticker = sys.argv[1]
	field = sys.argv[2]

	req = get_response(ticker)

	# with open(f'{ticker}.html', 'w') as f:
	# 	f.write(req.text)

	# time.sleep(5)
	soup = BeautifulSoup(req.text, 'html.parser')
	script = soup.find('script', text=re.compile('root.App.main'))
	json_text = re.search(r'\s*root.App.main\s*=\s*({.*?})\s*;\s*$', str(script), flags=re.DOTALL | re.MULTILINE).group(1)
	data_dict = json.loads(json_text)

	# data = json.dumps(data_dict, indent=4)
	# with open(f'{ticker}.json', 'w') as f:
	# 	print(data, file=f)

	quote_time_series_store = data_dict['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']

	# data = json.dumps(quote_time_series_store, indent=4)
	# with open(f'{ticker}_quote_time_series_store.json', 'w') as f:
	# 	print(data, file=f)

	print(create_tuple_field(quote_time_series_store, field))

	# os.remove(f'{ticker}.html')
	# os.remove(f'{ticker}.json')
	# os.remove(f'{ticker}_quote_time_series_store.json')


# ----- Tests ----- #


def test_price_formatting():
	num = price_formatting(35940000000)
	assert num == '35,940,000'

	num = price_formatting(24578000000)
	assert num == '24,578,000'

	num = price_formatting(21461268000)
	assert num == '21,461,268'


def test_str_to_camel_style():
	s = str_to_camel_style('Hello World')
	assert s == 'HelloWorld'

	s = str_to_camel_style('Total Revenue')
	assert s == 'TotalRevenue'

	s = str_to_camel_style('Error')
	assert s == 'Error'


def test_get_price():
	resp = get_response('TSLA')

	bs = BeautifulSoup(resp.text, 'html.parser')
	script_find = bs.find('script', text=re.compile('root.App.main'))
	json_txt = re.search(r'\s*root.App.main\s*=\s*({.*?})\s*;\s*$', str(script_find), flags=re.DOTALL |
																						re.MULTILINE).group(1)

	data = json.loads(json_txt)

	fundamental_indicators = data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']
	indicator_field = "Total Revenue"

	price = get_price(fundamental_indicators, indicator_field, 'trailing')
	assert price == '35,940,000'

	price = get_price(fundamental_indicators, indicator_field, 'annual', 1)
	assert price == '21,461,268'

	price = get_price(fundamental_indicators, indicator_field, 'annual', 2)
	assert price == '24,578,000'


def test_create_tuple_field():
	resp = get_response('TSLA')

	bs = BeautifulSoup(resp.text, 'html.parser')
	script_find = bs.find('script', text=re.compile('root.App.main'))
	json_txt = re.search(r'\s*root.App.main\s*=\s*({.*?})\s*;\s*$', str(script_find), flags=re.DOTALL |
																						re.MULTILINE).group(1)
	data = json.loads(json_txt)

	fundamental_indicators = data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']
	indicator_field = "Total Revenue"

	tuple_field = create_tuple_field(fundamental_indicators, indicator_field)
	assert isinstance(tuple_field, tuple)
	assert tuple_field == ('Total Revenue',	'35,940,000', '31,536,000', '24,578,000', '21,461,268',	'11,758,751')

	indicator_field = "Cost of Revenue"
	tuple_field = create_tuple_field(fundamental_indicators, indicator_field)
	assert tuple_field == ('Cost of Revenue', '28,329,000', '24,906,000', '20,509,000', '17,419,247', '9,536,264')
	

def test_get_response():
	try:
		get_response('TSLA')
	except Exception:
		assert False
	
	try:
		get_response('qwesasfxzc')
	except Exception:
		assert True
	
	try:
		get_response('FB')
	except Exception:
		assert False
