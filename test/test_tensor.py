import pytest
import sys
sys.path.insert(0, '..')
import tensor
import numpy as np
# test case 1
def test_kron_I_A():
    A = np.random.rand(10, 10)
    true_result = np.kron(np.eye(A.shape[0]), A)
    test_result = tensor.kron_I_A(A, A.shape[0])
    assert np.allclose(true_result, test_result)
    
