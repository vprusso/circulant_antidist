import numpy as np
from toqito.matrices import standard_basis
from toqito.state_opt import state_exclusion

# Define the standard basis 2-qubit basis (|0>, |1>).
e0, e1 = standard_basis(2)

# Define the so-called "trine" states.
phi0 = e0
phi1 = -1/2 * e0 + np.sqrt(3)/2 * e1
phi2 = -1/2 * e0 - np.sqrt(3)/2 * e1

# The trine states are antidistinguishable.
vectors = [phi0, phi1, phi2]
opt_value, measurements = state_exclusion(vectors, primal_dual="primal")

# SDP value being zero indicates that the states are antidistinguishable.
print(f"Optimal SDP value: {opt_value}")

print("Measurements:")
print(f"M_0 = \n {np.around(measurements[0], decimals=5)}")
print(f"M_1 = \n {np.around(measurements[1], decimals=5)}")
print(f"M_2 = \n {np.around(measurements[2], decimals=5)}")