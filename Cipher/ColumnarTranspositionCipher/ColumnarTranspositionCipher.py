ENC = 0
DEC = 1

def parseKey(key):
    tmp = []
    key = key.upper()           

    for i, k in enumerate(key):                 #i:index k:key
        tmp.append((i,k))                       
    
    tmp = sorted(tmp, key = lambda x:x[1])      #Sort tuples by second element in ascending order
    enc_table = {}
    dec_table = {}

    for i, r in enumerate(tmp):
        enc_table[r[0]] = i
        dec_table[i] = r[0]

    return enc_table, dec_table

def transposition(msg, key, mode):
    msgsize = len(msg)
    keysize = len(key)
    ret = ''
    msg = msg.upper()

    while(msgsize % keysize != 0):      #
        msg += '0'
        msgsize = len(msg)
    enc_table, dec_table = parseKey(key)

    if mode == ENC:
        table = enc_table
    elif mode == DEC:
        table = dec_table

    if mode == ENC:
        buf = ['']*keysize              #Create bufs equal to the number of keysize
        for i, c in enumerate(msg):     
            col = i%keysize
            buf[table[col]] += c
            
        for text in buf:
            ret += text
    
    elif mode == DEC:
        blocksize = int(msgsize/keysize)
        buf = ['']*keysize              #Create bufs equal to the number of keysize
        pos = 0
        for i in range(keysize):
            text = msg[pos:pos+blocksize]
            buf[table[i]] += text
            pos += blocksize

        for i in range(blocksize) :
            for j in range(keysize) :
                if buf[j] [i] != '0':
                    ret += buf[j][i]

    return ret

def main() :

    h = open('DecPlain.txt', 'rt')      #File to be decrypted
    content1 = h.read()
    h.close()

    h = open('EncPlain.txt', 'rt')      #File to be encrypted
    content2 = h.read()
    h.close()   

    h = open('Col_DEC.txt', 'wt+')      
    h.write(transposition(content1, 'PYTHON' ,DEC))
    h.close()

    h = open('Col_ENC.txt', 'wt+')      
    h.write(transposition(content2, 'PYTHON',ENC))
    h.close()

if __name__ == '__main__':
    main()