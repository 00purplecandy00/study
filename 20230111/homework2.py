##1
print(input().upper())



##2
a=int(input())
sum = 0
i = 1
for i in range(a+1):
    sum += i
print(sum)



##3
a,b = map(int,input().split())
if a==1 and b ==2:
    print('B')
elif a==1 and b ==3:
    print('A')
elif a==2 and b==1:
    print('A')
elif a==2 and b ==3:
    print('B')
elif a==3 and b==1:
    print('B')
elif a==3 and b==2:
    print('A')



##4
print('#++++')
print('+#+++')
print('++#++')
print('+++#+')
print('++++#')

list1 = ['+++++']
for i in range(5):
    list[i] = '#'
for j in range(5):
    print(list1)

##5
a = int(input())
result = 0
while(1):
        i = a//10
        j = a%10
        a = a//10
        result += j
        if i == 0 and j ==0:
            break
print(result)



##6
number = int(input())
for i in range(0,number+1):
    print(2**i,end=" ")
print()