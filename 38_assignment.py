from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
import xlsxwriter as xlsx
import time

workbook = xlsx.Workbook("NYTimes_news.xlsx")
worksheet = workbook.add_worksheet("News")
cellRow = 0
cellCol = 0
worksheet.write(cellRow, cellCol, "Heading")
worksheet.write(cellRow, cellCol + 1, "Author")
areas = ["africa", "americas", "asia", "australia", "canada", "europe", "middleeast"]

for a in areas:
    url = "https://www.nytimes.com/section/world/"+str(a)
    print(url)
    uclient = req(url)
    page = uclient.read()
    uclient.close()
    pagesoup = soup(page, 'html.parser')
    allNewsHeading = pagesoup.findAll("h2", {"class":"css-1j9dxys e1xfvim30"})
    #allNewsDate = pagesoup.findAll("div", {"class":"css-n1vcs8 e1xfvim33"})
    allNewsAuthor = pagesoup.findAll("span", {"class":"css-1n7hynb"})
    #print(allNewsDate)
    counter = 0
    while counter < 5:
        eachheading = allNewsHeading[counter]
        #eachdate = allNewsDate[counter]
        eachauthor = allNewsAuthor[counter]
        print("Heading: " + str(eachheading.text))
        print("Author: " + str(eachauthor.text))
        #print("Date: " + str(eachdate.))
        worksheet.write(cellRow, cellCol, eachheading.text)
        worksheet.write(cellRow, cellCol + 1, eachauthor.text)
        cellRow += 1
        counter += 1
    time.sleep(1)
workbook.close()