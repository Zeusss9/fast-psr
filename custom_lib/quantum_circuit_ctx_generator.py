import qiskit
import ansatz
import numpy as np
from qimax import converter, constant
from . import fixed_point_handler

def read_file(file_name):
    lines = []
    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line.strip())

    return lines

def write_file(file_name, lines):
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line + '\n')

def generate_quantum_circuit_data(num_qubits=3, quanvolutional_idx=1, basis_gate_list=['h', 's', 'cx', 'rx', 'ry', 'rz'], output_file_path='output.txt'):
    qc = qiskit.QuantumCircuit(num_qubits) 

    if(quanvolutional_idx == 1):
        qc = ansatz.quanvolutional1(qc)
    elif(quanvolutional_idx == 2):
        qc = ansatz.quanvolutional2(qc)
    elif(quanvolutional_idx == 3):
        qc = ansatz.quanvolutional3(qc)
    elif(quanvolutional_idx == 4):
        qc = ansatz.quanvolutional4(qc)
    elif(quanvolutional_idx == 5):
        qc = ansatz.quanvolutional5(qc)
    elif(quanvolutional_idx == 6):
        qc = ansatz.quanvolutional6(qc)
    elif(quanvolutional_idx == 7):
        qc = ansatz.quanvolutional7(qc)
    elif(quanvolutional_idx == 8):
        qc = ansatz.quanvolutional8(qc)
    elif(quanvolutional_idx == 9):
        qc = ansatz.quanvolutional9(qc)
    elif(quanvolutional_idx == 10):
        qc = ansatz.quanvolutional10(qc)
    elif(quanvolutional_idx == 11):
        qc = ansatz.quanvolutional11(qc)
    elif(quanvolutional_idx == 12):
        qc = ansatz.quanvolutional12(qc)
    elif(quanvolutional_idx == 13):
        qc = ansatz.quanvolutional13(qc)
    elif(quanvolutional_idx == 14):
        qc = ansatz.quanvolutional14(qc)
    elif(quanvolutional_idx == 15):
        qc = ansatz.quanvolutional15(qc)
    elif(quanvolutional_idx == 16):
        qc = ansatz.quanvolutional16(qc)
    elif(quanvolutional_idx == 17):
        qc = ansatz.quanvolutional17(qc)
    elif(quanvolutional_idx == 18):
        qc = ansatz.quanvolutional18(qc)
    elif(quanvolutional_idx == 19):
        qc = ansatz.quanvolutional19(qc)
        
    qc = qiskit.transpile(circuits=qc, basis_gates=basis_gate_list, optimization_level=3)
    # qc.draw(output='mpl').savefig('qc.png')

    # Convert to readable files
    texts = []
    texts.append(len(qc.data))
    for gate in qc.data:
        name = gate.name.upper()
        params = None
        wires = converter.get_wires_of_gate(gate)

        if name == 'CX':
            type = 2
        else:
            type = 1
            gate_entries = constant.constant_gate[name]
            if name in ['RX', 'RY', 'RZ']:
                params = gate.params[0]
                gate_entries = gate_entries(params)
        texts.append(type)
        if type == 2:
            texts.append("{" + str(wires[0]) + ", "+ str(wires[1]) + "}")
            # texts.append(wires[1])
        else:
            texts.append(wires[0])
            texts.append(gate_entries[0][0])
            texts.append(gate_entries[0][1])
            texts.append(gate_entries[1][0])
            texts.append(gate_entries[1][1])

    with open(output_file_path, 'w') as f:
        for item in texts:
            f.write("%s\n" % item)

