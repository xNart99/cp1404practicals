income_list = []

months = int(input("How many months? "))

for month in range(1, months + 1):
    income = float(input(f"Enter income or a month {month}: "))
    income_list.append(income)

print("\nIncome Report\n-------------")

total = 0

for month in range(1, months + 1):
    income = income_list[month - 1]
    total += income
    print(f"Month {month} - Income: ${income_list[month - 1]:.2f} \t Total: ${total:.2f}")


