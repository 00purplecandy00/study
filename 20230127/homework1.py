import sys
##1
sys.stdin = open("input1.txt","r")
list1 = list(map(int,input().split()))
a = list1.index(max(list1))
list1.pop(a)
print(max(list1))

##2
sys.stdin = open("input2.txt","r")
list1 = []
cnt = 0
sentence = input()
if sentence == "고무오리 디버깅 시작":
    while(1):    
        if sentence == "고무오리 디버깅 끝":
            break
        sentence = input()
        list1.append(sentence)
      
for word in list1:
    if word == "문제":
        cnt += 1
    elif word == "고무오리":
        if cnt == 0:
            cnt += 2
        else:
            cnt -= 1
            
if cnt == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")

##3
sys.stdin = open("input3.txt","r")
a,b = map(int,input().split())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list3 = set(list1)^set(list2)
print(len(list3))

##4
sys.stdin = open("input4.txt","r")
list1=[]
list2=[]
for _ in range(10):
    a = int(input())
    list1.append(a)
for number in list1:
    a = number%42
    list2.append(a)
print(len(set(list2)))

##5
sys.stdin = open("input5.txt","r")
T = int(input())
list1=[]
dic={}
i=0
for _ in range(T):
    a = input()
    if a not in list1:        
        list1.append(a)
list1.sort()
for word in list1:
    dic[word] = len(word)
dic = sorted(dic.items(),key=lambda x:x[1])
for i in range(len(dic)):
    print(dic[i][0])
    
##6
sys.stdin = open("input6.txt","r")
import heapq
numbers = []
T = int(input())
for _ in range(T):
    a = int(input())
    if a != 0:
        heapq.heappush(numbers,(abs(a),a))
    else:
        if not numbers:
            print(0)
        else:
            print(heapq.heappop(numbers)[1])
