import numpy as np
import gate

def HA(A):
    # sqrt2_times_A = 1/np.sqrt(2) * A
    # m, n = A.shape
    # out = np.zeros((2, m, 2, n), dtype=A.dtype)
    
    # out[0, :, 0:1, :] = sqrt2_times_A
    # out[0, :, 1, :] = sqrt2_times_A
    # out[1, :, 0, :] = sqrt2_times_A
    # out[1, :, 1, :] = -sqrt2_times_A
    # out.shape = (2 * m, 2 * n)
    # return out
    return np.kron(gate.gate1['H'], A) # This way is still faster

def AH(A):
    sqrt2_times_A = 1/np.sqrt(2) * A
    m, n = A.shape
    out = np.zeros((m, 2, n, 2), dtype=A.dtype)
    
    out[:, 0, :, 0] = sqrt2_times_A
    out[:, 0, :, 1] = sqrt2_times_A
    out[:, 1, :, 0] = sqrt2_times_A
    out[:, 1, :, 1] = -sqrt2_times_A
    
    out.shape = (2 * m, 2 * n)
    return out

def IA(A, N):
    m, n = A.shape
    out = np.zeros((N, m, N, n), dtype=A.dtype)
    r = np.arange(N)
    out[r, :, r, :] = A
    out.shape = (m*N, n*N)
    return out


def AI(A, N):
    m, n = A.shape
    out = np.zeros((N, m, N, n), dtype=A.dtype)
    r = np.arange(N)
    out[:, r, :, r] = A
    out.shape = (m*N, n*N)
    return out


def XA(A):
    X = gate.gate1['X']
    m, n = A.shape
    out = np.zeros((2, m, 2, n), dtype=A.dtype)
    out[0, :, 1, :] = A
    out[1, :, 0, :] = A
    out.shape = (2 * m, 2 * n)
    return out


def AX(A):
    X = np.array([[0, 1], [1, 0]])
    m, n = A.shape
    out = np.zeros((m, 2, n, 2), dtype=A.dtype)
    out[:, 0, :, 1] = A
    out[:, 1, :, 0] = A
    out.shape = (2 * m, 2 * n)
    return out

def ZA(A):
    Z = np.array([[1, 0], [0, -1]])
    m, n = A.shape
    out = np.zeros((2, m, 2, n), dtype=A.dtype)
    out[0, :, 0, :] = A
    out[1, :, 1, :] = -A
    out.shape = (2 * m, 2 * n)
    return out

def AZ(A):
    Z = np.array([[1, 0], [0, -1]])
    m, n = A.shape
    out = np.zeros((m, 2, n, 2), dtype=A.dtype)
    out[:, 0, :, 0] = A
    out[:, 1, :, 1] = -A
    out.shape = (2 * m, 2 * n)
    return out


def RXA(A, theta):
    cos_theta_2_times_A = np.cos(theta / 2) * A
    sin_theta_2_times_A = -1j * np.sin(theta / 2) * A
    m, n = A.shape
    out = np.zeros((2, m, 2, n), dtype=complex)
    
    out[0, :, 0, :] = cos_theta_2_times_A
    out[0, :, 1, :] = sin_theta_2_times_A
    out[1, :, 0, :] = sin_theta_2_times_A
    out[1, :, 1, :] = cos_theta_2_times_A
    
    out.shape = (2 * m, 2 * n)
    return out

def ARX(A, theta):
    cos_theta_2_times_A = np.cos(theta / 2) * A
    sin_theta_2_times_A = -1j * np.sin(theta / 2) * A
    m, n = A.shape
    out = np.zeros((m, 2, n, 2), dtype=complex)
    out[:, 0, :, 0] = cos_theta_2_times_A
    out[:, 0, :, 1] = sin_theta_2_times_A
    out[:, 1, :, 0] = sin_theta_2_times_A
    out[:, 1, :, 1] = cos_theta_2_times_A
    out.shape = (2 * m, 2 * n)
    return out

def RYA(A, theta):
    cos_theta_2_times_A = np.cos(theta / 2) * A
    sin_theta_2_times_A = np.sin(theta / 2) * A
    m, n = A.shape
    out = np.zeros((2, m, 2, n), dtype=complex)
    
    out[0, :, 0, :] = cos_theta_2_times_A
    out[0, :, 1, :] = -sin_theta_2_times_A
    out[1, :, 0, :] = sin_theta_2_times_A
    out[1, :, 1, :] = cos_theta_2_times_A
    
    out.shape = (2 * m, 2 * n)
    return out

def ARY(A, theta):
    cos_theta_2_times_A = np.cos(theta / 2) * A
    sin_theta_2_times_A = np.sin(theta / 2) * A
    m, n = A.shape
    out = np.zeros((m, 2, n, 2), dtype=complex)
    out[:, 0, :, 0] = cos_theta_2_times_A
    out[:, 0, :, 1] = -sin_theta_2_times_A
    out[:, 1, :, 0] = sin_theta_2_times_A
    out[:, 1, :, 1] = cos_theta_2_times_A
    out.shape = (2 * m, 2 * n)
    return out

