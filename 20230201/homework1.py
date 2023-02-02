import sys
##1
sys.stdin = open("input1.txt","r")
hour,minutes = map(int,input().split())
time = int(input())
cook_hour = (hour*60+minutes+time)//60
if cook_hour >= 24:
    cook_hour -= 24
cook_minutes = (hour*60+minutes+time)%60
print(cook_hour,cook_minutes)

##2
sys.stdin = open("input2.txt","r")
a,b = map(int,input().split())
list1 = list(map(int,input().split()))
list2 = []
for i in list1:
    for j in list1:
        for k in list1:
            if i == j or j == k or i == k:
                pass
            else:
                list2.append(i+j+k)
list2 = sorted(list2,reverse=True)
for p in list2:
    if p > b:
        pass
    else:
        print(p)
        break
    
##3
sys.stdin = open("input3.txt","r")
T = int(input())
for _ in range(T):
    score = list(map(int,input().split()))
    a = max(score)
    score.remove(a)
    b = min(score)
    score.remove(b)
    new_a = max(score)
    new_b = min(score)
    if new_a - new_b >= 4:
        print("KIN")
    else:
        print(sum(score))
        
##4
sys.stdin = open("input4.txt","r")
int_a = int(input())
list1 = [{'7','4'},{'7'},{'4'}]
list2 = []
for i in range(int_a,-1,-1):
    list2.append(i)
for j in list2:
    if set(str(j)) in list1:
        print(j)
        break

##5
sys.stdin = open("input5.txt","r")
a = int(input())
list1=[]
i = 666
j = 1
while(1):   
    if j == a:
        print(i)
        break
    else:
        i += 1
        if '666' in str(i):
            j += 1