import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=42)

numpy_Data = rng.integers(1, 10, 5)
phyton_data = [1, 2, 3, 4, 5]

# One Dimension
datas = [
    ("NumPy Data", numpy_Data)
    ,("Phyton Data", phyton_data)
    ,("Dict Data", {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
]

series_datas = {}

def read_data(data_name, data) -> None:
    s = pd.Series(data)
    series_datas[data_name] = s

    print(f"{data_name}:\n{s}"
          ,end="\n\n------O-O------\n\n")
    
def search_label(data= pd.Series, label= str):

    # .loc function searches for the given label by the user, outputing the value as result.
    return print(data.loc[label])

def search_index(data= pd.Series, index= int):
    # .iloc function returns values corresponding with the inserted index, outputing the value as result.

    return print(data.iloc[index])

for data in datas:
    read_data(*data)

print(series_datas)
search_index(series_datas["NumPy Data"], 1)
search_label(series_datas["Dict Data"], "a")
