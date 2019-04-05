import os
import requests
from bs4 import BeautifulSoup

mainUrl = "http://www.eventgalaxy.com.sg/products/lighted-balloon-stands/"
request = requests.get(mainUrl)
soup = BeautifulSoup(request.text,features="html.parser")

products = soup.find_all("li",{"class":"page_item"})
for product in products:
    productUrl = product.find("a")['href']
    saveFolder = productUrl.split("/")[-2] 
    saveInitials = "".join([x[0].upper() for x in saveFolder.split('-')]) + "_"
    savePath = "D:\\Projects\\Images\\" + productUrl.split("/")[-2] 

    if not os.path.exists(savePath):
        os.makedirs(savePath)
    #print("Product Url: ",productUrl)
    productRequest = requests.get(productUrl)
    productSoup = BeautifulSoup(productRequest.text,features="html.parser")

    # For each product url, get all the categories
    try:
        counter = 1
        start_at = productSoup.find("li",{"class":"page_item page-item-1742"})
        shortened_productSoup = start_at.find_all_previous("li")
    except:
        continue

    # For each category in the product url
    for category in shortened_productSoup:
        try: 
            categoryUrl = category.find("a")['href']
            categoryRequest = requests.get(categoryUrl)
            categorySoup = BeautifulSoup(categoryRequest.text,features="html.parser")
            if categoryUrl == "http://www.eventgalaxy.com.sg":
                break
            else:
                print("Getting images for %s, %s, url: %s"%(saveFolder,categoryUrl.split("/")[-2],categoryUrl))
                #print("Category Url: ",categoryUrl)
                # Download the images for that category
                imgs = categorySoup.find_all("div",{"class":"productCatPhoto"})
                for img in imgs:
                    img = img.find("img")
                    with open("D:\\Projects\\Images\\" + saveFolder + "\\" + saveInitials + str(counter) + ".jpg","wb") as f:
                        f.write(requests.get(img["src"]).content)
                    counter += 1
        except TypeError:
            pass
