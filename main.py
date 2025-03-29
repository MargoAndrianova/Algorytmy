import numpy as np
import matplotlib.pyplot as plt

# Сітка для побудови
x_vals = np.linspace(-5, 5, 20)
y_vals = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x_vals, y_vals)

# Векторне поле для системи: dx/dt = y, dy/dt = y - 2x
U = Y
V = Y - 2*X

# Нормалізуємо вектори для гарного відображення напрямів
magnitude = np.sqrt(U**2 + V**2)
U_norm = U / magnitude
V_norm = V / magnitude

# Побудова фазового портрета
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, U_norm, V_norm, angles='xy')
plt.title("Фазовий портрет системи:\n$\dot{x} = y$, $\dot{y} = y - 2x$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect('equal')
plt.show()
