def crout(A):
    n = len(A)
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]
    for i in range(n):
        L[i][0] = A[i][0]
        U[i][i] = 1
    for j in range(1, n):
        U[0][j] = A[0][j] / L[0][0]

    for i in range(1, n):  # i=1
        for j in range(1, i):  # 1,1
            L[i][j] = A[i][j] - L[i][0:j - 1] * U[0:j - 1][j]
        for j in range(i + 1, n):
            U[i][j] = (A[i][j] - L[i][0:i - 1] * U[1:i - 1][j]) / L[i][i]

    return [L, U]


