# 문제 목록


# 문제 1
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.

# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.

# 단, index() / find() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# 1
# 출력 예시 2
# 문자열을 입력하세요 > hEllo hypergrowth # 사용자 입력
# 9
# 출력 예시 3
# 문자열을 입력하세요 > java # 사용자 입력
# -1

a = input("문자열을 입력하세요")
cnt = 0
if 'e' in a:
    for i in a:    
        if i == 'e':
            print(cnt)
            break
        elif i != 'e':
            cnt += 1
else:
    print(-1)





# 문제 2
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# hello 1
# 출력 예시 2
# 문자열을 입력하세요 > hello hypergrowth # 사용자 입력
# hello 1
# hypergrowth 1
# 출력 예시 3
# 문자열을 입력하세요 > apple apple banana grape # 사용자 입력
# apple 2
# banana 1
# grape 1

list = input("문자열을 입력하세요").split()
dic = {}
for i in list:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for j in dic:
    print(j,dic[j])



# 문제 3
# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.

# 단, replace() 메서드는 사용하지 마세요.

# 출력 예시 1
# 문자열을 입력하세요 > apple # 사용자 입력
# appl
# 출력 예시 2
# 문자열을 입력하세요 > hello # 사용자 입력
# hllo
# 출력 예시 3
# 문자열을 입력하세요 > hEllo # 사용자 입력
# hEllo

b = input("문자열을 입력하세요")
list = [char for char in b]
cnt = 0
for i in list:
    if i != 'e':
        cnt += 1
    else:
        list.pop(cnt)

for j in list:
    print(j,end="")

print()

# 문제 4
# 문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한 알파벳의 개수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > apple p # 사용자 입력
# 2
# 출력 예시 2
# 문자열을 입력하세요 > hello o # 사용자 입력
# 1
# 출력 예시 3
# 문자열을 입력하세요 > hEllo a # 사용자 입력
# 0

a,b = input("문자열과 알파벳을 공백으로 구분해서 입력해주세요").split()
cnt = 0
for i in a:
    if i == b:
        cnt += 1
    
print(cnt)




# 문제 5
# 양의 정수 3개를 입력받고, 3개의 양수를 - 로 연결해서 출력하세요.

# 단, join() 메서드는 사용하지마세요.

# 출력 예시
# 문자열을 입력하세요 > 010 1234 5678 # 사용자 입력
# 010-1234-5678

list=[]
list = input("양의정수 3개를 띄어쓰기로 구분해서 입력하세요").split()
for i in list:
    if i == list[len(list)-1]:
        print(i)
    else:    
        print(i,end="-")



# 문제 6
# 양의 정수를 입력받고, 자리수의 합을 출력하세요.

# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.

# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > 244 # 사용자 입력
# 10
# 출력 예시 2
# 문자열을 입력하세요 > 1 # 사용자 입력
# 1
# 출력 예시 3
# 문자열을 입력하세요 > -10 # 사용자 입력
# -1

list = []
result = 0
count = 1
a = int(input("양의 정수를 입력하세요"))
b = a
if b <= 0:
    print(-1)
else:
    while(1):
        if b < 10:
            break
        else:
            count += 1
            b = b//10
print(count)

for i in range(count,-1,-1):
    c = a//(10**(i))
    list.append(c)
    a = a - c*(10**(i))

for j in list:
    result += j

print(result)