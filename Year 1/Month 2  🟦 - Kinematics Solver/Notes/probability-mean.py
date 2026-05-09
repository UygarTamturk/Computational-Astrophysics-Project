import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=42)

small_sample = rng.integers(1, 7, 25)
large_sample = rng.integers(1, 7, 25)


print(np.mean(small_sample)
      ,np.mean(large_sample)
      ,sep="\n------o------\n"
      ,end="\n\n-------O-O------\n\n")


fig, ax = plt.subplots()

ax.plot(np.arange(small_sample.size), small_sample, label="small sample")
ax.plot(np.arange(large_sample.size), large_sample, label="large sample")

ax.set_xlabel("Roll Amount")
ax.set_ylabel("Rolls")

plt.legend()
plt.show()

