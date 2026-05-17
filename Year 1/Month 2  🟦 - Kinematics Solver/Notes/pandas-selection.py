import pandas as pd
import numpy as np

# Set RNG
rng = np.random.default_rng(42)

columns = pd.Series(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
index = np.arange(0, 5)

df = pd.DataFrame(rng.integers(0, 10, (5, 10)), index=index, columns=columns)
df_copy = df.copy()
df_copy["E"] = ["one", "two", "three", "four", "five"]

# Getting Items []
print(df
      ,df["A"]
      ,df.A
      ,df[["B", "A"]]
      ,df[1:3]
      ,df.T["A":"C"]
      ,sep="\n------o------\n"
      ,end="\n\n------O-O------\n\n")


# Selection by Label
print(df
    ,df.loc[index[1]]
    ,df.loc[:, ["A", "B"]]
    ,df.loc[1:3, ["A", "B"]]
    ,df.loc[index[0], "A"]
    ,df.at[index[0], "A"] # Fast access to scalars.
    ,sep="\n------o------\n"
    ,end="\n\n------O-O------\n\n")

# Selection by Position
print(df
      ,df.iloc[3]
      ,df.iloc[1:3, :]
      ,df.iloc[[1, 2, 4], [1, 2]]
      ,sep="\n------o------\n"
      ,end="\n\n------O-O------\n\n")


# Boolean Indexing
print(df
      ,df[df["A"] > 3]
      ,df_copy[df_copy["E"].isin(["one", "four"])] # Filtering
      ,sep="\n------o------\n"
      ,end="\n\n------O-O------\n\n")

# Setting
s = pd.Series(np.arange(5), index=np.arange(5))

df["A"] = s
df.at[index[0], "B"] = 12
df.iat[0, 2] = 15
df.loc[:, "D"] = np.array([5] * len(df))
df[df > 5] = "W"
print(df
      ,sep="\n------o------\n"
      ,end="\n\n------O-O------\n\n")