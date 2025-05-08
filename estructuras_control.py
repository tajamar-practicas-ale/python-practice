count = 0

n1 = 15
n2 = 3

while count < 3:
    for i in range(1):
        if count == 0:
            print(f"15 + 3 = {n1+n2}")
        elif count == 1:
            print(f"15 - 3 = {n1-n2}")
        elif count == 2: 
            print(f"15 * 3 = {n1*n2}")
    count += 1
print("Se ha realizado tres operaciones")