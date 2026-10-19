matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]

# Row 1 total: 12 | Row 1 average: 4.0
# Row 2 total: 9 | Row 2 average: 3.0
# Row 3 total: 60 | Row 3 average: 20.0

# Column 1 total: 13
# Column 2 total: 27
# Column 3 total: 41

def rows(matrix: list[int]) -> str:
    for index, numbers in enumerate(matrix):
        
        start = len(matrix)
        end = 0
        
        while start > end:
            total = 0
            
            for number in numbers:
                total += number
            
            average = total / len(numbers)
                
            print(f"Row {index + 1} total: {total} | Row {index + 1} average: {average}")
            
            break
                                      
        end += 1

def columns(matrix: list[list[int]]) -> list[int]:
        
    num_cols = len(matrix[0])
    col_sums = []
    
    for col_index in range(num_cols):
        total = 0
        for row in matrix:
            total += row[col_index]
        col_sums.append(total)
        
    for index, number in enumerate(col_sums):
        print(f"Column {index + 1} total: {number}")


rows(matrix)
columns(matrix)