import requests
from bs4 import BeautifulSoup

url = "http://www.eventgalaxy.com.sg/products/lighted-balloon-stands/features/property-launch-events/"
request = requests.get(url)
soup = BeautifulSoup(request.text,features="html.parser")

imgs = soup.find_all("div",{"class":"productCatPhoto"})
counter = 1
for img in imgs:
    img = img.find("img")
    with open("D:\\Projects\\Advertising\\LBS\\" + "LBS_" + str(counter) + ".jpg","wb") as f:
        f.write(requests.get(img["src"]).content)
    counter += 1