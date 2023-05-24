class Stock:
    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price

    def update_price(self, new_price):
        self.price = new_price


class TradingSystem:
    def __init__(self):
        self.stocks = []

    def add_stock(self, symbol, name, price):
        stock = Stock(symbol, name, price)
        self.stocks.append(stock)
        print("Stock added successfully.")

    def update_stock_price(self, symbol, new_price):
        for stock in self.stocks:
            if stock.symbol == symbol:
                stock.update_price(new_price)
                print("Stock price updated successfully.")
                return
        print("Stock not found.")

    def view_stock_details(self):
        if not self.stocks:
            print("No stocks available.")
        else:
            print("Stock Details:")
            for stock in self.stocks:
                print(f"Symbol: {stock.symbol}")
                print(f"Name: {stock.name}")
                print(f"Price: {stock.price}")
                print("-------------------------")


def menu():
    trading_system = TradingSystem()
    while True:
        print("\n--- Stock Market Trading System ---")
        print("1. Add a stock")
        print("2. Update stock price")
        print("3. View stock details")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            name = input("Enter stock name: ")
            price = float(input("Enter stock price: "))
            trading_system.add_stock(symbol, name, price)

        elif choice == "2":
            symbol = input("Enter stock symbol to update price: ")
            new_price = float(input("Enter new stock price: "))
            trading_system.update_stock_price(symbol, new_price)

        elif choice == "3":
            trading_system.view_stock_details()

        elif choice == "4":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
menu()