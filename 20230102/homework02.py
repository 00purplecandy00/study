number1 = int(input("숫자를 입력해주세요"))
print(number1+10)

food = input("좋아하는 음식을 입력해주세요")
print("좋아하는 음식 : %s"%food)

name = input("이름을 입력해 주세요")
birth_year = int(input("태어난 년도를 입력해주세요"))
print("저의 이름은 %s이고, 올해 나이는 %s입니다"%(name,(2023-birth_year+1)))

first1 = input("첫 번째 문장을 입력해주세요")
second1 = input("두 번째 문장을 입력해주세요")
print(first1+second1)

number2 = int(input("숫자를 입력해주세요"))
print(number2*(-1))

first2 = int(input("첫 번째 숫자를 입력해주세요"))
second2 = int(input("두 번째 숫자를 입력해주세요"))

print("더하기 연산 : %s"%(first2 + second2))
print("빼기 연산 : %s"%(first2 - second2))
print("곱하기 연산 : %s"%(first2 * second2))
print("몫 연산 : %s"%(first2//second2))
print("나머지 연산 : %s"%(first2%second2))

first3 = int(input("첫 번째 숫자를 입력해 주세요"))
second3 = int(input("두 번째 숫자를 입력해주세요"))
third3 = int(input("세 번째 숫자를 입력해주세요"))
print((first3+second3+third3)/3)

list1 = []

list1.append(int(input("첫 번째 숫자를 입력해주세요")))
list1.append(int(input("두 번째 숫자를 입력해주세요")))
list1.append(int(input("세 번째 숫자를 입력해주세요")))
list1.append(int(input("네 번째 숫자를 입력해주세요")))
list1.append(int(input("다섯 번째 숫자를 입력해주세요")))
print(list1)

string3 = input("문자열을 입력해주세요")
number3 = int(input("숫자를 입력해주세요"))
print(string3*number3)

number4 = int(input("첫 번째 숫자를 입력해주세요"))
print(number4)
number4 += int(input("두 번째 숫자를 입력해주세요"))
print(number4)
number4 += int(input("세 번째 숫자를 입력해주세요"))
print(number4)
number4 += int(input("네 번째 숫자를 입력해주세요"))
print(number4)
number4 += int(input("다섯 번째 숫자를 입력해주세요"))
print(number4)