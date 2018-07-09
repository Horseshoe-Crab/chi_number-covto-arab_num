import pdb
import string
import os
chi_number={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'零':0,'两':2}
chi_times={'十':10,'百':100,'千':1000,'万':10**4,'兆':10**6,'亿':10**8}
process=[[]]
process_string=[]
str_test='一个弟弟有65块钱，他说他是两个人，其实只有三百四十五快钱，有一万零一块钱,两千三百四十五万八千六百三十二'
flag=True
for i in str_test:
    if i in chi_number.keys() or i in chi_times.keys():
        if flag == False:
            process.append([])
        process[-1].append(i)
        flag= True
    else: 
        flag=False

#print(process)
tmp=0
result=[]
bigger=False 
temp=0
for i in process:
    result.append(int)
    for j in i:
        if j in chi_number.keys():
           if len(i)==1:
                tmp =tmp+chi_number[j]
           else:
            temp=chi_number[j]
        else:
            if tmp<chi_times[j]:
                tmp=tmp*chi_times[j]
            tmp=tmp+temp*chi_times[j]
    tmp=tmp+temp
    string_tmp=str(tmp)
    result[-1]=string_tmp;
    tmp=0
    temp=0
print(str_test)
for i in process:
   process_string.append([])
   process_string[-1]=''.join(i)
for i in range(len(process_string)):
    str_test=str_test.replace(process_string[i],result[i],1)
print(result)
print(process_string)
print(str_test)
