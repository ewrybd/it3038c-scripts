import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.kohls.com/product/prd-1252558/la-crosse-technology-14-in-atomic-analog-wall-clock.jsp?prdPV=22").content
soup = BeautifulSoup(data, 'html.parser')
search = soup.find("h1", {"class":"product-title"})
name = search.text.strip()
search = soup.find("span", {"class":"pdpprice-row2-main-text"})
price = search.text.strip()
search = soup.find("span", {"class":"creativeBadgeTop"})
rated = search.text.strip()
print("The item %s is in stock at Kohls! It has a price of %s in USD. This item is listed as a %s item." % (name, price, rated))