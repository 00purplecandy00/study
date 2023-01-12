f=open('PJT-01/data/fruits.txt','r',encoding='UTF8')
dic={}
fruits=f.readlines()
for i in fruits:   
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
        
print(dic)
f.close()