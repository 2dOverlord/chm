def inputg():
    rows = int(input('Enter number of x: '))
    matrix = []
    for row in range(rows):
        temp_array = []
        for col in range(rows+1):
            temp_array.append(int(input(f'Enter the [{row}][{col}] element of the matrix: ')))
        matrix.append(temp_array)
    return matrix

def gauss(A):
    m = len(A)
    n = m + 1

    for k in range(m):
        pivots = [abs(A[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k

        # Check for singular matrix
        assert A[i_max][k] != 0, "Matrix is singular!"

        # Swap rows
        A[k], A[i_max] = A[i_max], A[k]

        for i in range(k + 1, m):
            f = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[k][j] * f

            # Fill lower triangular matrix with zeros:
            A[i][k] = 0

    # Solve equation Ax=b for an upper triangular matrix A
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, A[i][m] / A[i][i])
        for k in range(i - 1, -1, -1):
            A[k][m] -= A[k][i] * x[0]
    return x

# print(main(inputf())

def inputlu():
    rows = int(input('Enter number of x: '))
    matrix = []
    for row in range(rows):
        temp_array = []
        for col in range(rows):
            temp_array.append(int(input(f'Enter the [{row}][{col}] element of the matrix: ')))
        matrix.append(temp_array)
    return matrix


def LU(A):
    n = len(A)  # Give us total of lines

    # (1) Extract the b vector
    b = [0 for i in range(n)]
    for i in range(0, n):
        b[i] = A[i][n-1]

    # (2) Fill L matrix and its diagonal with 1
    L = [[0 for i in range(n)] for i in range(n)]
    for i in range(0, n):
        L[i][i] = 1

    # (3) Fill U matrix
    U = [[0 for i in range(0, n)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            U[i][j] = A[i][j]

    n = len(U)

    # (4) Find both U and L matrices
    for i in range(0, n):  # for i in [0,1,2,..,n]
        # (4.1) Find the maximun value in a column in order to change lines
        maxElem = abs(U[i][i])
        maxRow = i
        for k in range(i + 1, n):  # Interacting over the next line
            if (abs(U[k][i]) > maxElem):
                maxElem = abs(U[k][i])  # Next line on the diagonal
                maxRow = k

        # (4.2) Swap the rows pivoting the maxRow, i is the current row
        for k in range(i, n):  # Interacting column by column
            tmp = U[maxRow][k]
            U[maxRow][k] = U[i][k]
            U[i][k] = tmp

        # (4.3) Subtract lines
        for k in range(i + 1, n):
            c = -U[k][i] / float(U[i][i])
            L[k][i] = c  # (4.4) Store the multiplier
            for j in range(i, n):
                U[k][j] += c * U[i][j]  # Multiply with the pivot line and subtract

        # (4.5) Make the rows bellow this one zero in the current column
        for k in range(i + 1, n):
            U[k][i] = 0

    n = len(L)

    # (5) Perform substitutioan Ly=b
    y = [0 for i in range(n)]
    for i in range(0, n, 1):
        y[i] = b[i] / float(L[i][i])
        for k in range(0, i, 1):
            y[i] -= y[k] * L[i][k]

    n = len(U)

    # (6) Perform substitution Ux=y
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = y[i] / float(U[i][i])
        for k in range(i - 1, -1, -1):
            U[i] -= x[i] * U[i][k]

    return x

print(LU([[6, 18, 3],
          [2, 12, 1],
          [4, 15, 3]]))

