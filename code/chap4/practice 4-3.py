total = 0

for i in range(1, 51):
    if i % 2 == 0 and i % 3 != 0:
        total += i

print("합: ", total)