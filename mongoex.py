from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
movie = db.movies.find_one({'title': '사운드 오브 뮤직'})
star = movie['star']
print(star)

star_movie = db.movies.find({'star': star})
db.movies.update_many({'star':star},{'$set': {'star': 0}})
