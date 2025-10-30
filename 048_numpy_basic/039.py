"""

Write a NumPy/Matplotlib program to visualize sin/cos of angles in the range [-2π, 2π].

"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    # x-ticks
    x_ticks = np.array([-2 * np.pi, -3/2 * np.pi, -np.pi, -np.pi/2])
    x_ticks = np.r_[x_ticks, 0, -x_ticks[::-1]]

    angles = np.linspace(x_ticks.min(), x_ticks.max(), 1000)

    fig, ax = plt.subplots(figsize=(12, 5))

    # sin/cos curves
    ax.plot(angles, np.sin(angles), label=r"$sin(\theta)$")
    ax.plot(angles, np.cos(angles), label=r"$cos(\theta)$")

    # titles
    ax.set_title(r"$sin(\theta),\ cos(\theta); \hspace{2} \theta \in [-2\pi, 2\pi]$")
    ax.set_xlabel(r"$\theta\ [rad]$")

    # set x-ticks
    x_ticks_lbl = [
        r"$-2\pi$", r"$-\frac{3\pi}{2}$", r"$-\pi$", r"$-\frac{\pi}{2}$", 0,
        r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"
    ]
    ax.set_xticks(x_ticks, x_ticks_lbl)
    ax.fmt_xdata = lambda val: f"{val:.3f}"     # restore the lost x-axis formatter (due to setting x-ticks)

    # enable a legend and a gird
    ax.legend()
    ax.grid(True, alpha=0.5)

    plt.show()


if __name__ == "__main__":
    main()
