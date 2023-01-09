f=open('PJT-01/data/fruits.txt','r',encoding='UTF8')
cnt = 0
list=[]
fruits=f.readlines()
for i in fruits:
    if i[-6:-1:1] == 'berry':        
        if i not in list:
            cnt += 1
            list.append(i)        
print(cnt)
print(list)
f.close()
