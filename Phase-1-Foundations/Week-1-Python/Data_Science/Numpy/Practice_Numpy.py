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

# # Arithmatic operation

# arr = np.array([1,2,3])
# arr1 = np.array([4,5,6])

# print(arr1+arr)  # Addition
# print(arr1-arr)  # Subtraction
# print(arr1/arr)  # Division
# print(arr1//arr) # Floor division (integer division return only integer value)
# print(arr1*arr)  # Multiplication
# print(arr1**arr)  # Exponantial (power)
# print(arr1%arr)  # Remainder


# # For squareroot

# arr = np.array([1,4,25,81,9])
# print(np.sqrt(arr))

# # For exponantial (power of e)

# arr = np.exp([3,4,6,7])
# print(arr)

# # For sine function

# arr = np.array([0, np.pi/2, np.pi])
# print(np.sin(arr))

# # Indexing & Slicing 

# arr = np.array([1,2,3,4,5,6])
# print(arr[3])
# print(arr[1:4])  # ending index will not included 
# print(arr[1:4:2])   
# print(arr[-3:-1])
# print(arr[-1:-4:-1])
# print(arr[-1:-4:-2])

# # Indexing & Slicing in 2-D

# arr = np.array([[1,2,3],
#                [4,5,6],
#                [7,8,9]])

# print(arr[0:2,1:])
# print(arr[0,-1])

# # Take function

# arr = np.array([1,2,3,4,5])
# ind = [2,4]
# print(np.take(arr,ind))

# # To iterate array (does not matter it's shape)

# arr = np.array([[1,2,4],
#                 [3,5,6]])

# for i in np.nditer(arr):
#     print(i,end="  ")

# # Enumerate function

# arr = np.array([[1,2,4],
#                  [3,5,6]])


# for ind, i in np.ndenumerate(arr):
#     print(ind,i)

# # View & Copy

# arr = np.array([1,2,3,4,5,6,7])
# view = arr[1:4]
# copy1 = arr[1:4].copy()
# print(view)
# print(copy1)
# arr[2]=10    # If we modify array so it will reflect in view also but not in copy
# print(view)
# print(copy1)

# # Transpose method

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr.transpose())

# # To swap axes (swap rows and columns)

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr.shape)
# swap = np.swapaxes(arr,0,1)
# print(swap.shape)

# # To concatenate array (combine array)

# arr = np.array([1,2])
# arr1 = np.array([3,4])
# print(np.concatenate((arr,arr1)))

# # Vertical stack & horizontal stack

# arr = np.array([[1,2],
#                 [3,4]])
# arr1 = np.array([[5,6],
#                 [7,8]])

# print(np.vstack((arr,arr1)))  # Verical stack
# print("-------")
# print(np.hstack((arr,arr1)))  # Horizontal stack

# # Stack method

# arr = np.array([[1,2],
#                 [3,4]])
# arr1 = np.array([[5,6],
#                 [7,8]])

# print(np.stack((arr,arr1),axis=0))  # 0 for column
# print("-------")
# print(np.stack((arr,arr1),axis=1))  # 1 for row

# # Split

# arr = np.array([[1,2],
#                 [3,4],
#                 [5,6],
#                 [7,8]])

# print(np.split(arr,4))
# print("-------")
# print(np.vsplit(arr,2))  # Vertical split
# print("-------")
# print(np.hsplit(arr,2)) # Horizontal split

# # Repeat method (repeats the elements)

# arr  = np.array([1,2,3])
# print(np.repeat(arr,2))

# # Tile method (repeat whole array)

# arr  = np.array([1,2,3])
# print(np.tile(arr,2))

# # Aggregate function

# arr = np.array([1,2,3,4,5])
# print(np.sum(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.mean(arr))
# print(np.median(arr)) # Middle element
# print(np.var(arr))    # How far numbers are from the average
# print(np.std(arr))    # Squareroot of varience

# # Axis base operation of aggregate function

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(np.sum(arr, axis=0))  # 0 for column
# print(np.min(arr, axis=0))  # 1 for row
# print(np.max(arr, axis=0))
# print(np.mean(arr, axis=0))
# print(np.median(arr, axis=0)) # Middle element
# print(np.var(arr, axis=0))    # How far numbers are from the average
# print(np.std(arr, axis=0))    # Squareroot of varience

# # Cumulative sum (running total) & Cumulative product (running product) 

# arr = np.array([1,2,3])
# print(np.cumsum(arr))  # cumulative sum -> [(1) (1+2) (1+2+3)]
# print(np.cumprod(arr)) # cumulative product -> [(1) (1*2) (1*2*3)]

# # Condition based choice

# arr = np.array([1,2,3,4])
# print(np.where(arr<3,'low','high')) # like if -else (condition, true, false) 
# print(np.where(arr<3))              # To get the position of element which satisfy condition 
# print(np.argwhere(arr>3))           # return the index where the condition satisfies
# print(np.nonzero(arr))              # return the index of non-zero elements
# print(np.logical_and(arr>1,arr<4))  # return true false according to both 'AND'condition
# print(np.logical_not(arr>1,arr<4))  # return true false according to both 'NOT 'condition
# print(np.logical_or(arr>1,arr<4))   # return true false according to both 'OR' condition
# print(np.logical_xor(arr>1,arr<4))  # return true false according to both 'xOR' condition

# Vectorization (To apply custom function on array)

# def sqr(arr):
#     return arr*arr

# arr = np.array([4,3,9,5])
# vectorize = np.vectorize(sqr)
# print(vectorize(arr))


# # To store and check none, infinite (+ve, -ve) values

# arr = np.array([3,np.nan,9,np.inf,8,-np.inf])

# print(np.logical_or(np.isnan(arr),np.isinf(arr)))


# # To replace none and infinite value

# arr = np.array([3,np.nan,9,np.inf,8,-np.inf])

# new = np.nan_to_num(arr)
# print(new)