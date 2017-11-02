import requests, json

page = requests.get("https://quod.lib.umich.edu/c/cme/Paston/1:2?rgn=div1;view=fulltext")

#print(page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

all_divs = soup.find_all("div", attrs = {"class": "textindentlevelx"})

blank_list = [] #want to make the list beforehand so it doesn't rewrite for every for loop

id_counter=1

for variable in all_divs:
    first_person = variable.find("h2")
    a_writer = first_person.text

    a_person = variable.find("h3")
    a_name = a_person.text

    a_content = variable.find_all("p")
    more_variables=""
    for some_content in a_content:
         more_variables = more_variables + some_content.text

    new_dictionary={"Writer":a_writer,"Recipient":a_name,"Content":more_variables,"Letter ID:":id_counter}
    blank_list.append(new_dictionary)
    id_counter = id_counter + 1
json.dump(blank_list,open("agnes.json","w"),indent=4)
