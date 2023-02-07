import sys
##1
sys.stdin = open("input1.txt","r")

n = int(input())
l = []

for _ in range(n):
	l.append(int(input()))
count = 0
max = 0
for x in reversed(l):
	if max < x:
		max = x
		count += 1
print(count)

##2
sys.stdin = open("input2.txt","r")

num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")
    
##3
sys.stdin = open("input3.txt","r")
king, stone, N = input().split()
k = list(map(int, [ord(king[0]) - 64, king[1]]))
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))
move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

for _ in range(int(N)):
    m = input()
    nx = k[0] + move[m][0]
    ny = k[1] + move[m][1]
    if 0 < nx <= 8 and 0 < ny <= 8:
        if nx == s[0] and ny == s[1]:
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny]
                s = [sx, sy]
        else:
            k = [nx, ny]
print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')