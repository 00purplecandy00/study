import sys
sys.stdin = open("input1.txt","r")
m,n = map(int,input().split())
dic={}
result=[]
for _ in range(m+n):
    a = input()
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1
for i in dic:
    if dic[i] == 2:
        result.append(i)
result = sorted(result)
print(len(result))
for j in result:
    print(j)