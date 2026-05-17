import pandas as pd
import numpy as np

# Set RNG
rng = np.random.default_rng(seed=42)

# Year - Month - Day
dates = pd.date_range("20260517", periods=6)
df = pd.DataFrame(np.random.random_integers(0, 7, (6, 4)), index=dates, columns=list("ABCD"))

print(dates
     ,df
     ,sep="\n------o------\n"
     ,end="\n\n------O-O------\n\n")

# Dataframe
df = pd.DataFrame({
    "A": 1.0
    ,"B": pd.Timestamp("20260517")
    ,"C": pd.Series(1, index=list(range(4)), dtype="float32")
    ,"D": np.array([3] * 4, dtype="int32")
    ,"E": pd.Categorical(["Test", "Train", "Test", "Train"])
    ,"F": "foo",
})

print(df
      ,df.dtypes
      ,sep="\n------o------\n"
      ,end="\n\n------O-O------\n\n")

