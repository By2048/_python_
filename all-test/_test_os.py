import base64


font='''


'''
fontdata=base64.b64decode(font)
file=open('/home/jason/workspace/1.ttf','wb')  
file.write(fontdata)  
file.close()  