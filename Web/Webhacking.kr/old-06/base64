import base64
import sys

id = 'admin'            
pw = 'nimda'               


id = id.encode('utf-8')
pw = pw.encode('utf-8')


for i in range(20):                 #Encode admin and nimda 20 times
    id = base64.b64encode(id)
    pw = base64.b64encode(pw)

pw = pw.decode()                   
id = id.decode()                    #Decoding

pw.replace("1","!")
pw.replace("2","@")
pw.replace("3","$")
pw.replace("4","^")
pw.replace("5","&")
pw.replace("6","*")
pw.replace("7","(")
pw.replace("8",")")

id.replace("1","!")
id.replace("2","@")
id.replace("3","$")
id.replace("4","^")
id.replace("5","&")
id.replace("6","*")
id.replace("7","(")
id.replace("8",")")                     #Replace




print('id = ' + id)                 #Print
print('pw = ' + pw)
