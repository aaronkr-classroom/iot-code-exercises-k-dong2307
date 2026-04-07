total = 0
i = 1

while i <= 50:
    if i % 2 == 0 and i % 3 != 0:
        total += i
    i += 1
    
print("합: ", total)