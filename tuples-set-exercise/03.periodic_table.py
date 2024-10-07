n = int(input())

elements = set()

for _ in range(n):
    elements_list = input().split()
    for el in elements_list:
        elements.add(el)

print(*elements, sep='\n')