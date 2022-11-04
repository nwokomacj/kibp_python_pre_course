# Write your solution below
# Follow the instructions in the tab to the right

# Use this exchange rate
NAIRA_PER_DOLLAR = 410.59 # exchange rate as of Nov 10 2021
Dollars = input("Enter the amount of USD to convert to naiara: ")
print()
DOLLAR = float(Dollars)
value = NAIRA_PER_DOLLAR * DOLLAR
print()
print(f"{value:.2f} NGN")