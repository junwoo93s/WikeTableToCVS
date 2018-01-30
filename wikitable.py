#Author : Junwoo Seo

import csv
import urllib.request
import urllib2
from urllib2 import urlopen
from bs4 import BeautifulSoup

f = open('FILENAME.csv', 'w', newline='') #this is where you open the excel file that you want to transferred into. 
writer = csv.writer(f)

with open("FILENAME.csv", "wb") as f: #FILENAME is where your file name goes in. 
    w = csv.DictWriter(f, fieldnames=["COULMNS NAME IN YOUR EXCEL"]) #you can list the colunms that you want to be saved 
    w.writeheader()


scrap = BeautifulSoup(urllib2.urlopen("https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Alabama").read(), 'lxml')
table_body = scrap('table', {"class": "wikitable sortable jquery-tablesorter"})[0].find_all('tr')
for row in table_body:
    colums = row.findChildren(recursive=False)
    colums = [ele.text.strip() for ele in colums]
    writer.writerow(colums)
    print(colums)

    
    
    
