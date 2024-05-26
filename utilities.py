import qiskit

def duplicate_xss(xss):
    return [xs.copy() for xs in xss for _ in range(2)]

def update_slot(slots, B):
    for b in B:
        slots[b] += 1
    return slots

def get_qubit_indices(qargs):
    return [q.index for q in qargs]