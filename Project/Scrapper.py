from bs4 import BeautifulSoup
import urllib2 
import re

class Scrapper:
    d = {}

    def scrap_and_get_names(self):
        url="http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        tabul = soup.find("table",{"class" : "wikitable sortable"})
        rex = re.compile(r'<td><a.*?>(.*?)</a></td>')
        rey = re.compile(r'<td>(.*?)</td>')
        d = {} # store all of the records in this list
        shortform=""
        name=""
        for row in tabul.findAll('tr'):
            if len(row)>1:
                    col = row.findAll('td')
                    if len(col)>3 :
                            #print col,"\n"
                            match = rex.match(str(col[0]))
                            shortform = match.group(1)
                            name = rex.match(str(col[1])).group(1) 
                            d[shortform] = name
        print(len(d.keys()))
        return d;

    def __init__(self):
        self.d={}

