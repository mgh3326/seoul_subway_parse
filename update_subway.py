import json
import operator
import os

from model import *
from util import my_dict

file_name = "./data/subway.json"
with open(file_name, encoding="utf-8") as json_file:
    json_data = json.load(json_file)
folder_name = "./upload_data"

file_name_list = ["ok.json", "inpung.json", "n01.json", "ujin.json"]
for _file_name in file_name_list:
    file_name = os.path.join(folder_name, _file_name)
    with open(file_name, encoding="utf-8") as json_file:
        input_json_data = json.load(json_file)
    datas = input_json_data['datas']
    for data in datas:
        if data["stationName"] == "":
            for _data in json_data['lines'][data['lineNumber'] - 1]["stations"]:
                ad = Ad(name=data['name'], company=data['company'], spec=data['spec'], price=data['price'],
                        tags=data['tags'],
                        desc=data['desc'], types=data['types'])
                _data['ads'].append(ad)
        else:

            for station_name in data['stationName'].split(","):
                station_name_strip = station_name.strip()
                if my_dict.get(station_name_strip) is not None:
                    station_name_strip = my_dict.get(station_name_strip)

                find_data = next(item for item in json_data['lines'][data['lineNumber'] - 1]["stations"] if
                                 item["name"] == station_name_strip)
                ad = Ad(name=data['name'], company=data['company'], spec=data['spec'], price=data['price'],
                        tags=data['tags'],
                        desc=data['desc'], types=data['types'])
                find_data['ads'].append(ad)
data = json.dumps(json_data, default=lambda x: x.__dict__, ensure_ascii=False)
f = open("./data/subway_2.json", 'w', encoding='utf-8')
f.write(data)
f.close()
print("Complete")
# upload_data 폴더 읽기
#
