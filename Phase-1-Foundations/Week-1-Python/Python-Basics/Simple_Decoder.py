n=input("Enter encoded message : ")
if(len(n)<3):
    s1=n[1]+n[0]
else:
    l=[i for i in n]
    i=0
    while(True):
        if(i<3):
            l.pop(0)
            i+=1
        elif(i<6 and i>2):
            l.pop()
            i+=1
        else:
            break
    s1=l[len(l)-1]
    l.pop()
    l.insert(0,s1)
    s1=''
    for i in range(len(l)):
        s1+=l[i]
print("Decoded messgae : ",s1)


