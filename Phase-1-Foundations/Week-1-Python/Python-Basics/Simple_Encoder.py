n=input("Enter your message : ")
if(len(n)<3):
    
    s=n[1]+n[0]
else:
    s=''
    l=[i for i in n]
    s1=l[0]
    l.append(s1)
    l.pop(0)
    l.insert(0,'z')
    l.insert(1,'e')
    l.insert(2,'d')
    l.append('i')
    l.append('p')
    l.append('o')
    for i in l:
        s+=i
print("Encoded message : ",s)