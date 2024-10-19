rows, cols = [int(i) for i in input().split(", ")]

matrix = []
sum_elements = 0
for row  in range(rows):
    row_elements = [int(i) for i in input().split(", ")]
    matrix.append(row_elements)
    sum_elements += sum(row_elements)

print(sum_elements)
print(matrix)
