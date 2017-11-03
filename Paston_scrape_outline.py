# - scrape main page with BS to get list of URLs using the "a" items [href?]

import requests, json

home_page = requests.get("http://name.umdl.umich.edu/Paston")

#print(page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(home_page.content, 'html.parser')

writer = soup.find_all("span", attrs = {"class": "divhead"})

for variable in writer:
    full_link = variable.find("a")
    if full_link.has_attr("href"):

        #need to do a second scrape and just do "find" as opposed to "findall" to pull out first link in each section
        if ("div", attrs = "class":"resindentlevelx")
            print(full_link.attrs["href"])



#     - put URLs into a list



# - for variable in list - so pull out each URL as a new variable and enter it into a function



#     - scrape each URL and pull out the h2, h3, and p as described in the original Paston scrape, putting it into a dictionary


#     - create a csv file that enters sections in the dictionary



#Next week:         - once this file is made, I think I can use regex to pull out specific sections I want, like date and recipient; I think I could also then put the p sections through something, like put it all together and then search each section for the subject terms



#             -like maybe I'll put in all the basic HTML pieces into the dictionary, then I'll be able to use that file to pull out individual pieces of information. It'll be easier to get information from a dictionary because I can just use the key and not have to worry so much about pulling large amounts from the web...
