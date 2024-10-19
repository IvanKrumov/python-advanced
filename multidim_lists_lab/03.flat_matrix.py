rows = int(input())

flatmat = []
for row  in range(rows):
    row_elements = [int(i) for i in input().split(", ")]
    for el in row_elements:
        flatmat.append(el)
    

print(flatmat)
