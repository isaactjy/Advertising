import requests
from bs4 import BeautifulSoup

url = "http://www.eventgalaxy.com.sg/products/lighted-balloon-stands/"
request = requests.get(url)
soup = BeautifulSoup(request.text,features="html.parser")

products = soup.find_all("li",{"class":"page_item"})
for product in products:
    print(product.find("a")['href'])