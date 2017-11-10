# - scrape main page with BS to get list of URLs using the "a" items [href?]

import requests, json, re

home_page = requests.get("http://name.umdl.umich.edu/Paston")

#print(page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(home_page.content, 'html.parser')

Paston_main=[]

Paston_dictionary_list = [] #want to make the list beforehand so it doesn't rewrite for every for loop

letter_id_counter=1

writer = soup.find_all("a", href=re.compile("rgn=div2"))

for variable in writer:
     Paston_main.append(variable.attrs["href"])

for individual_link in Paston_main:
    link_request = requests.get(individual_link)
    link_request_content = BeautifulSoup(link_request.content,'html.parser')
    all_divs = link_request_content.find_all("div", attrs = {"class": "textindentlevelx"})

    for new_variable in all_divs:
        # first_person = variable.find("h2")
        # a_writer = first_person.text

        try:
            a_person = new_variable.find("h3")
            a_name = a_person.text
            print(a_name)
        except:
            print("No recipient")

#         a_content = variable.find_all("p")
#         more_variables=""
#         for some_content in a_content:
#              more_variables = more_variables + some_content.text
#
#         new_dictionary={"Writer":a_writer,"Recipient":a_name,"Letter ID:":id_counter,"Letter URL":individual_link,"Content":more_variables}
#         Paston_dictionary_list.append(new_dictionary)
#         id_counter = id_counter + 1
# json.dump(blank_list,open("Paston_Letters.json","w"),indent=4)

    # a_person = individual_link.find("h3")
    # a_name = a_person.text


#Add code to pull out pieces you want based on old code
#Put code in JSON file
#Use regex in JSON file to break down date and names (could pull just things that begin with "To..." since those will actually be letters, not wills or charters)


#writer = soup.find_all("div", attrs = {"class": "indentlevel1"})


# for variable in writer:
#     full_link = variable.find("a")
#     if full_link.has_attr("href"):
#         Paston_main.append(full_link.attrs["href"])
#
# Paston_main_set = set(Paston_main)
#
# Paston_full_links = []
#
# for variable in writer:
#     full_link_all = variable.findall("a")
#     if full_link_all.has_attr("href"):
#         Paston_full_links.append(full_link_all.attrs["href"])
#

        # individual_link = full_link.find("div",attrs = {"class":"resindentlevelx"})
        # print(individual_link)

        #need to do a second scrape and just do "find" as opposed to "findall" to pull out first link in each section
#        if ("div", attrs = "class":"resindentlevelx")
#            print(full_link.attrs["href"])



#     - put URLs into a list
#link_list = []



# - for variable in list - so pull out each URL as a new variable and enter it into a function



#     - scrape each URL and pull out the h2, h3, and p as described in the original Paston scrape, putting it into a dictionary


#     - create a csv file that enters sections in the dictionary



#Next week:         - once this file is made, I think I can use regex to pull out specific sections I want, like date and recipient; I think I could also then put the p sections through something, like put it all together and then search each section for the subject terms



#             -like maybe I'll put in all the basic HTML pieces into the dictionary, then I'll be able to use that file to pull out individual pieces of information. It'll be easier to get information from a dictionary because I can just use the key and not have to worry so much about pulling large amounts from the web...
