import sys

def	get_prices(name_company):
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

	COMPANIES_with_lower_key = {k.lower(): v for k, v in COMPANIES.items()}
	name_company = name_company.lower()
	if name_company not in COMPANIES_with_lower_key.keys():
		print("Unknown company")
		return
	else:
		ticker = COMPANIES_with_lower_key[name_company]
		print(STOCKS[ticker])

if __name__ == "__main__":
	if (len(sys.argv) == 2):
		get_prices(sys.argv[1])
