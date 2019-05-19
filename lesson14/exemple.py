import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 51)
y1 = t**2*np.exp(-t**2)
y2 = t**4*np.exp(-t**2)

plt.plot(t, y1, label='t^2*exp(-t^2)')
plt.plot(t, y2, label='t^4*exp(-t^2)')

# декоративная часть
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plotting two curves in the same plot')
plt.legend()

plt.show()