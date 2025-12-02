def fib(a,b,n):
    if(n>0):
        c=a+b
        print(c,end=' ')
        fib(b,c,n-1)

z=int(input("Enter the total numbers of series : "))        
print(0,1,end=' ')
fib(0,1,z-2)

   
