import sys


##1
sys.stdin = open("h_input1.txt","r")

a = int(input())
b = int(input())
c = int(input())

if a+b+c != 180:
    print("Error")
else:
    if a==b==c:
        print("Equilateral")
    else:
        if a==b or b==c or c==a:
            print("Isosceles")
        else:
            print("Scalene")
            
##2
i = 0
sys.stdin = open("h_input2.txt","r")
T = int(input())
for i in range(T):  
    change = int(input())
    q = change // 25
    change %= 25

    d = change // 10
    change %= 10

    n = change // 5
    change %= 5

    p = change
    print(q,d,n,p)

##3
sys.stdin = open("h_input3.txt","r")
T = int(input())
list1 = []
say_no = 0
customer = list(map(int,input().split()))
for i in customer:
    if i not in list1:
        list1.append(i)
    else:
        say_no += 1
print(say_no)

##4
sys.stdin = open("h_input4.txt","r")

list1=[]
T = int(input())
for i in range(T):
    a = int(input())
    if a == 0:
        list1.pop()
    else:
        list1.append(a)
    
print(sum(list1))

##5
i = 0
j = 0
k = 0
l = 0
m = 0
z = 0
sys.stdin = open("h_input5.txt","r")
T = int(input())
list1 = []
list2 = []
for i in range(1,T+1):
    list1.append(i)

for k in range(T-1):
    j = list1.pop(0)
    list2.append(j)
    j = list1.pop(0)
    list1.append(j)
j = list1.pop(0)
list2.append(j)

for l in list2:
    print(l,end = " ")
    
##6
i = 0
j = 0
sys.stdin = open("h_input6.txt","r")

T = int(input())
for _ in range(T) :
    string = input()
    answer = 'YES'
    cnt = 0
    for i in range(len(string)) :       
        if string[i] == '(' :    
            cnt = cnt + 1      
        else:
            cnt = cnt - 1
        if cnt < 0:
            answer = 'NO'
            break;
    if cnt != 0 : answer = 'NO'
    print(answer)