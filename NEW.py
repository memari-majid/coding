import math
arr = [7, 1, 5, 3, 6, 4]

min_price = 10
max_profit = 0
for i in range(len(arr)):
    if arr[i] < min_price:
        min_price = arr[i]
        print(min_price)
    elif arr[i] - min_price > max_profit:
        max_profit = arr[i] - min_price

print(min_price, max_profit)