

price = 0
number = None

try:
    number = int(input("Number of Item: "))
    while number < 0:
        print("Invalid input!")
        number = int(input("Number of Item: "))
    for i in range(number):
        item_price = float(input("Price of item: "))
        price += item_price

    if price > 100:
        price = price * ((100 - 10) / 100)
except ValueError:
    print("Invalid input!")
    print("Program closed!")

if price > 0:
    print(f"Total price of {number} items is ${price:.2f}")
