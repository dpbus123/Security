def makeCodebook() :
    decbook = {'5' : 'a', '2' : 'b', '#' : 'd', '8' : 'e', '1' : 'f', '3' : 'g', '4' : 'h', '6' : 'i', '0' : 'l', '9' : 'm', '*' : 'n', '%' : 'o', '=' : 'p', '(' : 'r', ')' : 's', ';' : 't', '?' : 'u' , '@' : 'v', ':' : 'y', '7' : ' '}
    encbook = {}
    for A in decbook:
        val = decbook[A]
        encbook[val] = A 
    return encbook, decbook

def encrypt(msg, encbook) :
    for B in encbook :
        if B in encbook :
            msg = msg.replace(B,encbook[B])
    return msg

def decrypt(msg, decbook) :
    for B in decbook :
        if B in decbook :
            msg = msg.replace(B, decbook[B])
    return msg

if __name__ == '__main__' :
    h = open('plain1.txt', 'rt')
    content = h.read()
    h.close()

    encbook, decbook = makeCodebook()
    content = encrypt(content, encbook)

    h = open('encryption.txt', 'wt+')
    h.write(content)
    h.close()
    
    h = open('plain2.txt', 'rt')
    content = h.read()
    h.close()

    content = decrypt(content,decbook)
    
    h = open('decryption.txt', 'wt+')
    h.write(content)
    h.close()
