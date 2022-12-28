import numpy as np

a = [1,2,11,6,8,18,2]
na = np.array(a)

# Imprime el arreglo
# print(na)

# Imprime el tipo de arreglo type()
# print(type(na))

# .shape: It's a rank 1 numpy array with 7 items
# print(na.shape)

#  Let's print out an element at index 2
# print(na[2])

# Isolate an entire chunk based on start index-end index
# print out values at start to end-1 index Location
# print(na[1:5])

# Use a step of two
# print(na[1:5:2])

# negative index
# print out values at start to end+1 index location
# print(a[-7:-4])

# print last item
# print(a[-1])

#  items start at one index and all the way to the end
# print(a[4:])

# Print items from beginning through end -1
# print(a[:4])

# Copy an array
# b = a[:]
# print(b)

# Concatenate two numpy arrays
# x = np.array([2,6,8,4])
# y = np.array([11,8,2])
# z = np.concatenate([x,y])
# print(z.shape)

# Multi-dimensional array operations
arr = [[1,2,3,4],[3,4,5,6],[7,8,9,6],[12,7,10,9],[2,11,8,10]]
narr = np.array(arr)
# print(narr)

#  Print second row at row index 1
# print(narr[0])

# Print 3rd row, at row index 2
# print(narr[2])

# Print contents of row with index 0 and column with index 1
# print(narr[0,1])

#  Replace value at location
# narr[3,0] = 14
# print(narr)

# get the last row
# print(narr[-1])

# get the 2nd last
# print(narr[-2])

# print rows and columns
#  #rows: 1 to 4-1 and columns 2 to 5-1 
# print(narr)
# print(narr[1:4,2:5])

# concatenation row and column wise
a = np.array([[1,2],[3,4]])
b = np.array([5,6])

# c = np.row_stack((a,b))
c = np.c_[a,b]

print(c)