import sys
from random import randint


class Research:
    def __init__(self, path_to_the_file):
        self.file_path = path_to_the_file

    def file_reader(self, has_header=True):
        try:
            with open(self.file_path) as f:
                lines = f.readlines()

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
            return 'Wrong struct to file'

    class Calculations:
        def __init__(self, data_from_file):
            self.data = data_from_file

        def counts(self):
            head = 0
            tail = 0
            for el in self.data:
                if el[0] == 1:
                    head += 1
                else:
                    tail += 1

            return head, tail

        def fractions(self, head_and_tail):
            summa = head_and_tail[0] + head_and_tail[1]
            head_percent = (head_and_tail[0] / summa) * 100
            tail_percent = (head_and_tail[1] / summa) * 100
            return head_percent, tail_percent

    class Analytics(Calculations):
        def pred_random(self, pred):
            predictions = []
            for i in range(0, pred):
                num = randint(0, 1)
                if num == 1:
                    predictions.append([1, 0])
                else:
                    predictions.append([0, 1])

            return predictions

        def pred_last(self, data_from_file):
            return data_from_file[-1]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise RuntimeError('Wrong number of arguments')

    file_path = sys.argv[1]

    r = Research(file_path)
    data = r.file_reader()
    print(data)

    calc = r.Calculations(data)
    counts = calc.counts()
    print(counts[0], counts[1])

    fractions = calc.fractions(counts)
    print(fractions[0], fractions[1])

    anlt = r.Analytics(data)
    print(anlt.pred_random(3))
    print(anlt.pred_last(data))
