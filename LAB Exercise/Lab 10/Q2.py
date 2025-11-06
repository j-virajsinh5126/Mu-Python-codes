import matplotlib.pyplot as plt
import numpy as np
# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# Plot
plt.plot(x, y1, label='Sine', color='blue')
plt.plot(x, y2, label='Cosine', color='orange')
# Add legend and show plot
plt.legend()
plt.title('Sine and Cosine Functions')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()
