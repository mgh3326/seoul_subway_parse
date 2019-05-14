import pymongo
import json

from config.settings import DATABASE_CONFIG
from model import *

line = 1
subway_list = []

for line in range(1, 9):
    file_name = "./data/%dline.json" % line
    with open(file_name, encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    station_list = []

    for oh in json_data["lineList"]:
        ad_list = []

        ad_list.append(Ad(name="천장걸이형 포스터", company="나스미디어", spec="200*30", price=500000, tags=["포스터",
                                                                                                "천장걸이",
                                                                                                "전동차내"], desc="쌉니다요"))
        ad_list.append(
            Ad(name="스크린 도어 조명 광고", company="나스미디어", spec="500*30", price=530000, tags=["조명광고", "스크린도어"],
               desc="빨리 사세요 곧 품절입니다."))
        station = Station(oh["statnNm"], ads=ad_list)
        station_list.append(station)

    subway = Subway(line, station_list)
    subway_list.append(subway)
subway_list = SubwayList(subway_list)
data = json.dumps(subway_list, default=lambda x: x.__dict__, ensure_ascii=False)

myclient = pymongo.MongoClient(DATABASE_CONFIG['host'], username=DATABASE_CONFIG['user'], password=DATABASE_CONFIG['password'], authSource=DATABASE_CONFIG['authSource'])
mydb = myclient[DATABASE_CONFIG['dbname']]
mycol = mydb[DATABASE_CONFIG['collection_name']]
dict2 = json.loads(data)
mydict = {"name": "John", "address": "Highway 37"}
# mycol.insert(subway_list)
x = mycol.insert_one(dict2)
