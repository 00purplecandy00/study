# 입출력 문제
# 문제에서 주어지는 입력을 받기 적합한 입력 코드를 작성하세요.

# 입력과 똑같이 출력하는 코드를 작성하세요.



# 문제 1
# 공백으로 구분된 정수

# 5 19 2901 2039 41 2 23 40 
import sys
sys.stdin = open("input1.txt","r")
print(input(),end=" ")
print()




# 문제 2
# 공백으로 구분된 문자열

# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
import sys
sys.stdin = open("input2.txt","r")
for i in input().split():
    print(i,end=" ")
print()



# 문제 3
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
import sys
sys.stdin = open("input3.txt","r")
test_case = int(input())
print(test_case)
for i in range(test_case):
    number = int(input())
    print(number)
    for j in range(number):
        numbers = list(map(int,input().split()))
        for n in numbers:
            print(n)


# 2 
# 3
# 1
# 2 
# 3
# 2
# 1 
# 2





# 문제 4
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
import sys
sys.stdin = open("input4.txt","r")
test_case = int(input())
print(test_case)
for i in range(test_case):
    number = int(input())
    print(number)
    for j in range(number):
        numbers = list(map(int,input().split()))
        for n in numbers:
            print(n,end=" ")
        print()



# 2  
# 3  
# 1 1
# 2 2
# 3 3
# 2
# 1 1
# 2 2





# 문제 5
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# 각 문장에 포함된 단어를 공백을 기준으로 출력하세요.

import sys
sys.stdin = open("input5.txt","r")
test_case = int(input())
print(test_case)
for i in range(test_case):
    number = int(input())
    print(number)
    for j in range(number):
        a = list(input().split("\n"))
        for n in a:
            print(n)

# 2 
# 2 
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Donec rutrum ex vel nibh vulputate, ut convallis turpis elementum.
# 5
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Nam eget tellus eu tortor rutrum tincidunt.
# Etiam scelerisque lacus ut enim dignissim, nec pulvinar nisl
# Vivamus quis orci malesuada, mattis libero a, rhoncus sapien.
# Phasellus vehicula turpis a nisl ullamcorper finibus.





# 문제 6
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
import sys
sys.stdin = open("input6.txt","r")
test_case = int(input())
print(test_case)
for i in range(test_case):
    number = int(input())
    print(number)
    for j in range(number):
        numbers = list(map(int,input().split()))
        for n in numbers:
            print(n,end=" ")
        print()


# 2  
# 3  
# 1 3 492 32
# 32 90 65 2 1
# 3 9 9
# 2
# 1 
# 4 93 1 2





# 문제 7
# 테스트 케이스와 입력 줄 수가 같은 줄에 주어지는 경우
import sys
sys.stdin = open("input7.txt","r")
test_case,number = map(int,input().split())
print(test_case,number)
for i in range(test_case):
    for j in range(number):
        numbers = list(map(int,input().split()))
        for n in numbers:
            print(n,end=" ")
        print()
# 2 1
# 1
# 2





# 문제 8
# 테스트 케이스와 입력 줄 수가 같은 줄에 주어지는 경우

# 2 2
# 2 3
# 1 2
# 3 4
# 5 9





# 문제 9
# 테스트 케이스와 입력 줄 수가 같은 줄에 주어지는 경우

# 2 3 
# 1 3 492 
# 32 90 65
# 3 9 9
# 1 3 9
# 4 93 1
# 2 4 2