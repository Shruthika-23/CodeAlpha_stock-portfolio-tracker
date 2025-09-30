stock_prices = {
    "AAPLE": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMAZON": 130,
    "MSFT": 310
}

portfolio = {}  
print("Welcome to Stock Portfolio Tracker ")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
while True:
    stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("Stock not available. Please try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter a number.")
total_investment = 0
print("\n Your Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares → ${value}")
print(f"\n Total Investment Value: ${total_investment}")
save_choice = input("\nDo you want to save the result in a file? (yes/no): ").lower()
if save_choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("=======================\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("✅ Portfolio saved to portfolio.txt")
