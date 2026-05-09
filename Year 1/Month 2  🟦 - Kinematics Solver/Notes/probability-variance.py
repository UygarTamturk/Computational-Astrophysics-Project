import numpy as np

rng = np.random.default_rng(seed=42)

"""
Variance measures how for the data points are spread out from that center.

A low variance means the data points are clustered closely around the mean
A high variance means the data is widely scattered
"""

# Distributing Data A
tight_data = rng.normal(loc=10, scale=0.5, size=1000)
spread_data = rng.normal(10, 0.5, 1000)

print(np.mean(tight_data)
      ,np.var(tight_data)
      ,np.mean(spread_data)
      ,np.var(spread_data)
      ,sep="\n-----o-----\n"
      ,end="\n\n------O-O------\n\n"
)