# 문제 1
# # 정수를 출력하세요.
# 5
a = int(input("정수를 입력하세요"))
print(a)


# 문제 2
# # 단어를 구분해서 출력하세요.
# hello python world
word = input("단어를 입력하세요(띄어쓰기로 구분)").split()
for i in word:
    print(i,end=" ")
print()


# 문제 3
# # 테스트 케이스마다 입력 값을 그대로 출력하세요.
# 3 # 테스트 케이스 수
# 1 
# 2 
# 3 
T = int(input("테스트케이스의 수를 입력하세요")) 

for t in range(1, T+1):
    print(t)




# 문제 4
# # 2개 이상의 정수를 출력하세요.
# 2 0 3 92 3

list = []
list = input("2개 이상의 정수를 입력하세요(띄어쓰기로 구분)").split()
for i in list:
    print(i,end=" ")
print()


# 문제 5
# # 2개의 정수를 출력하세요.
# 2 3
a,b = map(int,input("2개의 정수를 입력하세요").split())
print(a,b)



# 문제 6
# # 단어를 구분해서 출력하세요.
# I am Programmer

string = input("단어를 구분해서 입력하세요").split()
for i in string:
    print(i,end=" ")
print()


# 문제 7
# # 테스트 케이스마다 입력 값을 그대로 출력하세요.
# 5 # 테스트 케이스 수
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# 13 14 15

T = int(input("테스트케이스의 수를 입력하세요"))
list1=[]
list=[]
for i in range(1,T+1):
    a,b,c = map(int,input("%s번째 3개 정수의 나열을 입력하세요(띄어쓰기로 구분)"%i).split())
    list = [a,b,c]
    list1.append(list)

for j in list1:
    for k in j:
        print(k,end =" ")
    print()

# 문제 8
# # 테스트 케이스마다 입력 값을 그대로 출력하세요.
# 5 # 테스트 케이스 수
# 1 38 108 29 3 2 39
# 1 9 12 3 5 1
# 28 39 1 20 9 1
# 34 5 6 8
# 9 3 2 10 1 2 4

T = int(input("테스트케이스의 수를 입력하세요"))
list1=[]
list=[]
for i in range(1,T+1):
    list = map(int,input("%s번째 정수의 나열을 입력하세요(띄어쓰기로 구분)"%i).split())
    list1.append(list)

for j in list1:
    for k in j:
        print(k,end =" ")
    print()