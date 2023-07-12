import numpy as np
from toqito.matrix_ops import vectors_from_gram_matrix
from toqito.state_opt import state_exclusion


# This matrix is antidistinguishable:
c = 1/np.sqrt(3)
gram = np.array([
    [1, c, c, c],
    [c, 1, c*1j, (1 + c*1j)/2],
    [c, -c*1j, 1, (1-c*1j)/2],
    [c, (1-c*1j)/2, (1+c*1j)/2, 1]
])

vectors = vectors_from_gram_matrix(gram)
gram_opt_value, _ = state_exclusion(vectors)
print(f"{gram_opt_value}")

# For small eps > 0, it is not antidistinguishable:
eps = 0.1
v = np.array([1, (-np.sqrt(3) + 1j)/2, (-np.sqrt(3) - 1j)/2, 0]).reshape(-1, 1)
w = np.array([0, 0, 0, 1]).reshape(-1, 1)

gram_eps = 1/(1 - 2 * eps) * (gram + eps * (v @ v.conj().T + w @ w.conj().T - 3 * np.identity(4)))
vectors = vectors_from_gram_matrix(gram_eps)
gram_eps_opt_value, _ = state_exclusion(vectors)
print(f"{gram_eps_opt_value}")