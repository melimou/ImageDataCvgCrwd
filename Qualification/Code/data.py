import csv
from random import shuffle


class Data:
    def __init__(self, filename):
        self.filename = filename

    def dataset_init(self):
        dataset = []
        with open(self.filename, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for line in reader:
                dataset.append(line[0]+'.jpeg')
        return dataset


#test

# data = Data('data.csv').dataset_init()
# shuffle(data)
# print(data)
