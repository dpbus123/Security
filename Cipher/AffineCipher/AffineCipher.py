ENC = 0
DEC = 1

def makeDisk(k1,k2):
    enc_disk = {}
    dec_disk = {}

    for i in range(26):
        enc_i = (k1*i+k2)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i+65)
        

    return enc_disk, dec_disk

def affine1(msg,k1,k2,mode):
    enc_disk, dec_disk = makeDisk(k1,k2)
    ret = ''
    
    msg = msg.upper()

    if enc_disk == None:
        return ret

    if mode == ENC:
        disk = enc_disk
    elif mode == DEC:
        disk = dec_disk

    for i in msg:
        if i in disk:
            ret += disk[i]
        else:
            ret += i
    return ret

def affine2(msg,k1,k2,mode):
    enc_disk, dec_disk = makeDisk(k1,k2)

    msg = msg.upper()

    if enc_disk == None:
        return ''

    if mode == ENC:
        disk = enc_disk
    elif mode == DEC:
        disk = dec_disk

    for c in disk:
        if c in msg:
            msg = msg.replace(c,disk[c].lower())
            
    msg = msg.upper()

    return msg

def main():
    k1, k2 = 7, 21
    h = open('DecPlain.txt', 'rt')      
    content1 = h.read()
    h.close()

    h = open('EncPlain.txt', 'rt')      
    content2 = h.read()
    h.close()   

    h = open('af1_DEC.txt', 'wt+')      
    h.write(affine1(content1, k1,k2 ,DEC))
    h.close()

    h = open('af1_ENC.txt', 'wt+')
    h.write(affine1(content2,  k1,k2,ENC))
    h.close()

    h = open('af2_DEC.txt', 'wt+')
    h.write(affine2(content1, k1,k2,DEC))
    h.close()

    h = open('af2_ENC.txt', 'wt+')
    h.write(affine2(content2, k1,k2,ENC))
    h.close()
    

if __name__ == '__main__':
    main()
