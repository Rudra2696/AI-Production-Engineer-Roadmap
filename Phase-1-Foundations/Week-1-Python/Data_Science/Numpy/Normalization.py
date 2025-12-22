# This program will take average of each row and then subratct the average from it's respective row


import numpy as np

arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

arr1 =  arr.mean(axis=1, keepdims=True)  # keepdims will make shape remains same 

print(arr1)
print(arr - arr1)