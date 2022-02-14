import hashlib

f = open("table.txt", 'w')


for i in range(10000000,100000000):
    k = str(i)+"salt_for_you"
    for j in range(500):
        h = hashlib.sha1()
        h.update(k.encode('utf-8'))
        k = h.hexdigest()
    print(str(i) + "is complete")
    f.write(str(i) +" : "+k+"\n");
f.close
