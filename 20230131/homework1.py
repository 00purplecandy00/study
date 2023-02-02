import sys
##1
sys.stdin = open("input1.txt","r")
a = int(input())
for i in range(0,a):
    print(" "*i,end="")
    print("*"*(a-i))
    
##2
sys.stdin = open("input2.txt","r")
dic={}
list1=[]
list2=[]
list3=[]
total = 0
for _ in range(10):
    a = int(input())
    if a not in dic:        
        dic[a] = 1
    else:
        dic[a] += 1
list1 = list(dic.items())
for i in range(0,len(list1)):
    total += list1[i][0]*list1[i][1]
average = int(total/10)
for i in range(0,len(list1)):
    list2.append(list1[i][0])
    list3.append(list1[i][1])
b = max(list3)
c = list3.index(b)
d = list2[c]
print(average,d,sep="\n")

##3
sys.stdin = open("input3.txt","r")
list1=[]
for _ in range(5):
    word = list(input())
    list1.append(word)
temp = 0
for i in range(0,5):
    if temp < len(list1[i]):
        temp = len(list1[i])
for i in range(0,5):
    if len(list1[i]) < temp:
        for _ in range(0,temp-len(list1[i])):
            list1[i].append("")
for i in range(0,temp):
    for j in range(0,5):
        print(list1[j][i],end="")