import numpy as np

# creating matrices
matrix = np.array([[1, 2, 3], [4, 5 ,6], [7, 8, 9]])

# reshaping arrays
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
# print(a 
#     ,b
#     ,sep="\n")

# slicing matrices
c = np.array([[1, 2, 3]
              ,[4, 5, 6]
              ,[7, 8, 9]])
# print(c[1:, 1:])

# sorting arrays
d = np.array([1, 6, 7, 2, 3, 9, 0])
sorted_d = np.sort(d)

# print(d
#       ,sorted_d
#       ,sep="\n")

# arithmetic operations

e = np.array([1, 2, 3])
f = np.array([2, 3, 4])

print(e + f
      ,e - f
      ,e * f
      ,e / f
      ,sep="\n")