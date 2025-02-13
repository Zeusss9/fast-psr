
import numpy as np
qasm_gates = [('RZ', 0.3, [0]),
 ('CX', -999, [0, 1]),
 ('H', -999, [2]),
 ('H', -999, [0]),
 ('RX', 0.5, [1]),
 ('H', -999, [2]),
 ('CX', -999, [0, 1]),
 ('RZ', 0.5, [0]),
 ('H', -999, [2])]

def operatoring(instructors):
    """Construct operators from the list of operators and list of xoperators
    """
    is_cx_first = False
    operators = []
    operator = []
    operator_temp = []
    xoperator = []
    xoperator_temp = []
    xoperators = []
    
    if instructors[0][0] == "CX":
        is_cx_first = True
    num_qubits = max(max(instructors, key=lambda x: max(x[2]))[2]) + 1
    barriers = [0] * num_qubits
    if instructors[0][0] == "CX":
        index_u_cx = 0
        index_u_noncx = 1
    else:
        index_u_cx = 1
        index_u_noncx = 0
    index_u_next_cx = 0
    index_u_next_noncx = 0
    break_noncx = False
    noncx_active = True
    j = 0
    gatess = [[0 for _ in range(num_qubits)] for _ in range(len(instructors))]
    while len(instructors) > 0:
        gate, param, index = instructors[0]
        if gate == "CX":
            barriers[index[0]] += 1
            barriers[index[1]] += 1
            if index_u_cx <= index_u_noncx:
                index_u_cx = index_u_noncx
            gatess[index_u_cx][0] = instructors.pop(0)
            index_u_next_noncx = index_u_cx + 1
            instructors = operator_temp + instructors
        else:
            if barriers[index[0]] == 0:
                barriers[index[0]] += 1
                gatess[index_u_noncx][index[0]] = instructors.pop(0)
                if sum(barriers) >= num_qubits and np.all(barriers):
                    if index_u_noncx >= index_u_cx:
                        index_u_noncx += 1
                    else:
                        index_u_noncx = index_u_next_noncx
                    barriers = [0] * num_qubits
            else:
                operator_temp.append(instructors.pop(0))
    

    return gatess

gatess = operatoring(qasm_gates.copy())
gatess