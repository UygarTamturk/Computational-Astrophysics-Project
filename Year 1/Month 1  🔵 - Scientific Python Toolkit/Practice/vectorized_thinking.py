import numpy as np

# Dimensions

normal_py_list = [[1, 2, 3]
                  ,[4, 5, 6]]
numpy_list = np.array([[1, 2, 3]
                       ,[4, 5, 6]])

# print(
#     normal_py_list
#     ,numpy_list
#     ,normal_py_list[0][0]
#     ,numpy_list[0, 0]
#     ,sep="\n"
# )

# Broadcasting

array = np.array([1, 2, 3])
broadcasted_array = np.array(array[np.newaxis, :] + array[:, np.newaxis])

# print(array
#       ,broadcasted_array
#       ,sep="\n")


# Boolean Masks

unmasked_array = np.arange(100).reshape(10, 10)
masked_array = unmasked_array[unmasked_array>=50].reshape(5, 10)
conditional_array = np.where(
    unmasked_array>=50
    ,True
    ,False
)

print(unmasked_array
      ,masked_array
      ,conditional_array
      ,unmasked_array[conditional_array]
      ,sep="\n")

# Arange

indices_py = range(len(array))
indices_np = np.arange(len(array))

nested_list_py = [i * 10 for i in range(len(array))]
not_nested_array_np = np.arange(len(array)) * 10

# print(indices_py
#       ,indices_np
#       ,nested_list_py
#       ,not_nested_array_np
#       ,sep="\n")

# ndenumerating

ndarray = np.arange(100).reshape(10, 10)
for (i, j), value in np.ndenumerate(ndarray):
    print(f"At row {i}, col{j}, the value is {value}")