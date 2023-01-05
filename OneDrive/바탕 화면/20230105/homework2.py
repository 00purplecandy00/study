# 문제 1
# 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.

# 단, count() 함수는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# 1
# 출력 예시 2
# 문자열을 입력하세요 > hello hypErgrowth # 사용자 입력
# 1

word = input("문자열을 입력하세요")
count = 0
for i in word:
    if i == 'e':
        count += 1
print(count)
    





# 문제 2
# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.

# 알파벳 모음 : a(A) e(E) i(I) o(O) u(U)

# 단, count() 함수는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# 2
# 출력 예시 2
# 문자열을 입력하세요 > aeiouAEIOU # 사용자 입력
# 10
# 출력 예시 3
# 문자열을 입력하세요 > bcd # 사용자 입력
# 0

word = input("문자열을 입력하세요")
모음 = ['a','A','i','I','u','U','o','O','e','E']
count = 0
for i in word:
    if i in 모음:
        count += 1
print(count)



# 문제 3
# 입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요.

# 입력
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

# ### 이하 문제 해결 코드 작성
# 출력 예시
# 나이 : 24세

age = input("나이를 입력하세요")
dict_variable['나이'] = age
print('나이 : ',dict_variable['나이'])


# 문제 4
# 이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고, 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.

# 출력 예시
# 이름을 입력하세요 > 정우영 # 사용자 입력
# 전화번호를 입력하세요 > 010-1234-5678 # 사용자 입력
# 거주지를 입력하세요 > 서울시 # 사용자 입력
# {'이름': '정우영', '전화번호': '010-1234-5678', '거주지': '서울시'}
# 이름 : 정우영
# 전화번호 : 010-1234-5678
# 거주지 : 서울시

info = {
    "이름":"",
    "전화번호":"",
    "거주지":""    
}

name = input("이름을 입력하세요")
phone = input("전화번호를 입력하세요")
address = input("거주지를 입력하세요")

info["이름"] = name
info["전화번호"] = phone
info["거주지"] = address

print(info)



# 문제 5
# 이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.

# Hint : 딕셔너리 안에 딕셔너리를 넣을 수 있습니다.

# 출력 예시
# 이름을 입력하세요 > 정우영 # 사용자 입력
# 전화번호를 입력하세요 > 010-1234-5678 # 사용자 입력
# 이메일을 입력하세요 > beemo@hphk.kr # 사용자 입력
# 거주지를 입력하세요 > 서울시 # 사용자 입력
# {'정우영': {'전화번호': '010-1234-5678', '이메일': 'beemo@hphk.kr', '거주지': '서울시'}}


info = {
    "이름":"",
    "전화번호":"",
    "이메일":"",
    "거주지":""    
}

name = input("이름을 입력하세요")
phone = input("전화번호를 입력하세요")
email = input("이메일을 입력하세요")
address = input("거주지를 입력하세요")

info["이름"] = name
info["전화번호"] = phone
info["이메일"] = email
info["거주지"] = address

info1 = {
    info["이름"]: {
        "전화번호":info["전화번호"],
        "이메일":info["이메일"],
        "거주지":info["거주지"]
    }
}

print(info1)

# 문제 6
# 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# h 1
# e 1
# l 2
# o 1
# 출력 예시 2
# 문자열을 입력하세요 > else # 사용자 입력
# e 2
# l 1
# s 1


word = input("문자열을 입력하세요")
list = []
dic = {
    
}
list1 = []
list2 = []
l = 0
for i in word:
    list.append(i)

j = 0
k = 0
for j in range(len(word)):
    for k in range(len(word)):
        if word[j] == list[k]:
            if word[j] not in list1:
                list1.append(word[j])
                list2.append(1)
            else:
                p = 0
                p = j%(len(list1))
                list2[p] += 1
            break
                

print(list1)
print(list2)
    
for l in range(len(list1)):
    dic[list1[l]] = list2[l]
print(dic)

