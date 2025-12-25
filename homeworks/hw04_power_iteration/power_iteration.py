import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    assert data.shape[0] == data.shape[1]
    
    eigenvector = np.random.random(data.shape[0])
    for _ in range(num_steps):
        eigenvector = data@eigenvector
        eigenvector = eigenvector/np.linalg.norm(eigenvector, ord=2)
    eigenvalue = (eigenvector@data@eigenvector)/(eigenvector@eigenvector)

    return float(eigenvalue), eigenvector