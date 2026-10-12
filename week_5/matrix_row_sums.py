def matrix_row_sums(matrixs: list):
    for index, matrix in enumerate(matrixs, start=1):
        total = 0

        for num in matrix:
            total += num

        print(f"Row {index} total: {total}")


matrixs= [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
result = matrix_row_sums(matrixs)
print(result)