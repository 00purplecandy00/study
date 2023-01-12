##1

t = int(input())
result = []
a=[]
answer = 0
for i in range(0,t):
	a = list(map(int,input().split()))
	for j in a:
		if j%2 == 1:
			answer += j
	result.append(answer)
	a = []
	answer = 0
for k in range(0,t):
    print('#%s %s'%((k+1),result[k]))
             

##2
t = int(input())
month = ['01','03','05','07','08','10','12','02','04','06','09','11']
month_type1 = ['01','03','05','07','08','10','12']
month_type2 = ['02']
month_type3 = ['04','06','09','11']
day_type1 = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
day_type2 = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
day_type3 = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
answer = []
for i in range(0,t):
    a = input()
    year = a[0:4]
    month1 = a[4:6]
    day1 = a[6:8]
    if month1 not in month:
        answer.append(-1)
    else:
        if month1 in month_type1:
            if day1 not in day_type3:
                answer.append(-1)
            else:
                answer.append("%s/%s/%s"%(year,month1,day1))
        elif month1 in month_type2:
            if day1 not in day_type1:
                answer.append(-1)
            else:
                answer.append("%s/%s/%s"%(year,month1,day1))
        else:
            if day1 not in day_type2:
                answer.append(-1)
            else:
                answer.append("%s/%s/%s"%(year,month1,day1))
              
for j in range(0,t):
    print("#%s %s"%((j+1),answer[j]))
        
            
            
##3
p,k = map(int,input().split())
print(p-k+1)

##4
a = int(input())
list1 = []
for i in range(1,a+1):
    if a%i == 0:
        list1.append(i)
for k in list1:
    print(k,end=" ")
print()