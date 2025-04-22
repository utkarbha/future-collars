import os
from ast import literal_eval


BALANCE_FILE = 'balance.txt'
WAREHOUSE_FILE = 'warehouse.txt'
OPERATIONS_FILE = 'operations.txt'


balance = 400
warehouse = {
    "bike": {
        "price": 100,
        "quantity": 10
    },
    "computer": {
        "price": 2300,
        "quantity": 3
    }
}
operations = []

# === Load data from files ===
def load_data():
    global balance, warehouse, operations
    try:
        if os.path.exists(BALANCE_FILE):
            with open(BALANCE_FILE, 'r') as f:
                balance = int(f.read().strip())

        if os.path.exists(WAREHOUSE_FILE):
            with open(WAREHOUSE_FILE, 'r') as f:
                warehouse = literal_eval(f.read())

        if os.path.exists(OPERATIONS_FILE):
            with open(OPERATIONS_FILE, 'r') as f:
                operations = literal_eval(f.read())

        print("Data loaded successfully.\n")
    except Exception as e:
        print(f" Error loading data: {e}")
        print("Starting with default values.")


def save_data():
    try:

        with open('balance.txt', 'w') as file:
            file.write(str(balance))


        with open('warehouse.txt', 'w') as file:
            file.write(str(warehouse))


        with open('operations.txt', 'w') as file:
            file.write(str(operations))
    except Exception as e:
        print(f"Error saving data: {e}")





def handle_balance():
    global balance
    print("Changing balance")
    try:
        balance_to_change = int(input("Type balance to add or subtract (use + or -): "))
        balance += balance_to_change
        operations.append(f"Balance changed by {balance_to_change}. New balance: {balance}")
        print(f"New balance: {balance}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def handle_sale():
    global balance
    print("Recording sale")
    try:
        product = input("Enter product name: ")
        if product not in warehouse:
            print("Error: Product not in warehouse")
            return

        price = int(input("Enter price per unit: "))
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Error: Quantity must be positive")
            return

        if warehouse[product]["quantity"] < quantity:
            print(f"Error: Not enough stock. Only {warehouse[product]['quantity']} available")
            return

        total_sale = price * quantity
        balance += total_sale
        warehouse[product]["quantity"] -= quantity
        operations.append(f"Sold {quantity} {product}(s) at {price} each. Total: {total_sale}")
        print(f"Sale recorded. New balance: {balance}")

        if warehouse[product]["quantity"] == 0:
            del warehouse[product]
            print(f"{product} is now out of stock")
    except ValueError:
        print("Invalid input. Please enter numbers for price and quantity.")

def handle_purchase():
    global balance
    print("Recording purchase")
    try:
        product = input("Enter product name: ")
        price = int(input("Enter price per unit: "))
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Error: Quantity must be positive")
            return

        total_cost = price * quantity
        if balance < total_cost:
            print(f"Error: Insufficient funds. Need {total_cost}, have {balance}")
            return

        balance -= total_cost
        if product in warehouse:
            warehouse[product]["quantity"] += quantity
            warehouse[product]["price"] = price
        else:
            warehouse[product] = {"price": price, "quantity": quantity}

        operations.append(f"Purchased {quantity} {product}(s) at {price} each. Total: {total_cost}")
        print(f"Purchase recorded. New balance: {balance}")
    except ValueError:
        print("Invalid input. Please enter numbers for price and quantity.")

def handle_account():
    print(f"Current account balance: {balance}")

def handle_list():
    print("Current warehouse inventory:")
    for product, details in warehouse.items():
        print(f"{product}: {details['quantity']} units at {details['price']} each")

def handle_warehouse():
    product = input("Enter product name to check: ")
    if product in warehouse:
        details = warehouse[product]
        print(f"{product}: {details['quantity']} in stock at {details['price']} each")
    else:
        print("Product not found in warehouse")

def handle_review():
    print("Recorded operations:")
    for i, op in enumerate(operations, 1):
        print(f"{i}. {op}")


def main():
    load_data()

    while True:
        print("\nAvailable commands: balance, sale, purchase, account, list, warehouse, review, end")
        command = input("Enter command: ")

        if command == "balance":
            handle_balance()
        elif command == "sale":
            handle_sale()
        elif command == "purchase":
            handle_purchase()
        elif command == "account":
            handle_account()
        elif command == "list":
            handle_list()
        elif command == "warehouse":
            handle_warehouse()
        elif command == "review":
            handle_review()
        elif command == "end":
            save_data()
            print("Exiting program...")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()