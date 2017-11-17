import requests, json, re, csv

Paston_scrape = json.loads("Paston_Letters.json")

with open("myfile.txt","r") as a_open_file:

    for a_line in a_open_file:
