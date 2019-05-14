import requests

from config.settings import API_KEY

headers = {'Content-Type': 'application/json; charset=utf-8'}

for i in range(1, 9):
    url = "http://swopenapi.seoul.go.kr/api/subway/%s/json/stationByLine/0/299/%d호선" % (API_KEY['key'], i)

    response = requests.get(url, headers=headers)
    f = open("./data/%dline.json" % i, 'w', encoding='utf-8')
    f.write(response.text)
    f.close()
