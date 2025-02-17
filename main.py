import numpy as np
import matplotlib.pyplot as plt

num = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000]
faces = [1, 2, 3, 4, 5, 6]
results = {}

for n in num:
    rolls = np.random.randint(1, 7, size=n)  # Симуляція кидків
    probabilities = [np.sum(rolls == face) / n for face in faces]  # Ймовірності випадіння
    results[n] = probabilities

for n, probs in results.items():
    plt.figure()
    plt.bar(faces, probs, tick_label=faces)
    plt.title(f"Емпіричні ймовірності після {n} кидків")
    plt.xlabel("Грань кубика")
    plt.ylabel("Ймовірність")
    plt.ylim(0, 0.4)
    plt.show()