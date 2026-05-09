import numpy as np

rng = np.random.default_rng(seed=42)

"""
rng.normal(loc, scale, size)
----------------------------

loc: the mean
scale: the standart deviation
size: the number of samples
"""

scores=rng.normal(loc=70, scale=10, size=10000)

top_scorers = np.sum(scores >= 90)

print(np.mean(scores)
      ,np.std(scores)
      ,top_scorers
      ,top_scorers/100
      ,sep="\n------o------\n"
      ,end="\n\n------O-O------\n\n")