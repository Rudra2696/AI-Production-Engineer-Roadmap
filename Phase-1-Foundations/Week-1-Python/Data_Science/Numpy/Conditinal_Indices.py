# This program will create an array of 50 elements between 0 to 1000 and then filter it to and remove elements which is less than 50 by boolean conditions and multiply by 2 to remanining elements


import numpy as np

arr = np.random.randint(0,1000,size=(10,5))

arr1 = arr>50

arr2 = arr[arr1]*2

print("\n\tOld Array\n\n",arr,"\n")
print("---------------------------------------------------------------------------\n\n\t\t\t\tNew Array\n")
print(arr2)