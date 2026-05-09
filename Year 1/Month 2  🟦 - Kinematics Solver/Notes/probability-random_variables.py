import numpy as np

# Setting a seed results in reproducibility of a data countless times
rng = np.random.default_rng()


die_rolls = rng.integers(low=1, high=7, size=10)
print(die_rolls
      ,end="\n\n-----O-O-----\n\n")

uniform_samples = rng.random(size=5)

print(uniform_samples
      ,end="\n\n-----O-O-----\n\n")

