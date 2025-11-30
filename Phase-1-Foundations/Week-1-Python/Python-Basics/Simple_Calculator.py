a=int(input("Enter any integer : "))
b=int(input("Enter any integer : "))
c=int(input("""Enter 1 for Addition
            Enter 2 for Subtraction
            Enter 3 for Multiplication
            Enter 4 Division 
            Enter 5 for remainder
            Enter 6 for quotient
            Entyer 7 for power
            Enter your choice : """))
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