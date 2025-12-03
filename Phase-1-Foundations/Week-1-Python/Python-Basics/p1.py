## I practiced python randomly in this file

# print("Hello World!")
# print(7,"hello",9,sep="~")
# print(5**2)
# a='hello-Bhai'
# print(a.split('-'))
# b="hellooooo            "
# print(b.rstrip().rstrip('o')+'b')
# c='this Is my laptop. Who Are You?'
# print(c.capitalize())
# d='    t    '
# print(d.isspace())


# x=5
# match x:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case _:
#         print(5)

# for i in range(1,5,2):
#     print(i)


## List comprehension
# lst=[i for i in range(15)]
# print(lst)

# print([i for i in range(15) if i%2==0])

# l=[4,32,6,7,2,9]
# l.sort(reverse=True)
# print(l)

# # to create tuple of single element 
# t=("Hello",)
# print(t)

# #to print {}
# a=4
# print(f'hey here value of {{a}} is {a}')

## Doc string

# def square(n):
#     '''This function will take n and does the square of n and then print it'''
#     print(n*n)

# square(5)
# print(square.__doc__)

# # To create an empty set 
# s = set()
# b={}
# print(type(s),type(b))

# Short hand if else

a=300
b=80
print("A") if(a>b) else print('=') if (a==b) else print('B')
c= 1 if(a>b) else 0
print(c)