import matplotlib.pyplot as plt
import numpy as np

# creating data
x = np.linspace (0, 2*np.pi, 300)
y = np.sin(x)
z = np.cos(x)

"""
Figure: entire canvas, it can contain one or many plots
Axes: a single plot, has its own x and y axis, title, data and legend. 

Everytime you plot something, you're adding data to an Axes.
Every time you resize the canvas or save the file, you're working with the figure
"""

# creating figure and axes
fig, ax = plt.subplots()

# plotting
ax.plot(x, z)
plt.show()