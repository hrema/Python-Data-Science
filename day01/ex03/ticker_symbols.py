import sys


def print_name_and_price(ticker):
	COMPANIES = {
		'Apple': 'AAPL',
		'Microsoft': 'MSFT',
		'Netflix': 'NFLX',
		'Tesla': 'TSLA',
		'Nokia': 'NOK'
		}

	STOCKS = {
		'AAPL': 287.73,
		'MSFT': 173.79,
		'NFLX': 416.90,
		'TSLA': 724.88,
		'NOK': 3.37
		}
	
	STOCKS_lower_key = {key.lower(): v for key, v in STOCKS.items()}
	ticker_lower = ticker.lower()

	# price = ''
	if ticker_lower not in STOCKS_lower_key.keys():
		print('Unknown ticker')
		return
	else:
		price_stock = STOCKS_lower_key[ticker_lower]

	COMPANIES_lower_value = {key: v.lower() for key, v in COMPANIES.items()}
	company = ''
	for key, v in COMPANIES_lower_value.items():
		if v == ticker_lower:
			company = key
			break

	print(company, price_stock)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		print_name_and_price(sys.argv[1])
