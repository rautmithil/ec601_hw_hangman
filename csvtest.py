import csv

f = open('macities.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print(row)

f.close()
