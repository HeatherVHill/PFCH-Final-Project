import json

import csv

infile = open("Paston_Letters.json","r")
outfile = open("Paston_Letters.csv","w")

writer = csv.writer(outfile)

data = json.loads(infile.read())

writer.writerow(data[0].keys())  # header row

for row in data:
    writer.writerow(row.values())
