# Implementing and testing the Matrix Chain Multiplication using Dynamic Programming
# Given a sequence of matrices, the goal is to find the most efficient way to multiply these matrices.
# The problem is not actually to perform the multiplications, but merely to decide the sequence of the matrix multiplications involved.

def matrix_chain_order(p):
    """
    Compute the minimum number of scalar multiplications needed to compute the product of matrices.
    """
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    
    return m[0][n - 1]

# Pytest for the matrix_chain_order function
def test_matrix_chain_order():
    assert matrix_chain_order([1, 2, 3, 4]) == 18
    assert matrix_chain_order([10, 20, 30]) == 6000
    assert matrix_chain_order([10, 20, 30, 40, 30]) == 30000
    assert matrix_chain_order([40, 20, 30, 10, 30]) == 26000

# Run the test
test_matrix_chain_order()
print("All matrix_chain_order tests passed!")
