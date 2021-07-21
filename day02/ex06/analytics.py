from random import randint
import logging
import os
import json
import urllib.request


logging.basicConfig(filename='analytics.log', filemode='w', format='%(asctime)s %(message)s', level=logging.DEBUG)


class Research:
	def __init__(self, file_path):
		self.file_path = file_path
		logging.debug('Research.__init__(): success created object')
	
	def file_reader(self, has_header=True):
		try:
			with open(self.file_path) as f:
				lines = f.readlines()
			logging.debug('Research.file_reader(): success readed file')
			if len(lines) < 2:
				raise Exception
			
			res = []
			if has_header:
				lines_without_header = lines[1:]
			else:
				lines_without_header = lines

			lines_strip = [x.strip() for x in lines_without_header]
			for line in lines_strip:
				line_split = line.split(',')
				if len(line_split) != 2:
					raise Exception
				line_split = [int(x) for x in line_split]
				res.append(line_split)
			
			return res

		except Exception:
			logging.debug('Research.file_reader(): failed readed file')
			return 'Wrong struct to file'

	def send_message_to_slack(self):
		webhook_url = 'https://hooks.slack.com/services/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'
		
		if not os.path.isfile('/Users/hrema/Desktop/Python-Data-Science/day02/ex06/analytics.log'):
			msg = 'The report was not created due to an error.'
		else:
			msg = 'The report was created successfully'
		
		slack_data = {'text': msg}
		data = json.dumps(slack_data)
		data = str(data)
		data = data.encode('utf-8')
		req = urllib.request.Request(webhook_url, data=data)
		urllib.request.urlopen(req)

	class Calculations:
		def __init__(self, data):
			self.data = data
			logging.debug('Calculations.__init__(): success created object')

		def counts(self):
			logging.debug('Calculations.counts(): calculating the counts of heads and tails')
			head = 0
			tail = 0
			for el in self.data:
				if el[0] == 1:
					head += 1
				else:
					tail += 1
			
			return head, tail
		
		def fractions(self, head_and_tail):
			logging.debug('Calculations.fractions(): calculating the percentage of heads and tails')
			summa = head_and_tail[0] + head_and_tail[1]
			head_percent = (head_and_tail[0] / summa) * 100
			tail_percent = (head_and_tail[1] / summa) * 100
			return head_percent, tail_percent

	class Analytics(Calculations):
		def pred_random(self, pred):
			logging.debug('Analytics.pred_random(): predicting heads and tails')
			predictions = []
			for i in range(0, pred):
				num = randint(0, 1)
				if num == 1:
					predictions.append([1, 0])
				else:
					predictions.append([0, 1])
				
			return predictions

		def pred_last(self, data):
			logging.debug('Analytics.pred_last(): return last elements')
			return data[-1]

		def save_file(self, data, name, form):
			try:
				with open(f'{name}.{form}', 'w') as f:
					f.write(data)
					logging.debug('Analytics.save_file(): success writed file')
			except Exception:
				logging.debug('Analytics.save_file(): failed writed file')
				raise RuntimeError('Wrong path to file')
