import numpy as np
rng = np.random.default_rng(seed=42)

"""
Standart deviation is usually preferred over Variance because it is expressed
in the same units as the original data.
"""

# Machine A: Very precise
machine_a = rng.normal(loc=10, scale=0.02, size=100) 

# Machine B: A bit "loose"
machine_b = rng.normal(loc=10, scale=0.2, size=100)

print(np.std(machine_a)
      ,np.std(machine_b)
      ,sep="\n------o------\n"
      ,end="\n\n------O-O------\n\n")