def zero_matrix(matrix):
    zero_cols = set()
    zero_rows = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_cols.add(i)
                zero_rows.add(j)
    for col in zero_cols:
        for i in range(len(matrix[0])):
            matrix[col][i] = 0
    for row in zero_rows:
        for i in range(len(matrix)):
            matrix[i][row] = 0
