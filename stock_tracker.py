stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 140,
    "MSFT": 300
}

total = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("\nEnter Stock Name (AAPL, TSLA, GOOGLE, AMZN, MSFT): ").upper()

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity
    total += investment

    print(f"Investment in {stock}: ${investment}")

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n==============================")
print("Total Investment Value = $", total)
print("==============================")
