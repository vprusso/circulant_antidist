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
v, m = state_exclusion(vectors)
print(v)

#print(vectors.is_antidistinguishable)