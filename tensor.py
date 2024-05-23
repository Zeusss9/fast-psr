import numpy as np
import gate


def kron_I_A(A, N):
    m, n = A.shape
    out = np.zeros((N, m, N, n), dtype=A.dtype)
    r = np.arange(N)
    out[r, :, r, :] = A
    out.shape = (m*N, n*N)
    return out


def kron_A_I(A, N):
    m, n = A.shape
    out = np.zeros((N, m, N, n), dtype=A.dtype)
    r = np.arange(N)
    out[:, r, :, r] = A
    out.shape = (m*N, n*N)
    return out


def kron_X_A(A):
    X = gate.gate1['X']
    m, n = A.shape
    out = np.zeros((2, m, 2, n), dtype=A.dtype)
    out[0, :, 1, :] = A
    out[1, :, 0, :] = A
    out.shape = (2 * m, 2 * n)
    return out


def kron_A_X(A):
    X = np.array([[0, 1], [1, 0]])
    m, n = A.shape
    out = np.zeros((m, 2, n, 2), dtype=A.dtype)
    out[:, 0, :, 1] = A
    out[:, 1, :, 0] = A
    out.shape = (2 * m, 2 * n)
    return out

def kron_Z_A(A):
    Z = np.array([[1, 0], [0, -1]])
    m, n = A.shape
    out = np.zeros((2, m, 2, n), dtype=A.dtype)
    out[0, :, 0, :] = A
    out[1, :, 1, :] = -A
    out.shape = (2 * m, 2 * n)
    return out

def kron_A_Z(A):
    Z = np.array([[1, 0], [0, -1]])
    m, n = A.shape
    out = np.zeros((m, 2, n, 2), dtype=A.dtype)
    out[:, 0, :, 0] = A
    out[:, 1, :, 1] = -A
    out.shape = (2 * m, 2 * n)
    return out


def kron_RX_A(A, theta):
    cos_theta_2_times_A = np.cos(theta / 2) * A
    sin_theta_2_times_A = -1j * np.sin(theta / 2) * A
    #i = 1j
    # RX = np.array([
    #     [cos_theta_2, -i * sin_theta_2],
    #     [-i * sin_theta_2, cos_theta_2]
    # ], dtype=complex)
    
    m, n = A.shape
    out = np.zeros((2, m, 2, n), dtype=complex)
    
    out[0, :, 0, :] = cos_theta_2_times_A
    out[0, :, 1, :] = sin_theta_2_times_A
    out[1, :, 0, :] = sin_theta_2_times_A
    out[1, :, 1, :] = cos_theta_2_times_A
    
    out.shape = (2 * m, 2 * n)
    return out

def kron_A_RX(A, theta):
    cos_theta_2_times_A = np.cos(theta / 2) * A
    sin_theta_2_times_A = -1j * np.sin(theta / 2) * A
    # i = 1j
    
    # RX = np.array([
    #     [cos_theta_2, -i * sin_theta_2],
    #     [-i * sin_theta_2, cos_theta_2]
    # ], dtype=complex)
    
    m, n = A.shape
    out = np.zeros((m, 2, n, 2), dtype=complex)
    out[:, 0, :, 0] = cos_theta_2_times_A
    out[:, 0, :, 1] = sin_theta_2_times_A
    out[:, 1, :, 0] = sin_theta_2_times_A
    out[:, 1, :, 1] = cos_theta_2_times_A
    out.shape = (2 * m, 2 * n)
    return out

