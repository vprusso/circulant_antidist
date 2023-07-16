"""Incoherent decomposition of Gram matrix."""
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from toqito.matrix_ops import vectors_from_gram_matrix
from toqito.state_opt import state_exclusion


def plot_dims(step: int = 10, start_dim: int = 3, end_dim: int = 8) -> None:
    eps = 0.0001
    plot_vals = defaultdict(dict)
    for n in range(start_dim, end_dim):
        gammas, opt_vals = [], []
        e = np.ones(n)
        for gamma in np.linspace(0, 1-eps, step):
            gram = (1 - (gamma*(n-1))/(n-2)) * np.identity(n) + gamma * (e * e.T + 1/(n-2) * np.identity(n))
            vectors = vectors_from_gram_matrix(gram)

            gammas.append(gamma)
            opt_val, _ = state_exclusion(vectors, primal_dual="dual")
            opt_vals.append(opt_val)
        plot_vals[n]["gammas"] = gammas
        plot_vals[n]["opt_vals"] = opt_vals

    for k, v in plot_vals.items():
        plt.plot(v["gammas"], v["opt_vals"], "-", linewidth=2, label=f"n={k}")

    plt.legend(loc="upper left")
    plt.xlabel(r"$\gamma$")
    plt.ylabel("Optimal SDP value")
    plt.title(r"Optimal SDP value vs. $\gamma$")
    plt.grid()
    plt.show()


plot_dims()