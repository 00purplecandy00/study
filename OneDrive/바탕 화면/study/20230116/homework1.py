##1
a,b = map(int,input().split())
print(a+b)

##2
a = int(input())
b = int(input())
print(a+b)

##3
T = int(input())
list1 = []

for i in range(T):
    a,b = map(int,input().split())
    list1.append(a+b)
for j in list1:
    print(j)

##4
T = int(input())
list1 = []
for i in range(T):
    a,b = map(int,input().split(','))
    list1.append(a+b)
for j in list1:
    print(j)

##5
T = int(input())
list1=[]
for i in range(0,T):
    a,b = map(int,input().split())
    list1.append(a+b)
for j in range(0,T):
    print("Case #%s: %s"%((j+1),(list1[j])))

##6
T = int(input())
list1=[]
list2=[]
result=[]
for i in range(T):
    a,b = map(int,input().split())
    list1.append(a)
    list2.append(b)
    result.append(a+b)
for j in range(T):
    print("Case #%s: %s + %s = %s"%((j+1),list1[j],list2[j],result[j]))