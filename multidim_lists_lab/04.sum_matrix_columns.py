rows, cols = [int(i) for i in input().split(", ")]

matrix = []

for row  in range(rows):
    row_elements = [int(i) for i in input().split(" ")]
    matrix.append(row_elements)    

for col in range(cols):
    sum_col = 0
    for row in range(rows):
        sum_col += matrix[row][col]
    print(sum_col)
