from random import choice

l=[1,2,3]
y=choice(l)
while(True):
    try :
        x=int(input("Enter 1 for stone\nEnter 2 for Sizer\nEnter 3 for Paper\nEnter your choice(1/2/3 only) : "))
        if (x in l):
            break
        else: 
            print(f"You entered {x} which is not valid input\n please enter 1/2/3 only")
    except Exception as e :
        
        print("Wrong input \n Please enter 1/2/3 only")

dict= {
    1 : 'stone',
    2 : 'sizer',
    3 : 'paper'
}

print(f"You selected {dict.get(x)}")
if(x==y):
    print("It's tie!!")
elif(x==1 and y==2):
    print("you Won!!")
elif(x==1 and y==3):
    print("You lose!")
elif(x==2 and y==1):
    print("You lose!")
elif(x==2 and y==3):
    print("You Won!!")
elif(x==3 and y==1):
    print("You Won!!")
elif(x==3 and y==2):
    print("You lose!")
else:
    print("Something went wrong")
    

