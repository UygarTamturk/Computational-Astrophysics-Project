import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


# returns the view of the ndarray "a"
b = a[1, 1:]
# difference from a built-in list is where copying a normal list returns its copy, while copying a ndarray returns its view
# when changed, it changes both the view and the original array

zeros = np.zeros([2, 2])
ones = np.ones([3, 2, 5])
# print(zeros
#       ,ones
#       ,a.ndim
#       ,a.shape
#       ,a.size
#       ,a.dtype
#       , sep="\n")


empty_array = np.empty([1, 2, 2])
empty_array[0, 0, 0] = 3


# first number, last number, step size
arange_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 20, 5)
new_a = np.ones([2, 2], dtype=np.int64)
# print(empty_array
#       ,arange_array
#       ,linspace_array
#       ,new_a
#       , sep="\n")

# Sorting

unsorted_a = np.array([[5, 6, 1, 2, 9, 10], [7, 8, 12, 16, 0, 4]], dtype=np.int64)
sorted_a = np.sort(unsorted_a)

print(sorted_a)

a = np.array([1, 2, 3, 4, 5, 6])
reshaped_a = a.reshape(3, 2)

# print(a
#       ,reshaped_a
#       ,sep="\n")

eye = np.eye(3, 3)
diagonal = np.diag([1, 2, 3, 4, 5])
reversed_diagonal = np.diag(diagonal)
vander = np.vander(np.arange(3), 3)

# print(eye
#       ,diagonal
#       ,reversed_diagonal
#       ,vander
#       ,sep="\n")

rng = np.random.default_rng()
random_integers = rng.integers(0, 10, 10, dtype=np.int32)

# print(random_integers)

sliced_a = a[:].copy()

array_1 = np.ones((2, 2))
array_2 = np.zeros((2, 2))
array_3 = np.diag([4, 5])
array_4 = np.eye(2, 2)
block = np.block([[array_1, array_2], [array_3, array_4]])

print(a
      ,sliced_a
      ,sep="\n")

array1 = np.array([[1, 3, 5, 7], [2, 4, 6, 8]]) # (2, 4)
array2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]]) # (4, 2)


# # Matrix Multiplication -> Linear Algebra
# print(array2@array1)


# # Element-wise Multiplication -> Broadcasting (NumPy)
# try:
#     print(array1*array2)

# except Exception as e:
#     print(e, "Cannot Broadcast", sep="\n")



rng = np.random.default_rng(42)


# Broadcastable
"""
Two dimensions are compatible when...
1.they are equal
2.one of them is 1

example:
[3, 1]
[1, 3]
/Broadcastable

[3, 2]
[1, 3]
/Not Broadcastable because 3 != 2

[3, 3]
[3, 3]
/Broadcastable
"""
array3 = rng.random([1, 3])
array4 = rng.random([3, 1])

# print(array3 + array4, array3 * array4, sep="\n")

x = np.arange(10)
y = x[3:5] # View
z = x[2:9:2]
