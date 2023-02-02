import sys
##1
sys.stdin = open("input1.txt","r")
a,b = input().split()
a = list(a)
b = list(b)
a_sum = 0
result = 0
for i in a:
    a_sum += int(i)
for j in b:
    result += a_sum * int(j)
print(result)

##2
sys.stdin = open("input2.txt","r")
N = int(input())
for i in range(1, N+1):
    print('*'*i)
    
##3
sys.stdin = open("input3.txt","r")
N = int(input())
for i in range(1,10):
    print("%s * %s = %s"%(N,i,N*i))
    
##4
sys.stdin = open("input4.txt","r")
list1=[]
for _ in range(5):
    a = list(map(int,input().split()))
    list1.append(sum(a))
b = max(list1)
c = list1.index(b)
print(c+1,b)

##5
sys.stdin = open("input5.txt","r")
list1=[]
for _ in range(4):
    a = list(map(int,input().split()))
    for i in range(a[0],a[2]):
        for j in range(a[1],a[3]):
            if (i,j) not in list1:
                list1.append((i,j))
print(len(list1))
