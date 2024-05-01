import cirq

# Define qubits
q0 = cirq.GridQubit(0, 0)  # Input qubit A
q1 = cirq.GridQubit(1, 0)  # Input qubit B
q2 = cirq.GridQubit(2, 0)  # Output qubit S
q3 = cirq.GridQubit(3, 0)  # Output qubit C

# Define circuit
circuit = cirq.Circuit()

# Add gates to the circuit
circuit.append([
    cirq.H(q0),            # Apply Hadamard gate to qubit A
    cirq.CNOT(q0, q2),     # Apply CNOT gate between qubit A and output qubit S
    cirq.CNOT(q0, q3),     # Apply CNOT gate between qubit A and output qubit C
    cirq.CNOT(q1, q2),     # Apply CNOT gate between qubit B and output qubit S
    cirq.CCX(q0, q1, q3),  # Apply Toffoli gate between qubit A, B, and output qubit C
])

# Measure the output qubits
circuit.append([cirq.measure(q2), cirq.measure(q3)])

# Print the circuit
print("Half Adder Circuit:")
print(circuit)
