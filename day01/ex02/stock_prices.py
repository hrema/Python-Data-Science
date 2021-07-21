import sys


def print_price_company(company):
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

	COMPANIES_lower_key = {k.lower(): v for k, v in COMPANIES.items()}
	company_lower = company.lower()
	if company_lower not in COMPANIES_lower_key.keys():
		print('Unknown company')
		return
	else:
		ticker = COMPANIES_lower_key[company_lower]
		print(STOCKS[ticker])


if __name__ == '__main__':
	if len(sys.argv) == 2:
		print_price_company(sys.argv[1])