def ARZ(A, theta):
    phase = 1j * theta / 2
    m, n = A.shape
    out = np.zeros((m, 2, n, 2), dtype=complex)
    out[:, 0, :, 0] = np.exp(-phase) * A
    out[:, 0, :, 1] = 0
    out[:, 1, :, 0] = 0
    out[:, 1, :, 1] = np.exp(phase) * A
    out.shape = (2 * m, 2 * n)
    return out

def RZA(A, theta):
    phase = 1j * theta / 2
    m, n = A.shape
    out = np.zeros((2, m, 2, n), dtype=complex)
    out[0, :, 0, :] = np.exp(-phase) * A
    out[0, :, 1, :] = 0
    out[1, :, 0, :] = 0
    out[1, :, 1, :] = np.exp(phase) * A
    out.shape = (2 * m, 2 * n)
    return out

def CXA(A):
    gate.gate2['CX']
    
    m, n = A.shape
    out = np.zeros((4, m, 4, n), dtype=A.dtype)
    
    out[0, :, 0, :] = A
    out[1, :, 1, :] = A
    out[2, :, 3, :] = A
    out[3, :, 2, :] = A 
    out.shape = (4 * m, 4 * n)
    return out

def ACX(A):
    gate.gate2['CX']
    
    m, n = A.shape
    out = np.zeros((m, 4, n, 4), dtype=A.dtype)

    out[:, 0, :, 0] = A
    out[:, 1, :, 1] = A
    out[:, 2, :, 3] = A
    out[:, 3, :, 2] = A
    
    out.shape = (4 * m, 4 * n)
    return out

def ACRX(A, theta):
    cos_theta_2_times_A = np.cos(theta / 2) * A
    sin_theta_2_times_A = -1j * np.sin(theta / 2) * A
    m, n = A.shape
    out = np.zeros((m, 4, n, 4), dtype=complex)
    out[:, 0, :, 0] = A
    out[:, 1, :, 1] = A
    out[:, 2, :, 2] = cos_theta_2_times_A
    out[:, 2, :, 3] = sin_theta_2_times_A
    out[:, 3, :, 2] = sin_theta_2_times_A
    out[:, 3, :, 3] = cos_theta_2_times_A
    out.shape = (4 * m, 4 * n)
    return out

def CRXA(A, theta):
    cos_theta_2_times_A = np.cos(theta / 2) * A
    sin_theta_2_times_A = -1j * np.sin(theta / 2) * A
    m, n = A.shape
    out = np.zeros((4, m, 4, n), dtype=complex)
    out[0, :, 0, :] = A
    out[1, :, 1, :] = A
    out[2, :, 2, :] = cos_theta_2_times_A
    out[2, :, 3, :] = sin_theta_2_times_A
    out[3, :, 2, :] = sin_theta_2_times_A
    out[3, :, 3, :] = cos_theta_2_times_A
    out.shape = (4 * m, 4 * n)
    return out

def ACRY(A, theta):
    cos_theta_2_times_A = np.cos(theta / 2) * A
    sin_theta_2_times_A = np.sin(theta / 2) * A

    m, n = A.shape
    out = np.zeros((m, 4, n, 4), dtype=complex)
    
    out[:, 0, :, 0] = A
    out[:, 1, :, 1] = A
    out[:, 2, :, 2] = cos_theta_2_times_A
    out[:, 2, :, 3] = -sin_theta_2_times_A
    out[:, 3, :, 2] = sin_theta_2_times_A
    out[:, 3, :, 3] = cos_theta_2_times_A
    
    out.shape = (4 * m, 4 * n)
    return out

def CRYA(A, theta):
    cos_theta_2_times_A = np.cos(theta / 2) * A
    sin_theta_2_times_A = np.sin(theta / 2) * A

    m, n = A.shape
    out = np.zeros((4, m, 4, n), dtype=complex)
    
    out[0, :, 0, :] = A
    out[1, :, 1, :] = A
    out[2, :, 2, :] = cos_theta_2_times_A
    out[2, :, 3, :] = -sin_theta_2_times_A
    out[3, :, 2, :] = sin_theta_2_times_A
    out[3, :, 3, :] = cos_theta_2_times_A
    
    out.shape = (4 * m, 4 * n)
    return out


def CRZA(A, theta):
    phase = 1j * theta / 2
    m, n = A.shape
    out = np.zeros((4, m, 4, n), dtype=complex)
    out[0, :, 0, :] = A
    out[1, :, 1, :] = A
    out[2, :, 2, :] = np.exp(-phase) * A
    out[3, :, 3, :] = np.exp(phase) * A
    out.shape = (4 * m, 4 * n)
    return out

def ACRZ(A, theta):
    phase = 1j * theta / 2
    m, n = A.shape
    out = np.zeros((m, 4, n, 4), dtype=complex)
    out[:, 0, :, 0] = A
    out[:, 1, :, 1] = A
    out[:, 2, :, 2] = np.exp(-phase) * A
    out[:, 3, :, 3] = np.exp(phase) * A
    out.shape = (4 * m, 4 * n)
    return out
