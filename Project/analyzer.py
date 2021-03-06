import pdb
from datetime import datetime
from filenames_getter import filler
# We use this to get the day wise, month wise,quarter wise data,
# We return the data taking today closing date from yesterday's closing date.
# 
class analyzer:
    months=[1,3,5,7,8,10,12]
    dates={}
    f = filler()
    def __init__(self):
        for i in range(1,13):
            self.dates[i] = False
        for month in self.months:
            self.dates[month] = True
    def get_next_date(self,date,value):
        # Get the next date from the given value
        # 
        if value=='month':
            if date[1] == 1:
                date[1] = 12
                date[0] -= 1
            else :
                date[1] -= 1
            daty = self.f.correct_date(date[2],date[1],date[0])
            i = 2
            j = 0
            for j in range(0,len(daty)):
                date[i] = daty[j]
                i -= 1
            return date

        elif value=='quarter':
            if date[1]-3 <= 0 :
                date[1] += 12
                date[1] -= 3
                date[0] -= 1
            else:
                date[1] -= 3
            daty = self.f.correct_date(date[2],date[1],date[0])
            i = 2
            j = 0
            for j in range(0,len(daty)):
                date[i] = daty[j]
                i -= 1
            return date
    
    def correct_date(self,date):
        if self.dates[date[1]] == False :
            if date[1] == 2:
                if date[0]%4 == 0:
                    if date[2] > 29:
                        date[2] = 29
                        return date
                    else :
                        if date[2] > 28 :
                            date[2] = 28
                            return date
            else:
                if date[2] > 31:
                        date[2] = 30
                        return date

    def compare_date(self,present,_next):
        # comparing the present date,with next date
        flag = False
        flag = datetime(present[0],present[1],present[2]) < datetime(_next[0],_next[1],_next[2])
        return flag 
                
    def analyze(self,filename):
        daywise = []
        monthwise = []
        quarterly = []
        yearly = []
        last_value = 0
        data=[]
        first_value_in_year=""
        l = 0
        with open(filename,'r') as fopen:
            fopen.readline()  # just to seek the file one line ahead :
            line = fopen.readline()
            if line.startswith('<html><head>'):
                return []
            data = line.split(',')
            first_value_in_year = data
            date = [int(x) for x in data[0].split('-')]
            first = date
            next_month = self.get_next_date(first,'month')
            this_month_close = line.split(',')
            next_quarter = self.get_next_date(date,'quarter')
            this_quarter_close = line.split(',')
            last_value = float(data[-3])
            # for every date compare , it it is less than next date and get the gaining valye
            for line in fopen:
                data = line.split(',')
                date = [int(x) for x in data[0].split('-')]
                if self.compare_date(date, next_month):
                    #pdb.set_trace()
                    monthwise.append(int(10**6 * (float(this_month_close[-3])/float(data[-3]))-1))
                    this_month_close = data
                    next_month = self.get_next_date(date,'month')
                if self.compare_date(date, next_quarter):
                    quarterly.append((float(this_quarter_close[-3])/float(data[-3]))-1)
                    this_quarter_close = data
                    next_quarter = self.get_next_date(next_quarter,'quarter')

                daywise.append(int(10**6 * (last_value/float(data[-3]))-1))
                last_value=float(data[-3])
        yearly.append((float(first_value_in_year[-3])/float(data[-3]))-1)
        monthwise.append((float(this_month_close[-3])/float(data[-3]))-1)
        quarterly.append((float(this_quarter_close[-3])/float(data[-3]))-1)
        return [daywise,monthwise,quarterly,yearly]