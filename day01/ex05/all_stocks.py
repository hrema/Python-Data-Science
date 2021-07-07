import sys

def	print_company_and_price(company, COMPANIES, STOCKS):
	COMPANIES_lower_key = {k.lower(): v for k, v in COMPANIES.items()}
	company_lower = company.lower()

	ticker = COMPANIES_lower_key[company_lower]
	for c in COMPANIES.keys():
		if c.lower() == company_lower:
			good_company = c
			break

	print(good_company, 'stock price is', STOCKS[ticker])


def print_ticker_and_company(ticker, COMPANIES):
	COMPANIES_lower_key = {key.lower(): v for key, v in COMPANIES.items()}
	ticker_lower = ticker.lower()

	for key, v in COMPANIES.items():
		if v.lower() == ticker_lower:
			good_ticker = v
			company = key
			break

	print(good_ticker, 'is a ticker symbol for', company)


def	print_info(name):
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
	
	if name.lower() in map(lambda x: x.lower(), COMPANIES.keys()):
		print_company_and_price(name, COMPANIES, STOCKS)
	elif name.lower() in map(lambda x: x.lower(), COMPANIES.values()):
		print_ticker_and_company(name, COMPANIES)
	else:
		print(name, 'is an unknown company or an unknown ticker symbol')

if __name__ == '__main__':
	if len(sys.argv) == 2:
		split_argv = [x.strip() for x in sys.argv[1].split(',')]
		if '' not in split_argv:
			for name in split_argv:
				print_info(name)
