h = open('DecPlain.txt','rt')
msg = h.read()
h.close

msg = msg.upper()

for j in range(26):
    attackmsg = ''
    for i in msg:
        if ord(i)>=65 and ord(i)<=95:               #If letter is alphabet
            alphabet = (ord(i)+j)%26 + 65
            attackmsg += chr(alphabet)
        else:                                       #If letter is not alphabet ex)'!'
            attackmsg += i
    print(attackmsg)