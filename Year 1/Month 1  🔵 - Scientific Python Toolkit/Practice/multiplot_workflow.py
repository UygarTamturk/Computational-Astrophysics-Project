import matplotlib.pyplot as plt
import numpy as np

t = np.arange(10)
acceleration = 5

fig, ax = plt.subplots(2, 2)
fig.suptitle("Displacement, Velocity and Acceleration")
fig.tight_layout()

ax[0, 0].plot(t, np.ones([t.size]) * acceleration)
ax[0, 0].set_ylabel("acceleration")


ax[1, 0].plot(t, t * acceleration)
ax[1, 0].set_ylabel("velocity")

ax[0, 1].plot(t, (t**2) * acceleration)
ax[0, 1].set_ylabel("displacement")


for axes in ax.flatten():
    axes.set_xlabel("time")
plt.show()