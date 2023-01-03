dust = int(input("미세먼지의 농도를 입력하세요"))
 
if dust >= 0 and dust <= 30:
    print('좋음')
elif dust > 30 and dust <=80:
    print('보통')
elif dust > 80 and dust <= 150:
    print('나쁨')
elif dust >150:
    print('매우 나쁨')
else:
    print('양수를 입력해 주세요')