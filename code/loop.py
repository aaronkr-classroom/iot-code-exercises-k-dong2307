cars = ["Hyundai", "BMW", "Porche", "Tesla"]

for car in cars:
    print(f"My new car is a {car}!")
    
prices = [i ** 2 for i in range(12) if i % 2 == 0]
for price in prices:
    print(f"It cost {price}!")