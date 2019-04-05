import urllib.request as urllib
from bs4 import BeautifulSoup

url = "http://www.eventgalaxy.com.sg/products/lighted-balloon-stands/features/property-launch-events/"
html = urllib.urlopen(url)
soup = BeautifulSoup(html)

imgs = soup.find_all("div",{"class":"productCatPhoto"})
counter = 1
for img in imgs:
    img = img.find("img")
    urllib.urlretrieve(img["src"], "D:\\Projects\\Advertising\\" + "LBS_" + str(counter) + ".jpg")
    counter += 1