import pytest
import sys
sys.path.insert(0, '..')
import tensor, gate
import numpy as np

def test_IA():
    A = np.random.rand(10, 10)
    true_result = np.kron(np.eye(A.shape[0]), A)
    test_result = tensor.IA(A, A.shape[0])
    assert np.allclose(true_result, test_result)
    
def testAI():
    A = np.random.rand(10, 10)
    true_result = np.kron(A, np.eye(A.shape[0]), )
    test_result = tensor.AI(A, A.shape[0])
    assert np.allclose(true_result, test_result)
    
def test_XA():
    A = np.random.rand(10, 10)
    true_result = np.kron(gate.gate1['X'], A)
    test_result = tensor.XA(A)
    assert np.allclose(true_result, test_result)

def testAX():
    A = np.random.rand(10, 10)
    true_result = np.kron(A, gate.gate1['X'])
    test_result = tensor.AX(A)
    assert np.allclose(true_result, test_result)
    
def test_ZA():
    A = np.random.rand(10, 10)
    true_result = np.kron(gate.gate1['Z'], A)
    test_result = tensor.ZA(A)
    assert np.allclose(true_result, test_result)
    
def testAZ():
    A = np.random.rand(10, 10)
    true_result = np.kron(A, gate.gate1['Z'])
    test_result = tensor.AZ(A)
    assert np.allclose(true_result, test_result)
    
def testAH():
    A = np.random.rand(10, 10)
    true_result = np.kron(A, gate.gate1['H'])
    test_result = tensor.AH(A)
    assert np.allclose(true_result, test_result)

def testHA():
    A = np.random.rand(10, 10)
    true_result = np.kron(gate.gate1['H'], A)
    test_result = tensor.HA(A)
    assert np.allclose(true_result, test_result)
    
def testRXA():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(gate.gate1['RX'](theta), A)
    test_result = tensor.RXA(A, theta)
    assert np.allclose(true_result, test_result)
    
def testARX():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(A, gate.gate1['RX'](theta))
    test_result = tensor.ARX(A, theta)
    assert np.allclose(true_result, test_result)
    
def testRYA():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(gate.gate1['RY'](theta), A)
    test_result = tensor.RYA(A, theta)
    assert np.allclose(true_result, test_result)

def testARY():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(A, gate.gate1['RY'](theta))
    test_result = tensor.ARY(A, theta)
    assert np.allclose(true_result, test_result)
    
def testRZA():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(gate.gate1['RZ'](theta), A)
    test_result = tensor.RZA(A, theta)
    assert np.allclose(true_result, test_result)
    
def testARZ():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(A, gate.gate1['RZ'](theta))
    test_result = tensor.ARZ(A, theta)
    assert np.allclose(true_result, test_result)
    
def testACRX():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(A.conj(), gate.gate2['CRX'](theta))
    test_result = tensor.ACRX(A, theta)
    assert np.allclose(true_result, test_result)
    
def testACRY():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(A.conj(), gate.gate2['CRY'](theta))
    test_result = tensor.ACRY(A, theta)
    assert np.allclose(true_result, test_result)
    
def testACRZ():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(A.conj(), gate.gate2['CRZ'](theta))
    test_result = tensor.ACRZ(A, theta)
    assert np.allclose(true_result, test_result)
    
def testCRXA():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(gate.gate2['CRX'](theta), A)
    test_result = tensor.CRXA(A, theta)
    assert np.allclose(true_result, test_result)
    
def testCRYA():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(gate.gate2['CRY'](theta), A)
    test_result = tensor.CRYA(A, theta)
    assert np.allclose(true_result, test_result)
    
def testCRZA():
    A = np.random.rand(10, 10)
    theta = np.random.uniform(0, 2*np.pi)
    true_result = np.kron(gate.gate2['CRZ'](theta), A)
    test_result = tensor.CRZA(A, theta)
    assert np.allclose(true_result, test_result)