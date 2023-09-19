car = "BMW"
cars = ['BMW M5', 'Nissan GTR', 'Toyota Supra']
prices = [120_000, 100_000, 43_000]
top_car = ['Supra', 43_000, 3.6]

info = []

print(f"{cars[0]}: ${prices[0]}")
print(f"{cars[1]}: ${prices[1]}")
print(prices[0] + prices[1])
print(cars[-1])

prices[0] = prices[0] - 20_000

top_car[0] = 'Nissan GTR'
top_car.append('black')
top_car.insert(0, 'Super car')
# del top_car[-1]
top_car.remove('black')
car1 = top_car.pop(0)


