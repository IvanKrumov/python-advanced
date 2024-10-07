m, n = input().split()
# m, n = map(int, input().split())

set_m = set()
set_n = set()

for i in range(int(m)):
    num = int(input())
    set_m.add(num)

for i in range(int(n)):
    num = int(input())
    set_n.add(num)

# result = set_m.intersection(set_n)

print(*(set_m & set_n), sep='\n')