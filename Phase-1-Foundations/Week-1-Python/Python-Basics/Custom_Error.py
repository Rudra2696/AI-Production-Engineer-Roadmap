# This program will throw an error if user enter anything except integer, and "quit"

n=input("Enter any integer : ")
if(n.lower()=='quit' or n.isnumeric()):
   print(n)
else:
   raise ValueError("Wrong Input!!")

