
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

while True:
    print("\nAvailable commands: balance, sale, purchase, account, list, warehouse, review, end")
    command = input("Enter command: ")

    if command == "balance":
        print("Changing balance")
        try:
            balance_to_change = int(input("Type balance to add or subtract (use + or -): "))
            balance += balance_to_change
            operations.append(f"Balance changed by {balance_to_change}. New balance: {balance}")
            print(f"New balance: {balance}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif command == "sale":
        print("Recording sale")
        try:
            product = input("Enter product name: ")
            if product not in warehouse:
                print("Error: Product not in warehouse")
                continue

            price = int(input("Enter price per unit: "))
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Error: Quantity must be positive")
                continue

            if warehouse[product]["quantity"] < quantity:
                print(f"Error: Not enough stock. Only {warehouse[product]['quantity']} available")
                continue

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

    elif command == "purchase":
        print("Recording purchase")
        try:
            product = input("Enter product name: ")
            price = int(input("Enter price per unit: "))
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Error: Quantity must be positive")
                continue

            total_cost = price * quantity
            if balance < total_cost:
                print(f"Error: Insufficient funds. Need {total_cost}, have {balance}")
                continue

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

    elif command == "account":
        print(f"Current account balance: {balance}")

    elif command == "list":
        print("Current warehouse inventory:")
        for product, details in warehouse.items():
            print(f"{product}: {details['quantity']} units at {details['price']} each")

    elif command == "warehouse":
        product = input("Enter product name to check: ")
        if product in warehouse:
            details = warehouse[product]
            print(f"{product}: {details['quantity']} in stock at {details['price']} each")
        else:
            print("Product not found in warehouse")

    elif command == "review":
        print("Recorded operations:")
        for i, op in enumerate(operations, 1):
            print(f"{i}. {op}")

    elif command == "end":
        print("Ending program...")
        break

    else:
        print("Invalid command. Please try again.")