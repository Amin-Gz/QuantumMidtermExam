import numpy as np

# Define the Pauli matrices
pauli_x = np.array([[0, 1], [1, 0]])
pauli_y = np.array([[0, -1j], [1j, 0]])
pauli_z = np.array([[1, 0], [0, -1]])

# Compute eigenvalues and eigenvectors, orthonormal decompositions, and diagonal representations
pauli_matrices = [pauli_x, pauli_y, pauli_z]

for pauli_matrix in pauli_matrices:
    eigenvalues, eigenvectors = np.linalg.eig(pauli_matrix)
    diagonal_matrix = np.diag(eigenvalues)
    orthonormal_matrix = np.conjugate(np.transpose(eigenvectors))
    
    print("Pauli matrix:")
    print(pauli_matrix)
    print("Eigenvalues:")
    print(eigenvalues)
    print("Eigenvectors:")
    print(eigenvectors)
    print("Orthonormal Decomposition:")
    print(orthonormal_matrix)
    print("Diagonal Representation:")
    print(diagonal_matrix)
    print("----------------------------------")