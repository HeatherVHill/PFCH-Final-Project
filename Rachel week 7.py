# webbrowser module documentation-->https://docs.python.org/2/library/webbrowser.html
import requests, json, webbrowser

# q: search for "Edward Hopper" + pagze_size: expand amt of items the API returns
payload = {"q": "Edward+AND+Hopper", "page_size": "100", "api_key": "c168315425c50175a04f5866431e91d6"}
r = requests.get('http://api.dp.la/v2/items', params=payload)

# print(r.status_code)
# print(r.text)

data = json.loads(r.text)
urls = []

for a_doc in data["docs"]:
    # try/except added to check to see if item has an "object" key
    try:
    # looks for URLs to add to list
        if "http" in a_doc["object"]:
            urls.append(a_doc["object"])
            # removes duplicate URLs-->https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
            urls = list(set(urls))
    except KeyError:
        print("No object found")


# opens URL
for url in urls:
    webbrowser.open(url)
