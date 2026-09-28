# Hardcoded stock prices (in dollars)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
}


def main():
    print("=== STOCK PORTFOLIO TRACKER ===")
    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nEnter stock name and quantity. Type 'done' to finish.\n")

    portfolio = {}   # stock name -> quantity

    while True:
        stock = input("Stock name: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found. Choose from the list above.\n")
            continue

        qty_text = input(f"Quantity of {stock}: ").strip()
        if not qty_text.isdigit() or int(qty_text) <= 0:
            print("Please enter a valid whole number greater than 0.\n")
            continue

        # If the same stock is entered again, add to the existing quantity
        portfolio[stock] = portfolio.get(stock, 0) + int(qty_text)
        print(f"Added {qty_text} x {stock}\n")

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    # Calculate and display the summary
    total = 0
    lines = []
    lines.append("--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        value = STOCK_PRICES[stock] * qty
        total += value
        lines.append(f"{stock}: {qty} x ${STOCK_PRICES[stock]} = ${value}")
    lines.append("-------------------------")
    lines.append(f"Total Investment: ${total}")

    print()
    for line in lines:
        print(line)

    # Optional: save result to a text file
    choice = input("\nSave result to a file? (y/n): ").lower().strip()
    if choice == "y":
        with open("portfolio.txt", "w") as f:
            f.write("\n".join(lines))
        print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()
