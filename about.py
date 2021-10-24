import os
from fractions import Fraction
def bijiao(path1,path2):
    f1=open('path1')
    f2=open('an.txt','w')
    line=f1.readline()
    num=1
    while line:
        line=line.split(". ")
        answer=line[1]
        ans=Fraction(eval(answer)).limit_denominator()
        f2.write(str(num)+". ")
        f2.write(str(ans.numerator) + '/' + str(ans.denominator))
        f2.write("\n")
        line = f1.readline()
        num+=1
    f1.close()
    f2.close()
