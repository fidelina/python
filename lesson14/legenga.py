import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 20)
y = t ** 2

plt.plot(t, y, 'g--', label='x**2')

plt.axis([-5, 5, -30, 30])  # задание [xmin, xmax, ymin, ymax]
plt.xlabel('t')  # обозначение оси абсцисс
plt.ylabel('y')  # обозначение оси ординат
plt.title('My first normal plot')  # название графика
plt.legend()  # вставка легенды (текста в label)

plt.show()