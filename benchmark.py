import psr
import time
import numpy as np
times_qiskit = []
times_pennylane = []
times_qulacs = []
for j in range(2, 17):
    for package in [psr.psr_qiskit, psr.psr_pennylane, psr.psr_qulacs]:
        start = time.time()
        package(j)
        end = time.time()
        exe_time = end-start
        if package == psr.psr_qiskit:
            times_qiskit.append(exe_time)
        elif package == psr.psr_pennylane:
            times_pennylane.append(exe_time)
        else:
            times_qulacs.append(exe_time)

np.savetxt("./times/qiskit.txt", times_qiskit)
np.savetxt("./times/pennylane.txt", times_pennylane)
np.savetxt("./times/qulacs.txt", times_qulacs)