import json

# 아래 코드 수정 금지
movie_json = open("PJT-01/data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("PJT-01/data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성

list = []
for i in movie:
    if i == 'genre_ids':
        for k in genres_list:
            for j in range(len(movie[i])):
                if movie[i][j] == k["id"]:
                    list.append(k["name"])
                    
dic = {}

list1 = ["id","title","vote_average","overview","genre_ids"]

for k in list1:
    if k != 'genre_ids':
        dic[k] = movie[k]

    else:
        dic["genre_names"] = list  
            
    

print(dic)