import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 180)

fig, ax = plt.subplots()

ax.plot(x, np.sin(x), label="sin(x)")
ax.plot(x, np.cos(x), label="cos(x)")
ax.plot(x, np.sin(x) * np.exp(x/4), label="damped sin(x)")

ax.set_xlabel("Angle (Radians)")
ax.set_ylabel("Amplitude")
ax.set_title("Trigonometric Functions")
ax.legend()

plt.show()