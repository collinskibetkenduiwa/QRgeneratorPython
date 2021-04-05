import qrcode


products=['Macbookm1','Intel7gz''AMDRZN7','THENEWBOSTONCRPT']

for product in products:
    qrcode.make(product).save(product+'.png')