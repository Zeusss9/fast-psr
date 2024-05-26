import qiskit

import numpy as np
import utilities


def qc_to_qcs_noncontrol2(qc: qiskit.QuantumCircuit) -> list[qiskit.QuantumCircuit]: 
    qcs = []
    sub_qc = qiskit.QuantumCircuit(qc.num_qubits)
    counter = 0
    active_2qubit = 0 # 0 mean dactive, 1 mean active, 2 mean break instruction
    slots = np.zeros(qc.num_qubits)
    for _, qargs, _ in qc.data: 
        indices = utilities.get_qubit_indices(qargs)
        if len(indices) == 2:
            active_2qubit += 1
        
        slots = utilities.update_slot(slots, indices)
        if any(slot > 1 for slot in slots) or active_2qubit == 2:
            qcs.append(sub_qc)
            active_2qubit = 0
            sub_qc = qiskit.QuantumCircuit(qc.num_qubits)
            sub_qc.append(qc[counter][0], qc[counter][1])
            if len(indices) == 2:
                active_2qubit += 1
            slots = np.zeros(qc.num_qubits)
            slots = utilities.update_slot(slots, utilities.get_qubit_indices(qargs))
            qc.data = qc.data[counter + 1:]
            counter = 0
        else:
            sub_qc.append(qc[counter][0], qc[counter][1])
            counter += 1
            if counter >= len(qc.data):
                qcs.append(sub_qc)
                return qcs
    return qcs

def qc_to_qcs_noncontrol(qc: qiskit.QuantumCircuit) -> list[qiskit.QuantumCircuit]:    
    """Split n-depth circuit into n sub-circuits, each sub-circuit does not have > 2 2-qubit gates

    Args:
        qc (qiskit.QuantumCircuit): Original circuit

    Returns:
        list[qiskit.QuantumCircuit]: Splitted circuit depth by depth
    """
    def valid_forward(qc: qiskit.QuantumCircuit, x) -> bool:
        count = 0
        qc.append(x[0], x[1])
        for _, qargs, _ in qc.data:
            if len(qargs) == 2:
                count += 1
        if qc.depth() == 1 and count < 2:
            return True
        return False
    depth = qc.depth()
    qcs = []
    if depth < 0:
        raise "The depth must be >= 0"
    sub_qc = qiskit.QuantumCircuit(qc.num_qubits)
    counter = 0 
    while(True):
        valid = valid_forward(sub_qc.copy(), qc[counter])
        if valid:
            sub_qc.append(qc[counter][0], qc[counter][1])
            counter += 1
        if valid is False or counter == len(qc.data):
            qc.data = qc.data[counter:]
            qcs.append(sub_qc)
            counter = 0
            sub_qc = qiskit.QuantumCircuit(qc.num_qubits)
        if len(qc.data) == 0:
            break
    return qcs



def qc_to_qcs(qc: qiskit.QuantumCircuit) -> list[qiskit.QuantumCircuit]:    
    """Split n-depth circuit into n sub-circuits

    Args:
        qc (qiskit.QuantumCircuit): Original circuit

    Returns:
        list[qiskit.QuantumCircuit]: Splitted circuit depth by depth
    """
    def look_forward(qc: qiskit.QuantumCircuit, x):
        qc.append(x[0], x[1])
        return qc
    depth = qc.depth()
    qcs = []
    if depth < 0:
        raise "The depth must be >= 0"
    for _ in range(depth):
        qc1 = qiskit.QuantumCircuit(qc.num_qubits)
        counter = 0
        if qc.depth() == 1:
            qcs.append(qc)
            return qcs
        for i in range(len(qc)):
            qc1.append(qc[i][0], qc[i][1])
            counter += 1
            if qc1.depth() == 1 and look_forward(qc1.copy(), qc[i+1]).depth() > 1:
                qc.data = qc.data[counter:]
                qcs.append(qc1)
                counter = 0
                break
    return qcs