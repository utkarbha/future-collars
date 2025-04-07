balance =400
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
            balance_to_change = int(input("Type balance to add or subtract: "))
            balance += balance_to_change
            operations.append(f"Balance changed by {balance_to_change}. New balance: {balance}")
            print(f"New balance {balance}")
        elif command == "sale":
            print("Recording sale")
            product = input("Enter product name: ")
            price = int(input("Enter price per unit: "))
            quantity = int(input("Enter quantity: "))
            total_sale = price * quantity


            if product in warehouse and warehouse[product]["quantity"] >= quantity:
                warehouse[product]["quantity"] -= quantity
                balance += total_sale
                operations.append(f"Sold {quantity} {product}(s) at {price} each. Total sale = {total_sale}")
                print(f"Total sale = {total_sale}")
                print(f"{product} remaining in stock: {warehouse[product]['quantity']}")

                if warehouse[product]["quantity"] == 0:
                    print(f"{product} is now out of stock")
            else:
                print("Not enough stock or product not found. Sale not completed.")
        elif command == "purchase":
            print("Recording purchase")
            product = input("Enter product name: ")
            price = int(input("Enter price per unit: "))
            quantity = int(input("Enter quantity: "))
            total_purchase = price * quantity
            print(f"Total purchase = {total_purchase}")

            if balance >= total_purchase:
                balance -= total_purchase
                if product in warehouse:
                    warehouse[product]["quantity"] += quantity
                else:
                    warehouse[product] = {"price": price, "quantity": quantity}
                operations.append(
                    f"Purchased {quantity} {product}(s) at {price} each. Total cost = {total_purchase}")
                print(f"Purchase successful. New balance: {balance}")
            else:
                print("Insufficient funds. Purchase not completed.")

        elif command == "account":
            print(f"Account balance = {balance}")

        elif command == "list":
            print("Warehouse inventory")
            for item in warehouse:
                print(f"{item}: quantity = {warehouse[item]['quantity']}, price = {warehouse[item]['price']}")

        elif command == "warehouse":
            product = input("Enter product name: ")
            if product in warehouse:
                print(print(f"{product}: quantity = {warehouse[product]['quantity']}, price = {warehouse[product]['price']}"))
            else:
                print("product not found")
        elif command == "review":
            print("Operation History:")

        elif command == "end":
            print("Terminating")
            break
        else:
            print("Invalid command")

