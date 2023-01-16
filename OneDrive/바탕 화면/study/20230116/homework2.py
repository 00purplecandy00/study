##1
list1 =[]
for i in range(5):
    a = int(input())
    if a < 40:
        list1.append(40)
    else:
        list1.append(a)
print(round(sum(list1)/5))

##2
list1=[]
list2=[]
a,b = map(int,input().split())
list1 = list(map(int,input().split()))
for i in list1:
    if i < b:
        list2.append(i)
for j in list2:
    print(j,end=" ")

##3
a,b,c = map(int,input().split())
answer = 0
if a==b==c:
    answer = 10000 + a*1000
elif a==b or a==c:
    answer = 1000 + a*100
elif b==c:
    answer = 1000 + b*100
else:
    answer = max(a,b,c)*100
print(answer)

##4
T=int(input())
answer = 0
for i in range(T):
    answer1 = int(input())
    if answer1 == 1:
        answer += 1
    else:
        answer -= 1
if answer > 0:
    print("Junhee is cute!")
elif answer < 0:
    print("Junhee is not cute!")

##5
T = int(input())
list1=[]
list2 = list(map(int,input().split()))
point = 0
total = 0
for i in range(T):
    if list2[i] == 0:
        point = 0
        list1.append(point)
    else:
        point += 1
        list1.append(point)
for j in list1:
    total += j
print(total)

