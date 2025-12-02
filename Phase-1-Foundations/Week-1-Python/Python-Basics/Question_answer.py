l=['11+55','66-55']
l1=[66,11]
for i in range(2):
    print(f'Q-{i+1} : {l[i]}')
    a=int(input("Answer : "))
    if(a==l1[i]):
        print("Correct Answer!")
    else:
        print("Wrong Answer!")
