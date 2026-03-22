import numpy as np

rng = np.random.default_rng(42)

x = np.arange(10)
y = x[3:5] # View
z = x[2:9:2]

# x[n:m] --> n >= x > m --> x => [n, m-1] or [n, m)
x[3:5] = [10,11]
# print(x
#       ,y
#       ,z
#       ,sep="\n")

t = np.array([[[1, 2, 3, 4, 5]
             ,[6, 7, 8, 9, 10]
             ,[11, 12, 13, 14, 15]
             ,[16, 17, 18, 19, 20]
             ,[21, 22, 23, 24, 25]]
             ,[
               [1, 2, 3, 4, 5]
             ,[6, 7, 8, 9, 10]
             ,[11, 12, 13, 14, 15]
             ,[16, 17, 18, 19, 20]
             ,[21, 22, 23, 24, 25]
             ]])
d = t[..., 2] # t[..., 2] == t[:, :, 2]

# print(t
#       ,d
#       ,sep="\n")

n = rng.random([3,], dtype=np.float32)
m = n[:, np.newaxis]
v = n[np.newaxis, :]

"""
n -> [1, 2, ..., n] (,10)=> m = n[:, np.newaxis] -> creates new dimension -> (10, 1)
                         => v = n[np.newaxis, :] -> creates new dimension -> (1, 10)
"""

# print(n
#       ,m
#       ,v
#       ,m * v
#       ,m.shape
#       ,v.shape
#       ,n.shape
#       ,sep="\n")

q = np.arange(25).reshape(5, 5)
f = q[np.array([2, 3]), np.array([2, 3])]
l = q[np.array([0, 2, 4]), 1]
k = q[np.array([0, 2, 4])]

# print(q
#       ,f
#       ,l
#       ,k
#       ,sep="\n")

j = np.arange(10).reshape(2, 5)
j_rows = np.array([0, 1], dtype=np.intp)
j_columns = np.array([2, 4], dtype=np.intp)

print(j
      ,j[np.ix_(j_rows, j_columns)]
      ,j[j_rows, j_columns]
      ,sep="\n")