import numpy as np

def I(xs: np.ndarray):
    return xs

def CX(xs: np.ndarray):
    # only swap two last elements
    return np.array([xs[0], xs[1], xs[3], xs[2]])

def X(xs: np.ndarray):
    return np.array([xs[1], xs[0]])

def Y(xs: np.ndarray):
    return np.array([xs[1], -xs[0]*1j])

def Z(xs: np.ndarray):
    return np.array([xs[0], -xs[1]])

def H(xs: np.ndarray):
    return np.array([xs[0]+xs[1], xs[0]-xs[1]])/np.sqrt(2)




gate1 = {
    "I": np.array([[1, 0], [0, 1]], dtype=np.complex128),
    "X": np.array([[0, 1], [1, 0]], dtype=np.complex128),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=np.complex128),
    "Z": np.array([[1, 0], [0, -1]], dtype=np.complex128),
    "RX": lambda theta: np.array([[np.cos(theta/2), -1j*np.sin(theta/2)], [-1j*np.sin(theta/2), np.cos(theta/2)]], dtype=np.complex128),
    "RY": lambda theta: np.array([[np.cos(theta/2), -np.sin(theta/2)], [np.sin(theta/2), np.cos(theta/2)]], dtype=np.complex128),
    "RZ": lambda theta: np.array([[np.exp(-1j*theta/2), 0], [0, np.exp(1j*theta/2)]], dtype=np.complex128),
    "H": np.array([[1, 1], [1, -1]], dtype=np.complex128)/np.sqrt(2),
}

