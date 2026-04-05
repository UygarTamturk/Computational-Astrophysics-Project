import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi, 300)
y = np.tan(x)

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_xlabel("Angle (radians)")
ax.set_ylabel("Amplitude")
ax.set_title("Tan wave")

plt.show()