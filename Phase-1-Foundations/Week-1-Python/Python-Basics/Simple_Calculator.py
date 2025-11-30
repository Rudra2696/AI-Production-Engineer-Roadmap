a=int(input("Enter any integer : "))
b=int(input("Enter any integer : "))
c=int(input("Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 Division \nEnter 5 for remainder\nEnter 6 for quotient\nEntyer 7 for power\nEnter your choice : "))
if(c==1):
    print(f"{a} +  {b} = {a+b}")
elif(c==2):
    print(f"{a} - {b} = {a-b}")
elif(c==3):
    print(f"{a} x {b} = {a*b}")
elif(c==4):
    print(f"{a} /{ b} = {a/b}")
elif(c==5):
    print(f"{a} % {b} = {a%b}")
elif(c==6):
    print(f"{a} // {b} = {a//b}")
elif(c==7):
    print(f"{a} ^ {b} = {a**b}")
else:
    print("Wrong Input!!")