print("Package Loading System")
print("----------------------")

# Get maximum number of items
while True:
    max_items = input("Enter the maximum number of items to be shipped: ")
    if max_items.isdigit():
        max_items = int(max_items)
        if max_items > 0:
            break
        else:
            print("Please enter a positive number.")
    else:
        print("Invalid input. Please enter a valid number.")

packages = []
current_package = 0
items_processed = 0

while items_processed < max_items:
    weight_input = input(f"Enter weight of item {items_processed + 1} (1-10 kg, 0 to stop): ")

    # Check if input is numeric
    if not weight_input.replace('.', '').isdigit():
        print("Invalid input. Please enter a number.")
        continue

    weight = float(weight_input)

    # Check for termination
    if weight == 0:
        print("\nTermination requested (0 kg entered).")
        break

    # Validate weight range
    if weight < 1 or weight > 10:
        print("Weight must be between 1 and 10 kg (or 0 to stop).")
        continue

    # Check package capacity
    if current_package + weight > 20:
        packages.append(current_package)
        current_package = weight
    else:
        current_package += weight

    items_processed += 1

# Add the last package if it has items
if current_package > 0:
    packages.append(current_package)

# Calculate statistics
num_packages = len(packages)
total_weight = 0
total_unused = 0
max_unused = 0
max_unused_pkg = 0

i = 0
while i < num_packages:
    total_weight += packages[i]
    unused = 20 - packages[i]
    total_unused += unused
    if unused > max_unused:
        max_unused = unused
        max_unused_pkg = i + 1
    i += 1

# Display results
print("\nResults:")
print(f"Number of packages sent: {num_packages}")
print(f"Total weight of packages sent: {total_weight} kg")

if num_packages > 0:
    print(f"Total 'unused' capacity: {total_unused} kg")
    print(f"Package with most 'unused' capacity: Package {max_unused_pkg} with {max_unused} kg unused")
else:
    print("No packages were sent.")