import numpy as np

x = np.array([[1, np.nan], [2, 3], [np.nan, np.nan]])
y = np.linspace(-5, 5, 5)
z = np.arange(25).reshape(5,5)
t = np.array([[0, 1], [1, 1], [2, 2]])
e = np.arange(12).reshape(4, 3)

# print(x
#       ,np.isnan(x)
#       ,~np.isnan(x)
#       ,x[np.isnan(x)]
#       ,x[~np.isnan(x)]
#       ,sep="\n-----\n")

# ~ -> invert

print(y
      ,y<=0
      ,y[y<=0]
      ,y[y<=0] + 20
      ,sep="\n-----\n")

new_z = z >= 15
# print(z
#     ,new_z
#     ,new_z[:, 0]
#     ,z[:, new_z[:, 0]]
#     ,z[new_z[:, 0], :]
#     ,z[new_z]
#     ,sep="\n-----\n"
# )

rowsum = t.sum(1)
"""
rowsum = array.sum(1)
columnsum = array.sum(0)
"""

print(t
      ,rowsum
      ,t[rowsum >= 2, :]
      ,t[np.ix_(rowsum >= 2)]
      ,sep="\n-----\n")

rows_e = (e.sum(1) % 2) == 0
rows_e_nz = np.nonzero(rows_e)[0]
columns_e = np.array([0, 2])
# print(e
#       ,np.ndim(rows_e)
#       ,np.ndim(columns_e)
#       ,rows_e
#       ,rows_e_nz
#       ,columns_e
#       ,e[rows_e_nz[:, np.newaxis], columns_e[np.newaxis, :]] # Path 1
#       ,e[np.ix_(rows_e, columns_e)] # Path 2
#       ,sep="\n-----\n")

new_second_z = z[np.array([0, 2, 4]), 0:3]
# print(z
#       ,new_second_z
#       ,sep="\n-----\n")