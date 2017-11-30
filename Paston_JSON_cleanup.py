import requests, json, re, csv

Paston_scrape = json.loads("Paston_Letters.json")

# with open("myfile.txt","r") as a_open_file:
#
#     for a_line in a_open_file:

with open('Paston_Letters.json', 'r+') as f:
    data = json.load(f)
    data['id'] = 134 # <--- add `id` value.

os.remove(filename)
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)


    for entry in Paston_scrape
        a_date = ____
        a_recipient


        try:
