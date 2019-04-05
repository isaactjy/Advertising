import os
import urllib.request as urllib
from bs4 import BeautifulSoup

mainUrl = "http://www.eventgalaxy.com.sg/products/lighted-balloon-stands/"
html = urllib.urlopen(mainUrl)
soup = BeautifulSoup(html,features="html.parser")

products = soup.find_all("li",{"class":"page_item"})
for product in products:
    productUrl = product.find("a")['href']
    saveFolder = productUrl.split("/")[-2] 
    savePath = "D:\\Projects\\Images\\" + productUrl.split("/")[-2] 

    if not os.path.exists(savePath):
        os.makedirs(savePath)
    #print("Product Url: ",productUrl)
    productHtml = urllib.urlopen(productUrl)
    productSoup = BeautifulSoup(productHtml,features="html.parser")

    # For each product url, get all the categories
    try:
        start_at = productSoup.find("li",{"class":"page_item page-item-1742"})
        shortened_productSoup = start_at.find_all_previous("li")
    except:
        continue

    # For each category in the product url
    for category in shortened_productSoup:
        counter = 1
        try: 
            categoryUrl = category.find("a")['href']
            categoryHtml = urllib.urlopen(categoryUrl)
            categorySoup = BeautifulSoup(categoryHtml,features="html.parser")
            if categoryUrl == "http://www.eventgalaxy.com.sg":
                break
            else:
                #print("Category Url: ",categoryUrl)
                # Download the images for that category
                imgs = categorySoup.find_all("div",{"class":"productCatPhoto"})
                counter = 1
                for img in imgs:
                    img = img.find("img")
                    s = "".join([x[0].upper() for x in saveFolder.split('-')]) + "_"
                    urllib.urlretrieve(img["src"], "D:\\Projects\\Images\\" + saveFolder + "\\" + s + str(counter) + ".jpg")
                    counter += 1
        except TypeError:
            pass
