import sys
##1
sys.stdin = open("input1.txt","r")
T = int(input())
cups = [1,0,0]
for _ in range(T):
  i,j = map(int,input().split())
  cups[i-1],cups[j-1] = cups[j-1],cups[i-1]
ball = cups.index(1)+1
print(ball)  

##2
sys.stdin = open("input2.txt","r")
W = []
K = []
for _ in range(10):
    W.append(int(input()))
for _ in range(10):
    K.append(int(input()))
W = sorted(W,reverse=True)
K = sorted(K,reverse=True)
W_score = W[0]+W[1]+W[2]
K_score = K[0]+K[1]+K[2]
print(W_score,K_score)

##3
sys.stdin = open("input3.txt","r")
T = int(input())
road = list(map(int,input().split()))
list1=[]
total_differ = 0
max_differ = 0
for i in range(0,T-1):
    if road[i+1] > road[i]:
        differ = road[i+1] - road[i]
        total_differ += differ
        if total_differ > max_differ:
            max_differ = total_differ
    else:
        total_differ = 0
print(max_differ)

##4
sys.stdin = open("input4.txt","r")
word = input()
list1=[]
word_length = len(word)
for i in range(1,word_length-1):
    for j in range(1,word_length-1):
        for k in range(1,word_length-1):
            if i+j+k == word_length:
                first = word[0:i]
                second = word[i:i+j]
                third = word[i+j:i+j+k]
                first = first[::-1]
                second = second[::-1]
                third = third[::-1]
                list1.append(first+second+third)
list1 = sorted(list1,key=lambda x:x)
print(list1[0])