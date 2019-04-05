import requests
from bs4 import BeautifulSoup

url = "http://www.eventgalaxy.com.sg/products/inflatable-arches/"
request = requests.get(url)
soup = BeautifulSoup(request.text,features="html.parser")

start_at = soup.find("li",{"class":"page_item page-item-1742"})
shortened_soup = start_at.find_all_previous("li")

for category in shortened_soup:
    try: 
        categoryUrl = category.find("a")['href']
        if categoryUrl == "http://www.eventgalaxy.com.sg":
            break
        print(categoryUrl)
    except TypeError:
        pass