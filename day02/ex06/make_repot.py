import sys
import config
import analytics


if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise RuntimeError('Wrong number of arguments')
	
	file_path = sys.argv[1]

	r = analytics.Research(file_path)
	data = r.file_reader()
	print(data)
	
	calc = r.Calculations(data)
	counts = calc.counts()
	print(counts[0], counts[1])

	fractions = calc.fractions(counts)
	print(fractions[0], fractions[1])

	anlt = r.Analytics(data)
	data_pred = anlt.pred_random(config.num_of_steps)

	calc_pred = r.Calculations(data_pred)
	counts_pred = calc_pred.counts()
	
	print(config.string.format(counts[0] + counts[1], counts[1], counts[0], fractions[1], fractions[0],
							config.num_of_steps, counts_pred[1], counts_pred[0]))
	r.send_message_to_slack()
