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

## Short hand if else

# a=300
# b=80
# print("A") if(a>b) else print('=') if (a==b) else print('B')
# c= 1 if(a>b) else 0
# print(c)

## Enumerate function

# s='hello'

# for index, character in enumerate(s,start=1):
#     print("It's l",index) if(character=='l') else ''

## passing function to function lambda function

# def add(fn,value):
#     print('cube=',fn(value))

# add(lambda x : x*x*x,3)

# def he(*a):
#     print(a)

# he(5,7,9)    


## Map function

# print(list(map(lambda x : x*x, [1,8,9,5,6])))

## Filter function
# print(list(filter(lambda x : x>3,[1,2,3,5,67])))

# # Reduce function
# from functools import reduce
# print(reduce(lambda x,y : x+y,[1,23,4,56,7,88,9]))

# # constructor

# class Hey:
    
#     def __init__(self,a=8,b=8):
#         self.a=a
#         self.b=b
    
#     def avg(self):
#         print("Average = ",(self.a+self.b)/2)

# c=Hey()
# c.avg()
# d=Hey(5,5)
# d.avg()
    
# # Decoraters 

# def dec(fx):
#     def mfx():
#         print("Hello!")
#         fx()
#         print("Thankyou for choosing us!!")
#     return mfx

# @dec
# def hey():
#     print("Wow")

# hey()

# # Decoraters with arguments

# def deco(fx):
#     def mfx(*args,**kwargs):
#         print("Hello!!")
#         fx(*args,**kwargs)
#         print("Thankyou for choosing us!!")
#     return mfx

# @deco
# def add(a,b):
#     print(a+b)

# add(5,6)

import time

print(time.strftime('%H:%M:%S',time.localtime()))