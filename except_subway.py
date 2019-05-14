import json
import operator

from model import *
from util import my_dict

file_name = "./data/subway.json"
with open(file_name, encoding="utf-8") as json_file:
    json_data = json.load(json_file)

line=3
my_list=["연신내","충무로","신사","남부터미널","양재","압구정","고속터미널"]
name_list=[]

for i in json_data['lines'][line- 1]["stations"]:
    name_list.append(i['name'])
for my in my_list:
    name_list.remove(my)
for name in name_list:
    print(name,end=",")


# upload_data 폴더 읽기
#
