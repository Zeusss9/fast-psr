import constant, tensor, gate, utilities
import numpy as np, qiskit

def circuit_to_gates(qc: qiskit.QuantumCircuit):
    gates = []
    for instr, qargs, _ in qc.data:
        qubit_indices = [q.index for q in qargs]
        name = instr.name.upper()
        gates.append(gate.Gate(name[1:] if name[0] == 'C' else name, indices = qubit_indices, param = np.squeeze(instr.params)))
    return gates
    
def gates_to_string(gates: list[qiskit.QuantumCircuit], num_qubits: int) -> np.ndarray:
    """Return the matrix representation of a circuit composed of a list of gates acting on `num_qubits` qubits.

    Args:
        gates (list[Gate]): List of gates in the circuit
        num_qubits (int): # of qubits in the system

    Returns:
        np.ndarray: Matrix representation of the circuit
    """
    # Example: {CNOT_1,3, RY_2(\pi)} act on 5 qubits circuit
    # Init tensor form as : I \otimes I \otimes ... \otimes I (num_qubits otimes)
    # and params form as [0, 0, ..., 0] (num_qubits times)
    tensor_form = [['I'] * num_qubits]
    params_form = [0] * num_qubits
    # Update tensor form and params form based on gates
    # => tensor_form = [['I', 'M', 'RY', 'I', 'I'], ['I', 'P', 'RY', 'X', 'I']]
    # => params_form = [0, 0, np.pi, 0, 0]
    for gate in gates:
        if gate.param is not None:
            if len(gate.indices) == 1:
                params_form[gate.indices[0]] = gate.param
            else:
                params_form[gate.indices[1]] = gate.param
        if len(gate.indices) == 1:
            tensor_form[0][gate.indices[0]] = gate.name
        else:
            
            tensor_form = utilities.duplicate_xss(tensor_form)
            tensor_form[0][gate.indices[0]] = 'M' # P0
            tensor_form[1][gate.indices[0]] = 'P' # P3
            tensor_form[1][gate.indices[1]] = gate.name
    
    return params_form, tensor_form

def string_to_matrix(params_form: np.ndarray, tensor_form: np.ndarray) -> np.ndarray:
    """Convert the tensor form and params form to the matrix representation of the circuit.

    Args:
        params_form (np.ndarray): lisr of parameters
        tensor_form (np.ndarray): list of gates (only gate names, no parameters)

    Returns:
        np.ndarray: matrix representation of the circuit
    """
    # Convert tensor form and params form to matrix
    # => [['I', 'M', 'RY', 'I', 'I'], ['I', 'P', 'RY', 'X', 'I']]
    # -> I \otimes M \otimes RY(np.pi) \otimes I \otimes I
    #  + I \otimes P \otimes RY(np.pi) \otimes X \otimes I
    matrices = [np.array([1])]*len(tensor_form)
    print(len(tensor_form[0]))
    print(len(tensor_form))
    for i in range(0, len(tensor_form[0])):
        for j in range(len(tensor_form)):
            print(matrices[j].shape)
            if len(tensor_form[j][i]) >= 2:
                matrices[j] = getattr(tensor, f'A{tensor_form[j][i]}')(matrices[j], params_form[i])
            else:
                matrices[j] = getattr(tensor, f'A{tensor_form[j][i]}')(matrices[j])
    return sum(matrices)

import qiskit.quantum_info as qi
import constant
from qoop.core.random_circuit import generate_with_pool
import splitter
num_qubits = 15
qc = generate_with_pool(num_qubits, 10)
qc = qc.assign_parameters([1]*qc.num_parameters)
true_state = qi.Statevector.from_instruction(qc).data
qcs = splitter.split_control(qc.copy())
matrices = []
for sub_qc in qcs:
    gates = circuit_to_gates(sub_qc)
    params_form, tensor_form = gates_to_string(gates, num_qubits)
    print(tensor_form)
    matrices.append(string_to_matrix(params_form, tensor_form))
# result = matrices[0]
# for i in range(1, len(matrices)):
#     # print(matrices[i].shape)
#     result = result @ matrices[i]
# # return result
# # matrix = qimax(qc)
# test_state = result @ constant.state0(num_qubits)
