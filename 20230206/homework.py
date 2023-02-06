import sys
##1
sys.stdin = open("/Volumes/SD/멀티캠퍼스/20230206/input1.txt","r")
happy=':-)'
sad=':-('
message = input()
cnt = 0
for i in range(0,len(message)-3):
    if message[i:i+3]==happy:
        cnt += 1
    if message[i:i+3]==sad:
        cnt -= 1

if cnt>0:
    print('happy')
elif cnt<0:
    print('sad')
else:
    if happy not in message and sad not in message:
        print('none')
    else:
        print('unsure')
        
##2
sys.stdin = open("/Volumes/SD/멀티캠퍼스/20230206/input2.txt","r")
passenger = 0
max_passenger = 0
for _ in range(4):
    a,b = map(int,input().split())
    passenger -= a
    passenger += b
    if max_passenger < passenger:
        max_passenger = passenger
print(max_passenger)

##3
sys.stdin = open("/Volumes/SD/멀티캠퍼스/20230206/input3.txt","r")
computer = int(input())
lines = int(input())
list1 = []
virus = [1]
for _ in range(lines):
    a,b = map(int,input().split())
    list1.append([a,b])

for _ in range(lines):
    for i in range(0,lines):
        for j in range(0,len(virus)):
            if list1[i][0] == virus[j] and list1[i][1] not in virus:
                virus.append(list1[i][1])
            if list1[i][1] == virus[j] and list1[i][0] not in virus:
                virus.append(list1[i][0])

print(len(virus)-1)

##4
sys.stdin = open("/Volumes/SD/멀티캠퍼스/20230206/input4.txt","r")
island_map = []
island=[]
cnt = 0
sum1 = 0
one_sum = 0
zero_sum = 0
while(1):
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    else:
        for _ in range(b):
            island = list(map(int,input().split()))
            island_map.append(island)
       