from Crypto.Hash import MD5         #pip install pycryptodome
import requests as rq               #pip install requests
import time


msg = str(int(time.time()))

m = MD5.new()
m.update(msg.encode()) 

url = "https://webhacking.kr/challenge/bonus-6/l4.php"

cip = m.hexdigest()
print(cip)
print(msg)

res = rq.get(url , params={"password" : cip})

print(res.text)
