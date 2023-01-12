word = 'banana'

if 'a' in word:
    print(1)

for i in range(len(word)):
    if word[i] == 'a':
        print(1)
        break
print('===================')
# 'a'를 제외하고 출력하시오
# continue :다음 반복을 실행
for i in range(len(word)):
    if word[i] == 'a':
        continue
    print(word[i])

for i in range(len(word)):
    if word[i] != 'a':
        print(word[i])

