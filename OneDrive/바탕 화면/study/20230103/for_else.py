word = 'mangoe'

# 'e'가 있으면 1을 출력
# 'e'가 아니면 0을 출력
is_end = False
for char in word:
    if char == 'e':
        print(1)
        is_end = True
        break

print('=====================')    
if is_end:
    print(1)
else:
    print(0)

print('=====================') 
for char in word:
    if char == 'e':
        print(1)
        break
else:
    print(0)

