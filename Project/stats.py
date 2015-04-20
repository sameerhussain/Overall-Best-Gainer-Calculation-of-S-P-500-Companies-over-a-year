from analyzer import analyzer
import glob
from _ast import TryExcept
# this class is used to sort the values according to gain and find the correspoing output valuee
class stats:

    def collect_data(self):
        filenames = glob.glob("*.csv")
        d = {}
        an = analyzer()
        for filename in filenames:
            d[filename[:-4]] = an.analyze(filename)
        return d 

    def sort_the_matter_out(self,d):
        keys = d.keys()
        B={}
        l = len(d[keys[0]][0])
        rank = 1
        len_of_keys=0
        value=[]
        A={}

        for  j in range(0,4) :
            rank = 1;
            l = len(d[keys[0]][j])
            A = {}

            if j == 0:
                for key in keys:
                    B[key] = [[],[],[],[]]

            for i in range(0,l) :
                A={}
                for key in keys :
                        try:
                            if len(d[key][j]) < l:
                                d.pop(key)
                                keys.remove(key)
                                continue
                        except IndexError:
                            d.pop(key)
                            keys.remove(key)
                            continue
                        if key in A.keys():
                            A[d[key][j][i]].append(key)
                        else:
                            A[d[key][j][i]] = [key]
                    # keys here, the values from the daily values
                rank = 1

                for key in sorted(A.keys()):
                    value = A[key]
                    len_of_keys = len(value)
                    if len_of_keys > 1:
                        value = A[key]
                        for val in value:
                            B[val][j].append(float(1/rank))
                            rank += 1
                    else:
                        B[value[0]][j].append(rank)
                        rank += 1
        
        keys = B.keys();
        print ("key","daywise","monthly","quarterly","yearwise")
        for key in keys:
             l = len(B[key])
             ck = []
             for j in range(0,l):
                 if ( B[key][j]):
                         m = sum(B[key][j])
                         n = max(B[key][j])
                         p = min(B[key][j])

                         B[key][j].append('%3.3f' %(1-((float(p)/float(n)))))
                         ck.append('%3.3f' %(1-((float(p)/float(n)))))
             print (key,ck)
        return B;

def main():
    a = stats()
    D = a.sort_the_matter_out(a.collect_data())

if __name__=='__main__':
    main()
