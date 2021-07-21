#!/Users/hrema/Desktop/Python-Data-Science/day03/ex00/hrema/bin/python

from bs4 import BeautifulSoup
import sys
import requests
import re
import json


def price_formatting(price):
	"""
	Accepts a float or int price, formats it, and returns the price converted to string.
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
	Convert string to camel styles. "Hello World" -> "helloWorld"
	"""

	field_camel = string.split(' ')
	field_camel = [x.replace(x[0], x[0].upper()) for x in field_camel]
	field_camel = ''.join(field_camel)
	return field_camel


def get_price(quote_time_series_store, field, period, quarter=0):
	"""
	The function takes a table field, formats it camel style.
	Finds the price of this field in a quarter, formats the price, and returns its string representation.
	"""

	if 'Available to' in field:
		field = field.replace('Available to', 'Availto', 1)
	if '&' in field:
		field = field.replace('&', 'And')

	field_camel = str_to_camel_style(field)

	price = quote_time_series_store.get(period + field_camel)
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


def main(argv):
	if len(sys.argv) != 3:
		raise RuntimeError('Wrong number of arguments')

	ticker = argv[1]
	field = argv[2]
	url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'

	try:
		req = requests.get(url, headers={'User-Agent': 'Custom'})
		if req.status_code != 200:
			raise RuntimeError(f'Server ruterned {req.status_code}')
		if req.url != url:
			raise RuntimeError('Wrong ticker name')
	except Exception:
		raise

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

	list_field = list()
	list_field.append(field)
	list_field.append(get_price(quote_time_series_store, field, 'trailing'))
	for i in range(3, -1, -1):
		list_field.append(get_price(quote_time_series_store, field, 'annual', i))
	print(tuple(list_field))

	# os.remove(f'{ticker}.html')
	# os.remove(f'{ticker}.json')
	# os.remove(f'{ticker}_quote_time_series_store.json')


if __name__ == '__main__':
	main(sys.argv)
