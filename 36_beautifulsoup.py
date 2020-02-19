from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as request

url = "https://www.flipkart.com/search?q=mobiles"
uclient = request(url)
page = uclient.read()
#page
pagesoup = soup(page, 'html.parser')
allMobileHtml = pagesoup.findAll("div", {"class":"_3wU53n"})
allMobilePriceHtml = pagesoup.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
#print(allMobilePricehtml)
counter = 0
for p in allMobilePriceHtml:
    eachdiv = p
    print(eachdiv.text)
#print(allMobileHtml)
for i in allMobileHtml:
    eachdiv = i
    print(eachdiv.text)