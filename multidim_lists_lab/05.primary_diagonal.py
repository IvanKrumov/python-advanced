rows = int(input())

diagonal = []
for row  in range(rows):
    row_elements = [int(i) for i in input().split(" ")]
    diagonal.append(row_elements[row])
    

print(sum(diagonal))
