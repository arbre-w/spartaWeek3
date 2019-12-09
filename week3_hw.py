import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.hwdb
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908', headers=headers)



soup = BeautifulSoup(data.text, 'html.parser')
tag = soup.select(' .newest-list >.music-list-wrap > .list-wrap > tbody > tr')
for t in tag:
    title = t.select_one('.list > .info > a.title').text.strip()
    span_ele = t.find_all("span")
    for span in span_ele:
        span.extract()

    rank = t.select_one('.list > .number').text.strip()
    singer = t.select_one('.list > .info > .artist').text.strip()
    #print(rank, title, singer)
    doc = {
        'rank' : rank,
        'title' : title,
        'singer' : singer
    }
    db.tag.insert_one(doc)



