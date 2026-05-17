import pandas as pd
import numpy as np

rng = np.random.default_rng(42)

# Viewing Data

dates = pd.date_range("20260517", periods=12)
df = pd.DataFrame(rng.integers(0, 7, (12, 4)), index=dates, columns=list("ABCD"))

print(df
    ,df.head(1)
    ,df.tail(3)
    ,df.index
    ,df.columns
    ,df.to_numpy()
    ,df.describe()
    ,df.T
    ,df.sort_index(axis=1, ascending=False)
    ,df.sort_values(by="A")
    ,sep="\n------o------\n"
    ,end="\n\n------O-O------\n\n")