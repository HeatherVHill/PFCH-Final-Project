import json

import csv

infile = open("Paston_Letters.json","r")
outfile = open("Paston_Letters2.csv","w")

writer = csv.writer(outfile)

for row in json.loads(infile.read()):
    writer.writerow(row)
