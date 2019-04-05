import urllib.request as urllib
from bs4 import BeautifulSoup

url = "http://www.eventgalaxy.com.sg/products/lighted-balloon-stands/"
html = urllib.urlopen(url)
soup = BeautifulSoup(html)

products = soup.find_all("li",{"class":"page_item"})
for product in products:
    print(product.find("a")['href'])