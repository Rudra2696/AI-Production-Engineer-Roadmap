try:
    s = input("Type sentence : ")

    s=s.lower()
    l= s.split()
    l1=[]

    for i in l:
        if(not(i in l1)):
            l1.append(i)

    print("Occurrences")
    
    for i in l1:
        c=0
        for j in range(len(l)):
            if (i==l[j]):
                c+=1
        print(f"{i.capitalize()}  : {c}")
    
except Exception as e:
    print("Something Went Wrong !!")