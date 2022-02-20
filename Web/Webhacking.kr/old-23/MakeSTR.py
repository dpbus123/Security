msg = "<script>alert(1);</script>"

cor = ''
for i in msg:
    cor += i
    cor += "%00"

print(cor)
