import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
from typing import List, Union

plt.style.use("cyberpunk")


class PoissonProcess:
    def __init__(self, intensity, T):
        self.intensity = intensity
        self.T = T

    def generate_trajectory(self):
        t = 0
        trajectory = [0]
        while t < self.T:
            t += np.random.exponential(1 / self.intensity)
            if t < self.T:
                trajectory.append(t)
        return trajectory


def plot_trajectories(processes: List[List[List[Union[int, float]]]], labels: List[str], filename=None):
    fig, axs = plt.subplots(len(processes), 1, figsize=(10, 6 * len(processes)))
    for i, process in enumerate(processes):
        for trajectory in process:
            axs[i].step([0] + trajectory, range(len(trajectory) + 1), where='post')
        axs[i].set_title(labels[i])
        axs[i].grid(True)  # Додати сітку до графіка
        axs[i].set_xlabel("Time")  # Задати підпис для осі X
        axs[i].set_ylabel("Number of Events")  # Задати підпис для осі Y
    plt.tight_layout()

    # Зберегти графік у форматі PNG, якщо вказано ім'я файлу
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
    # dpi - це абревіатура від "dots per inch" (точок на дюйм).
    # Це параметр, який використовується для визначення роздільної здатності
    # (кількості точок на дюйм) при збереженні зображення у форматі PNG або іншому растровому форматі.
    plt.show()


if __name__ == "__main__":
    # Визначте інтенсивності (ламбди) та час симуляції T
    lambdas = [0.1, 0.25]
    # Часовий інтервал
    T = 100
    trajectories = []
    labels = []
    for lam in lambdas:
        process = PoissonProcess(lam, T)
        trajectories.append([process.generate_trajectory() for _ in range(2)])
        labels.append(f"Poisson process with λ={lam}")
    # Візуалізуйте траєкторії і збережіть у файл "myplot.png"
    plot_trajectories(trajectories, labels, filename="img/myplot.png")
