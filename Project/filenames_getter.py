import urllib
import StringIO
from lxml import etree
class filler:
    months = []
    incs={}

    def get_input(self):
        print("Enter the date as DD,MM,YYYY");
        c=filler()
        (day,month,year)=tuple(int(x.strip()) for x in raw_input().split(','))
        date = c.correct_date(day,month,year)
        return date;
        

    def __init__(self):
        self.months = [1,3,5,7,8,10,12]

    def get_all_from_years(self,day,month,year):

        link = "http://real-chart.finance.yahoo.com/table.csv?s="
        a="&a="+str(month-1);
        b="&b="+str(day)
        c="&c="+str(year-1)
        d="&d="+str(month-1)
        e="&e="+str(day)
        f="&f="+str(year)
        link_b = a+b+c+d+e+f+"&g=d&ignore=.csv"
        result = urllib.urlopen('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        html = result.read()
        parser = etree.HTMLParser()
        tree   = etree.parse(StringIO.StringIO(html), parser)
        xpath = '//table/tr[position()>1]/td[position()=1]/a/child::text()'
        names = tree.xpath(xpath)
        companies = tree.xpath('//table/tr[position()>1]/td[position()=2]/a/child::text()')

        i = 0
        while ( i < len(names)):
            self.incs[names[i]] = companies[i]
            print names[i],companies[i],"\n"
            csvfile = urllib.urlopen(link + names[i] + link_b)
            file_ = open(names[i]+'.csv','w')
            file_.write(csvfile.read())
            file_.close()
            i += 1
        return self.incs;
     
    def correct_date(self,day,month,year):
        i = year%4;
        if year > 2015 :
            year = 2015
        if day < 1 :
            day = 1;
        if (month<1):
            month = 1
        elif month>12:
            month = 12
        if (month == 2):
            if i:
                if day > 28 :
                    day = 28
            else :
                if day > 29:
                    day = 28
        elif month in self.months:
            if day>31:
                day = 31
        else:
            if day > 30 :
                day = 30 
        
        return (day,month,year)
            
    def main(self):
        tup=self.get_input()
        self.get_all_from_years(tup[0],tup[1],tup[2])