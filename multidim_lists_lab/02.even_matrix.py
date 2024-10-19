rows = int(input())

matrix = []

for row  in range(rows):
    row_elements = [int(i) for i in input().split(", ") if int(i) % 2 == 0]
    matrix.append(row_elements)

print(matrix)
