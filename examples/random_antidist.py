"""Generate random states and check if they are antidistinguishable."""
import numpy as np
from qiskit.quantum_info.states.random import random_statevector
from toqito.state_opt import state_exclusion


num_examples, num_states, dim = 10, 4, 4
for _ in range(num_examples):
    vectors = [random_statevector(dim).data for _ in range(num_states)]  
    print(f"Is antidistinguishable: {}") 
    