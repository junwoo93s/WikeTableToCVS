# for 100
# wiki data
# https://en.wikipedia.org/wiki/List_of_United_States_counties_and_county_equivalents
# https://en.wikipedia.org/wiki/List_of_counties_by_U.S._state
# https://www.census.gov/geo/reference/geoguide.html
# https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt

import csv
#import urllib.request
import urllib2
#from urllib2 import urlopen
from bs4 import BeautifulSoup

#f = open('Alabama.csv', 'w', newline='')
#writer = csv.writer(f)

with open("Alabama.csv", "wb") as f:
    w = csv.DictWriter(f, fieldnames=["Difference", "NumNegativePorter", "NumPositivePorter", "dsk", "pubdate", "pubmon", "statementNumber"])
    w.writeheader()


soup = BeautifulSoup(urllib2.urlopen("https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Alabama").read(), 'lxml')
tbody = soup('table', {"class": "wikitable sortable jquery-tablesorter"})[0].find_all('tr')
for row in tbody:
    cols = row.findChildren(recursive=False)
    cols = [ele.text.strip() for ele in cols]
    writer.writerow(cols)
    print(cols)
