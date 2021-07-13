#!/Users/hrema/Desktop/Python-Data-Science/day03/ex00/hrema/bin/python

import sys
sys.path.insert(0, '/Users/hrema/Desktop/Python-Data-Science/day03/ex03/')
import financial


def test_price_formatting():
	num = financial.price_formatting(35940000000)
	assert num == '35,940,000'

	num = financial.price_formatting(24578000000)
	assert num == '24,578,000'

	num = financial.price_formatting(21461268000)
	assert num == '21,461,268'


def test_str_to_camel_style():
	s = financial.str_to_camel_style('Hello World')
	assert s == 'HelloWorld'

	s = financial.str_to_camel_style('Total Revenue')
	assert s == 'TotalRevenue'

	s = financial.str_to_camel_style('Error')
	assert s == 'Error'


def test_get_price():
	
