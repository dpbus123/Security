ENC = 0
DEC = 1

def makeDisk(key) :
    keytable = map(lambda x: (chr(x+65), x) , range(26))    # keytable = [('A', 0), ('B',1) ...... ('Z', 25)]
    
    key2index = {}                      #key2index = {'A' : 0, 'B' : 1, ..... 'Z' : 25}
    for t in keytable:
        alphabet, index = t[0], t[1]
        key2index[alphabet] = index

    if key in key2index:
        k = key2index[key]          #Ex)key = 'B' 이면 k = '1'
    else :
        return None, None
    
    enc_disk = {}                       #평문 문자 : 암호문 문자
    dec_disk = {}                       #암호문 문자 : 평문 문자
    
    for i in range(26) :
        enc_i = (i+k)%26
        enc_ascii = enc_i + 65   #암호문 문자
        enc_disk[chr(i+65)] = chr(enc_ascii)    #enc[평문 문자] = 암호문 문자
        dec_disk[chr(enc_ascii)] = chr(i+65)      #dec[암호문 문자] = 평문 문자

    return enc_disk, dec_disk

def caesar(msg, key, mode) :        #ret라는 문자열에 한 문자씩 집어넣는 방식
    ret = ''

    msg = msg.upper()
    enc_disk, dec_disk = makeDisk(key)

    if enc_disk is None:
        return ret
    
    if mode is ENC:
        disk = enc_disk
   
    if mode is DEC:
        disk = dec_disk

    for c in msg:
        if c in disk:
            ret += disk[c]
        else:
            ret += c

    return ret

def caesar2(msg, key, mode):        #msg 문자열을 replace 함수로 변형시키는 방법

    msg = msg.upper()

    enc_disk, dec_disk = makeDisk(key)
    
    if enc_disk is None:
        return ''
    
    if mode is ENC:
        disk = enc_disk

    elif mode is DEC:
        disk = dec_disk
   
    for c in disk:
        if c in msg:
            msg = msg.replace(c,disk[c].lower())
    return msg.upper()

def main() :

    h = open('DecPlain.txt', 'rt')      #복호화 시키고자 하는 파일
    content1 = h.read()
    h.close()

    h = open('EncPlain.txt', 'rt')      #암호화 시키고자 하는 파일
    content2 = h.read()
    h.close()   

    h = open('ca1_DEC.txt', 'wt+')      
    h.write(caesar(content1, 'B' ,DEC))
    h.close()

    h = open('ca1_ENC.txt', 'wt+')
    h.write(caesar(content2, 'B',ENC))
    h.close()

    h = open('ca2_DEC.txt', 'wt+')
    h.write(caesar2(content1, 'B',DEC))
    h.close()

    h = open('ca2_ENC.txt', 'wt+')
    h.write(caesar2(content2, 'B',ENC))
    h.close()
    
    

if __name__ == '__main__':
    main()