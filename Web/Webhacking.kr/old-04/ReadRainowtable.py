f= open("table.txt",'r')

while True:
    line = f.readline()
    if 'str' in line:
        print(line)
    if not line:
        break
print("0")
