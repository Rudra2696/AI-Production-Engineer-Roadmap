
a=int(input("Enter the total number of series : "))
a1=0
a2=1
print('0  1 ',end=' ')
for i in range(a-2):
    a3=a1+a2
    print(a3,end='  ')
    a1=a2
    a2=a3