import numpy as np
import gate
def kron_I_A(A, N):
    m,n = A.shape
    out = np.zeros((N,m,N,n),dtype=A.dtype)
    r = np.arange(N)
    out[r,:,r,:] = A
    out.shape = (m*N,n*N)
    return out

def kron_A_I(A, N):
    m,n = A.shape
    out = np.zeros((N,m,N,n),dtype=A.dtype)
    r = np.arange(N)
    out[:,r,:,r] = A
    out.shape = (m*N,n*N)
    return out

def kron_X_A(A):
    X = gate.gate1['X']
    m, n = A.shape
    out = np.zeros((2, m, 2, n), dtype=A.dtype)
    out[0, :, 1, :] = A
    out[1, :, 0, :] = A   
    out.shape = (2 * m, 2 * n)
    return out
# def kron_A_I(A, N):
#     out = np.zeros((N*N, N*N),dtype=A.dtype)
#     for i in range(N):
#         for j in range(N):
#             value = A[i,j]
#             out[i*2: i*2 + 2,j*2:j*2 + 2] = np.array([[value, 0], [0, value]])
#     return out

