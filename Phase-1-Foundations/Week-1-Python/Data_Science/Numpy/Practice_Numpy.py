import numpy as np

# # To check dimensions

# arr = np.array([1,5,9,3,7])
# print(arr.ndim)

# # To create array like list comprehension 

# arr = np.arange(1,10,2)
# print(arr)

# # To divide number equally in part and then store it

# arr = np.linspace(0,1,5)
# print(arr)

# # Logarithmic scale array (base = 10 by default)

# arr = np.logspace(1,4,4,base=2)
# print(arr)

# # To create an matrix of zeros

# arr = np.zeros(5)
# arr1 = np.zeros([3,3])
# print(arr)
# print("----------------")
# print(arr1)

# # To create an matrix of ones

# arr = np.ones(5)
# arr1 = np.ones([3,3])
# print(arr)
# print("----------------")
# print(arr1)

# # To create an matrix of our choice value

# arr = np.full(5,6)
# arr1 = np.full([3,3],6)
# print(arr)
# print("----------------")
# print(arr1)

# # To create empty matrix (it gives values which were already allocated on that memory but it is empty it means uninitialized matrix)

# arr = np.empty(5)
# arr1 = np.empty([3,3])
# print(arr)
# print("---------------------------------------------------")
# print(arr1)

# # To create matrix by random float

# arr = np.random.rand(2,3)
# print(arr)

# # To create matrix by random float from standard normal distribution (near to zero)

# arr = np.random.randn(2,3)
# print(arr)

# # To create matrix by random integer

# arr = np.random.randint(0,9,size=(3,2))
# print(arr)

# # To check Datatype of array

# arr = np.array([1,2,34.7,8,0])
# print(arr.dtype)

# # To type casting datatype of array

# arr = np.array([1,2,3,4,8,0], dtype=np.float32)
# print(arr.dtype)

# # To type casting datatype of array by creating new array

# arr = np.array([1,2,3,4,8,0])
# arr1=arr.astype(np.float32)
# print(arr1.dtype)

# # To create multi dimension array by lists

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr)

# # To get the shape of array (number of rows and columns)

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr.shape)

# # To get the size of array (total elements)

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr.size)

# # To check how many bits were used by each element

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr.itemsize)

# # To reshape the shape of array without modifing existing data

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr.reshape(3,2))

# # To convert any dimension array into 1 dimension array

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr.ravel())   # ravel will not create new array it will return view only if possible
# print(arr.flatten()) # flatten will always create new array

# # If you use ravel and you change any element of origin array so it will change ravel also.
# # If you use flatten and you change any element of origin array so it will not change flatten.

# arr = np.array([[1,2,3],
#                  [4,5,6]])
# arr1 = arr.ravel()
# arr2 = arr.flatten()
# arr[0,0]=9
# print(arr1)
# print(arr2)

# Arithmatic operation

arr = np.array([1,2,3])
arr1 = np.array([4,5,6])

print(arr1+arr)  # Addition
print(arr1-arr)  # Subtraction
print(arr1/arr)  # Division
print(arr1//arr) # Floor division (integer division return only integer value)
print(arr1*arr)  # Multiplication
print(arr1**arr)  # Exponantial (power)
print(arr1%arr)  # Remainder