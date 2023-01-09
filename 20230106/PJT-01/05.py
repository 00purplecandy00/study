import json

# 아래 코드 수정 금지
movie_json = open("PJT-01/data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

list = ['id','title','vote_average','overview','genre_ids']
dic = {}
for i in list:
    if i in movie:
        dic[i] = movie[i]
print(dic)