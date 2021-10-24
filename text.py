import random
from fractions import Fraction
import math
from typing import List

print("请输入题目数目n:",end="")
N=input()
N=int(N)
print("请输入取值范围R",end="")
print()
r=input()
r=int(r)
# 生成随机数字
def number(input):
    answer=round(random.uniform(0,input),int(random.uniform(0,3)))
    output=(Fraction(answer).limit_denominator())
    return(answer)

# 创建一个起始式子
def array():
    newArray=[1,2.0,3,4.0,5]
    newArray[0]='('
    newArray[4]=')'
    newArray[1]=number(r)#暂定数字范围为0-2   
    newArray[3]=number(r)
    newArray[2]=random.choice(['+','*','-','/'])
    if(newArray[2]=='-'):#保证算数结果不为负数
        if(newArray[1]<newArray[3]):
            temp=newArray[1]
            newArray[1]=newArray[3]
            newArray[3]=temp
    elif(newArray[2]=='/'):#保证除数不为0
        while(newArray[3]==0):
            newArray[3]=number(r)  
    newArray[3]=Fraction(newArray[3]).limit_denominator()
    newArray[1]=Fraction(newArray[1]).limit_denominator()
    return(newArray)

# 平凑其新的式子
def new(num):
    newArray=[1,2.0,3,4.0,5]
    newArray[0]='('
    newArray[4]=')'
    newArray[3]=number(r) #暂定数字范围为0-2  
    while(newArray[3]==0):
        newArray[3]=number(r)
    if(num<newArray[3]):
        newArray[2]=random.choice(['-','*','/'])
    else:newArray[2]=random.choice(['+','*','-','/'])

    if(newArray[2]=='-'):
        newArray[1]=newArray[3]+num
    elif(newArray[2]=='+'):
        newArray[1]=num-newArray[3]
    elif(newArray[2]=='*'):
        newArray[1]=num/newArray[3]
    else:
        while(newArray[3]==0):
            newArray[3]=number(r)
        newArray[1]=num*newArray[3]
    newArray[3]=(Fraction(newArray[3]).limit_denominator())
    newArray[1]=(Fraction(newArray[1]).limit_denominator())
    return(newArray)

fl=open('pro.txt',mode='w')
sum=1
while(sum<=N):
    list=array()#创建一个基本式子
    num=[]
    for i in range(len(list)):
        if(type(list[i])!=type(list[0])):num.append(i)#确认数字的位置
    a=random.choice(num)#随机挑选一个数字
    n=new(list[a])#生成新的式子
    n=n[-1::-1]
    del list[a]
    print(str(sum)+(". "),end="")
    fl.write(str(sum)+(". "))
    for i in n:
        list.insert(a,i)
    for i in list:
        print(i,end='')
        fl.write(str(i))
    print(" ")
    fl.write("\n")
    sum+=1
fl.close()
