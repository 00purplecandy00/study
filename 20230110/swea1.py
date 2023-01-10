
T = int(input())

list = []
for test_case in range(0, T):
    a,b = map(int,input().split())
    answer1 = a//b
    answer2 = a%b
    list.append(answer1)
    list.append(answer2)

for j in range(1,T+1):
	print('#%d %d %d'%((j),list[2*j - 2],list[2*j-1]))

    