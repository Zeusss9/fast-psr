import numpy as np

def P(i, n = 2):
    result = np.zeros((n,n))
    result[i // n, i % n] = 1
    return result

def state0(num_qubits):
    state = np.zeros(2**num_qubits)
    state[0] = 1
    return state

r = 1/2
epsilon = np.pi/2