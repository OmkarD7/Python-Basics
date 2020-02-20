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
worksheet.write(cellRow, cellCol + 2, "Area")
areas = ["africa", "americas", "asia", "australia", "canada", "europe", "middleeast"]

for a in areas:
    url = "https://www.nytimes.com/section/world/"+str(a)
    print(url)
    uclient = req(url)
    page = uclient.read()
    uclient.close()
    pagesoup = soup(page, 'html.parser')
    newsAreas = pagesoup.find("h1", {"class":"css-1qq4zod e1bbdwbz0"})
    allNewsHeading = pagesoup.findAll("h2", {"class":"css-1j9dxys e1xfvim30"})
    allNewsDate = pagesoup.findAll("div",{"class":"css-n1vcs8 e1xfvim33"})
    allNewsAuthor = pagesoup.findAll("span", {"class":"css-1n7hynb"})
    counter = 0
    eachnewsarea = newsAreas
    while counter < 3:
        eachheading = allNewsHeading[counter]
        #eachdate = allNewsDate[counter]
        eachauthor = allNewsAuthor[counter]
        print("Heading: " + str(eachheading.text))
        print("Author: " + str(eachauthor.text))
        print("Area: "+ str(eachnewsarea.text))
        #print("Date: " + str(eachdate.))
        worksheet.write(cellRow, cellCol, eachheading.text)
        worksheet.write(cellRow, cellCol + 1, eachauthor.text)
        worksheet.write(cellRow, cellCol + 2, eachnewsarea.text)
        cellRow += 1
        counter += 1
    time.sleep(1)
workbook.close()