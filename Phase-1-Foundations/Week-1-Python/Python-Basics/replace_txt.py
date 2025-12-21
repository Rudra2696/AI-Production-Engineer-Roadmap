
with open ("file.txt","r") as f:
    str = f.read()
    str = str.replace('text','hello')

with open ('result.txt','w') as f1:
    f1.write(str)