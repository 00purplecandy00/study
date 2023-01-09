import json

# 아래 코드 수정 금지
movies_json = open("PJT-01/data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성

list = ['id','title','poster_path','vote_average','overview','genre_ids']
for j in range(len(movies_list)):
    for i in list:
        if i in movies_list[j]:
            print(i,movies_list[j][i])
