n = int(input())

parking = set()

for _ in range(n):
    activity = input().split(', ')
    if activity[0] == "IN":
        parking.add(activity[1])
    else:
        parking.remove(activity[1])

if parking:
    print(*parking, sep='\n')
else:
    print("Parking Lot is Empty")