def generate_quantum_circuit_ctx(bit_width=32, fraction_width=30, raw_file_path='output.txt', processed_file_path='output_hex.txt'):
    raw_data = read_file(raw_file_path)
    processed_data = []

    print("Raw data: ")
    print(raw_data)

    sub_idx = 0
    gate_type = 1 # 0: Sprase, 1: Dense, 2: CX
    for index, line in enumerate(raw_data):
        if index == 0: # Number of gates
            bin_data = fixed_point_handler.int_to_binary(number=int(line.strip()), bit_width=bit_width*2)
            hex_data = fixed_point_handler.binary_to_hex(binary_str=bin_data, bit_width=bit_width*2)
            processed_data.append(hex_data[2:])

            print("Number of gates: ", line.strip())
        else:
            if(sub_idx == 0): # Process gate type
                gate_type = int(line.strip())

                bin_data = fixed_point_handler.int_to_binary(number=int(line.strip()), bit_width=bit_width*2)
                hex_data = fixed_point_handler.binary_to_hex(binary_str=bin_data, bit_width=bit_width*2)

                sub_idx = sub_idx + 1
                processed_data.append(hex_data[2:])

                print("Gate type: ", "Dense" if(gate_type == 1) else "CX")
            elif(sub_idx == 1):
                if(gate_type == 1): # Process dense gate position
                    bin_data = fixed_point_handler.int_to_binary(number=int(line.strip()), bit_width=bit_width*2)
                    hex_data = fixed_point_handler.binary_to_hex(binary_str=bin_data, bit_width=bit_width*2)

                    sub_idx = sub_idx + 1
                    processed_data.append(hex_data[2:])

                    print("Gate position: ", line.strip())
                elif(gate_type == 2): # Process CX gate position
                    ctrl_pos, tgt_pos = line.strip("{}").split(", ")

                    ctrl_pos_binary = fixed_point_handler.int_to_binary(number=int(ctrl_pos), bit_width=bit_width)
                    tgt_pos_binary = fixed_point_handler.int_to_binary(number=int(tgt_pos), bit_width=bit_width)

                    ctrl_pos_hex = fixed_point_handler.binary_to_hex(binary_str=ctrl_pos_binary, bit_width=bit_width)
                    tgt_pos_hex = fixed_point_handler.binary_to_hex(binary_str=tgt_pos_binary, bit_width=bit_width)

                    sub_idx = 0
                    processed_data.append(ctrl_pos_hex[2:]+tgt_pos_hex[2:])

                    print("Control position: ", ctrl_pos, "| Target position: ", tgt_pos)
            else: # Process dense gate entries
                if(gate_type):
                    if(line[0] == '('):
                        line = line.strip("()")
                        
                    line = line.strip("")
                    compl_num = complex(line)

                    real_part = compl_num.real
                    imaginary_part = compl_num.imag
                    
                    print("Gate entries: ", real_part + 1j*imaginary_part)

                    real_part_binary = fixed_point_handler.convert_fixedpoint_to_binary(number=real_part, bit_width=bit_width, dot_position=fraction_width)
                    imaginary_part_binary = fixed_point_handler.convert_fixedpoint_to_binary(number=imaginary_part, bit_width=bit_width, dot_position=fraction_width)

                    real_part_hex = fixed_point_handler.binary_to_hex(binary_str=real_part_binary, bit_width=bit_width)
                    imaginary_part_hex = fixed_point_handler.binary_to_hex(binary_str=imaginary_part_binary, bit_width=bit_width)

                    if(sub_idx < 5):
                        sub_idx = sub_idx + 1
                    else:
                        sub_idx = 0
                        

                    processed_data.append(real_part_hex[2:]+imaginary_part_hex[2:])

    write_file(processed_file_path, processed_data)

# # Result from Qiskit
# qc_qiskit = (qiskit.quantum_info.Statevector.from_instruction(qc).data)
# print(qc_qiskit)


# # Calculate error
# def fidelity(state1: np.ndarray, state2: np.ndarray):
#     state1 = np.expand_dims(state1, axis=0)
#     state2 = np.expand_dims(state2, axis=0)
#     return (np.abs(np.inner(np.conjugate(state1), state2))**2)[0][0]


# def mse(state1: np.ndarray, state2: np.ndarray):
#     return np.mean(np.abs(state1 - state2)**2)

# qc_fpga = ?
# print(fidelity(qc_qiskit, qc_fpga))
# print(mse(qc_qiskit, qc_fpga))