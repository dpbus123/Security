import requests as rq       #pip install requests
url = "https://webhacking.kr/challenge/bonus-6/lv2.php"
res = rq.post(url, data={"post": "hehe", "post2": "hehe2"})
print(res.text);
