T = int(input())

for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    평균값 = sum(numbers)/len(numbers)    
    
    
    print(f'#{t} {round(평균값)}')
