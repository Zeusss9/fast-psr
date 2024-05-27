import qiskit.quantum_info as qi
import qimax.constant
from qoop.core.random_circuit import generate_with_pool
from qoop.core.gradient import grad_loss
num_qubits = 4
qc = generate_with_pool(num_qubits, 2)
qc = qc.assign_parameters([1] * qc.num_parameters)
class U():
    def __init__(self, params_form, tensor_form, index = 0):
        self.params_form = params_form
        self.tensor_form = tensor_form
        self.matrix_form = None
        self.index = index
    def plus_params_form(self, plus: int):
        # add plus to the 
        self.params_form = params_form
        return self
    def compare(self, us):
        for u in us:
            if self.params_form == u.params_form and self.tensor_form == u.tensor_form:
                self.index = u.index
                self.matrix_form = u.matrix_form
                return True
        return False
    def to_matrix(self):
        if self.matrix_form is None:
            self.matrix_form = qimax.converter.string_to_matrix(self.params_form, self.tensor_form)
        return self.matrix_form

import qimax.constant
import qimax.converter
import qimax.splitter
matrices = []
Us = []
Usm = [] # [U_{0:m-1}, U_{1:m-1}, ... U_{m-1:m-1}]
index = 0
print(qc.draw())
qasm_gates = qimax.converter.qasm_to_qasmgates(qc.qasm())
qcs = qimax.splitter.qasmgates_to_qcs2(qasm_gates)
#qcs.reverse() 
for qasmgates in qcs:
    gates = qimax.converter.qasmgates_to_gates(qasmgates)
    params_form, tensor_form = qimax.converter.gates_to_string(gates, num_qubits)
    u = U(params_form, tensor_form, index)
    if u.compare(Us) == False:
        index += 1
        u.to_matrix()
    Us.append(u)
for u in Us:
    print(u.params_form)