gate2 = {
    "II": np.array(
        [[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
        [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
        [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j],
        [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]]
    , dtype = np.complex128),
    "IX": np.array(
        [[0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
       [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
       [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j],
       [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j]]
    , dtype = np.complex128),
    "IY": np.array([[0.+0.j, 0.-1.j, 0.+0.j, 0.-0.j],
       [0.+1.j, 0.+0.j, 0.+0.j, 0.+0.j],
       [0.+0.j, 0.-0.j, 0.+0.j, 0.-1.j],
       [0.+0.j, 0.+0.j, 0.+1.j, 0.+0.j]], dtype = np.complex128),
    "IZ": np.array([[ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j, -1.+0.j,  0.+0.j, -0.+0.j],
       [ 0.+0.j,  0.+0.j,  1.+0.j,  0.+0.j],
       [ 0.+0.j, -0.+0.j,  0.+0.j, -1.+0.j]], dtype = np.complex128),
    "IH": np.array([[ 0.70710678+0.j,  0.70710678+0.j,  0.        +0.j,
         0.        +0.j],
       [ 0.70710678+0.j, -0.70710678+0.j,  0.        +0.j,
        -0.        +0.j],
       [ 0.        +0.j,  0.        +0.j,  0.70710678+0.j,
         0.70710678+0.j],
       [ 0.        +0.j, -0.        +0.j,  0.70710678+0.j,
        -0.70710678+0.j]], dtype = np.complex128),
    "XI": np.array([[0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j],
       [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j],
       [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
       [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j]], dtype = np.complex128),
    "XX": np.array([[0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j],
       [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j],
       [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
       [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]], dtype = np.complex128),
    "XY": np.array([[0.+0.j, 0.-0.j, 0.+0.j, 0.-1.j],
       [0.+0.j, 0.+0.j, 0.+1.j, 0.+0.j],
       [0.+0.j, 0.-1.j, 0.+0.j, 0.-0.j],
       [0.+1.j, 0.+0.j, 0.+0.j, 0.+0.j]], dtype = np.complex128),
    "XZ": np.array([[ 0.+0.j,  0.+0.j,  1.+0.j,  0.+0.j],
       [ 0.+0.j, -0.+0.j,  0.+0.j, -1.+0.j],
       [ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j, -1.+0.j,  0.+0.j, -0.+0.j]], dtype = np.complex128),
    "XH": np.array([[ 0.        +0.j,  0.        +0.j,  0.70710678+0.j,
         0.70710678+0.j],
       [ 0.        +0.j, -0.        +0.j,  0.70710678+0.j,
        -0.70710678+0.j],
       [ 0.70710678+0.j,  0.70710678+0.j,  0.        +0.j,
         0.        +0.j],
       [ 0.70710678+0.j, -0.70710678+0.j,  0.        +0.j,
        -0.        +0.j]], dtype = np.complex128),
    "YI": np.array([[0.+0.j, 0.+0.j, 0.-1.j, 0.-0.j],
       [0.+0.j, 0.+0.j, 0.-0.j, 0.-1.j],
       [0.+1.j, 0.+0.j, 0.+0.j, 0.+0.j],
       [0.+0.j, 0.+1.j, 0.+0.j, 0.+0.j]], dtype = np.complex128),
    "YX": np.array([[0.+0.j, 0.+0.j, 0.-0.j, 0.-1.j],
       [0.+0.j, 0.+0.j, 0.-1.j, 0.-0.j],
       [0.+0.j, 0.+1.j, 0.+0.j, 0.+0.j],
       [0.+1.j, 0.+0.j, 0.+0.j, 0.+0.j]], dtype = np.complex128),
    "YY": np.array([[ 0.+0.j,  0.-0.j,  0.-0.j, -1.+0.j],
       [ 0.+0.j,  0.+0.j,  1.-0.j,  0.-0.j],
       [ 0.+0.j,  1.-0.j,  0.+0.j,  0.-0.j],
       [-1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j]], dtype = np.complex128),
    "YZ": np.array([[ 0.+0.j,  0.+0.j,  0.-1.j,  0.-0.j],
       [ 0.+0.j, -0.+0.j,  0.-0.j,  0.+1.j],
       [ 0.+1.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j, -0.-1.j,  0.+0.j, -0.+0.j]], dtype = np.complex128),
    "YH": np.array([[ 0.+0.j        ,  0.+0.j        ,  0.-0.70710678j,
         0.-0.70710678j],
       [ 0.+0.j        , -0.+0.j        ,  0.-0.70710678j,
         0.+0.70710678j],
       [ 0.+0.70710678j,  0.+0.70710678j,  0.+0.j        ,
         0.+0.j        ],
       [ 0.+0.70710678j, -0.-0.70710678j,  0.+0.j        ,
        -0.+0.j        ]], dtype = np.complex128),
    "ZI": np.array([[ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j, -1.+0.j, -0.+0.j],
       [ 0.+0.j,  0.+0.j, -0.+0.j, -1.+0.j]], dtype = np.complex128),
    "ZX": np.array([[ 0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j],
       [ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j, -0.+0.j, -1.+0.j],
       [ 0.+0.j,  0.+0.j, -1.+0.j, -0.+0.j]], dtype = np.complex128),
    "ZY": np.array([[ 0.+0.j,  0.-1.j,  0.+0.j,  0.-0.j],
       [ 0.+1.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.-0.j, -0.+0.j,  0.+1.j],
       [ 0.+0.j,  0.+0.j, -0.-1.j, -0.+0.j]], dtype = np.complex128),
    "ZZ": np.array([[ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j, -1.+0.j,  0.+0.j, -0.+0.j],
       [ 0.+0.j,  0.+0.j, -1.+0.j, -0.+0.j],
       [ 0.+0.j, -0.+0.j, -0.+0.j,  1.-0.j]], dtype = np.complex128),
    "ZH": np.array([[ 0.+0.j        ,  0.+0.j        ,  0.-0.70710678j,
         0.-0.70710678j],
       [ 0.+0.j        , -0.+0.j        ,  0.-0.70710678j,
         0.+0.70710678j],
       [ 0.+0.70710678j,  0.+0.70710678j,  0.+0.j        ,
         0.+0.j        ],
       [ 0.+0.70710678j, -0.-0.70710678j,  0.+0.j        ,
        -0.+0.j        ]], dtype = np.complex128),
    
    
    "CX": np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=np.complex128),
    "SWAP": np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=np.complex128),
    "CZ": np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]], dtype=np.complex128),
    "CRX": lambda theta: np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, np.cos(theta/2), -1j*np.sin(theta/2)], [0, 0, -1j*np.sin(theta/2), np.cos(theta/2)]], dtype=np.complex128),
    "CRY": lambda theta: np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, np.cos(theta/2), -np.sin(theta/2)], [0, 0, np.sin(theta/2), np.cos(theta/2)]], dtype=np.complex128),
    "CRZ": lambda theta: np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, np.exp(-1j*theta/2), 0], [0, 0, 0, np.exp(1j*theta/2)]], dtype=np.complex128),
}