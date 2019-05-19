import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

t = np.linspace(-5, 5, 20)  # 20 точек между -5 и 5
y = f(t)

plt.plot(t, y)
plt.show()