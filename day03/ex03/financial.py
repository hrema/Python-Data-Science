#!/Users/hrema/Desktop/test/ex00/hrema/bin/python3

from bs4 import BeautifulSoup
import sys
import requests
import os
import re
import json

def	get_price(field, period, quarterl=0):
	field_camel = field.split(" ")
	field_camel = [x.replace(x[0], x[0].upper()) for x in field_camel]
	if '&' in field_camel:
		index = field_camel.index('&')
		field_camel[index] = "And"
	field_camel = ''.join(field_camel)
	if (period == "trailing"):
		price = quote_time_series_store.get("trailing" + field_camel)
		if (price is None):
			return ('-')
		else:
			if (len(price) > 0):
				price = price[0]["reportedValue"]["raw"]
			else:
				return "-"
	else:
		price = quote_time_series_store.get("annual" + field_camel)
		if price is None:
			return "-"
		else:
			if (len(price) > 0):
				price = price[quarterl]["reportedValue"]["raw"]
			else:
				return "-"

	if "EPS" in field_camel:
		return f"{price:.2f}"
	sign = 1
	if price < 0:
		sign = -1
		price *= -1
	price //= 1000
	price = int(price)
	price = list(str(price))
	for i in range(-3, -(len(price) + 1), -4):
		price.insert(i, ",")
	if sign == -1:
		price.insert(0, '-')
	price = ''.join(price)
	return price


if __name__ == "__main__":
	if len(sys.argv) != 2:
		raise RuntimeError("Wrong numbre of arguments")
	
	ticker = sys.argv[1]
	# field = sys.argv[2]
	url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"

	try:
		req = requests.get(url, headers={'User-Agent': 'Custom'})
		if (req.status_code != 200):
			raise RuntimeError(f"Server ruterned {req.status_code}")
		if (req.url != url):
			raise RuntimeError("Wrong ticker name")
	except Exception:
		raise

	# with open(f"{ticker}.html", "w") as f:
	# 	f.write(req.text)

	soup = BeautifulSoup(req.text, "html.parser")
	script = soup.find('script', text=re.compile("root.App.main"))
	json_text = re.search(r"\s*root.App.main\s*=\s*({.*?})\s*;\s*$", str(script), flags=re.DOTALL | re.MULTILINE).group(1)
	data_dict = json.loads(json_text)

	# data = json.dumps(data_dict, indent=4)
	# with open(f"{ticker}.json", "w") as f:
	# 	print(data, file=f)

	quote_time_series_store = data_dict["context"]["dispatcher"]["stores"]["QuoteTimeSeriesStore"]["timeSeries"]

	data = json.dumps(quote_time_series_store, indent=4)
	with open(f"{ticker}_quote_time_series_store.json", "w") as f:
		print(data, file=f)

	l = [
		"Total Revenue",
		"Operating Revenue",
		"Cost of Revenue",
		"Gross Profit",
		"Operating Expense",
		"Selling General and Administration",
		"Research & Development",
		"Operating Income",
		"Net Non Operating Interest Income Expense",
		"Interest Income Non Operating",
		"Interest Expense Non Operating",
		"Other Income Expense",
		"Other Non Operating Income Expenses",
		"Pretax Income",
		"Tax Provision",
		"Net Income Common Stockholders",
		"Net Income",
		"Net Income Including Noncontrolling Interests",
		"Net Income Continuous Operations",
		"Diluted NI Availto Com Stockholders",
		"Basic EPS",
		"Diluted EPS",
		"Basic Average Shares",
		"Diluted Average Shares",
		"Total Operating Income as Reported",
		"Total Expenses",
		"Net Income from Continuing & Discontinued Operation",
		"Normalized Income",
		"Interest Income",
		"Interest Expense",
		"Net Interest Income",
		"EBIT",
		"EBITDA",
		"Reconciled Cost of Revenue",
		"Reconciled Depreciation",
		"Net Income from Continuing Operation Net Minority Interest",
		"Normalized EBITDA",
		"Tax Rate for Calcs",
		"Tax Effect of Unusual Items",
	]

	for field in l:
		list_field = []
		list_field.append(field)
		list_field.append(get_price(field, "trailing"))
		for i in range(3, -1, -1):
			list_field.append(get_price(field, "annual", i))
		print(tuple(list_field))
	
	# os.remove(f"{ticker}.html")
	# os.remove(f"{ticker}.json")
	# os.remove(f"{ticker}_quote_time_series_store.json")
