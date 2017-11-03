# - scrape main page with BS to get list of URLs using the "a" items [href?]



#     - put URLs into a list



# - for variable in list - so pull out each URL as a new variable and enter it into a function



#     - scrape each URL and pull out the h2, h3, and p as described in the original PAston scrape, putting it into a dictionary


#     - create a JSON file that enters sections in the dictionary



#         - once this file is made, I think I can use regex to pull out specific sections I want, like date and recipient; I think I could also then put the p sections through something, like put it all together and then search each section for the subject terms



#             -like maybe I'll put in all the basic HTML pieces into the dictionary, then I'll be able to use that file to pull out individual pieces of information. It'll be easier to get information from a dictionary because I can just use the key and not have to worry so much about pulling large amounts from the web...
