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
            print(f"New balance {balance}")
        elif command == "sale":
             print("sale")
             product = input("Enter product name: ")
             price = int(input("Enter price per unit: "))
             quantity = int(input("Enter quantity: "))
        total_sale = price * quantity
        print(f"Total sale = {total_sale}")
        operations.append(f"sold{quantity} {product}. Total sale = {total_sale}")
        if warehouse[product]["quantity"] == 0:

            print(f"{product} is now out of stock")
        elif command == "purchase":
            print("Recording purchase")

                product = input("Enter product name: ")
                price = int(input("Enter price per unit: "))
                quantity = int(input("Enter quantity: "))