import csv

csvfile = open('DATASET.TXT', 'r').readlines()
new_file = open('new_dataset.txt', 'a')
new_data = []

for line in csvfile:
    new_data.append(line.split(";"))

for element in new_data:
    for line in element:
        if line.rstrip():
            new_file.write(line + '\n')
