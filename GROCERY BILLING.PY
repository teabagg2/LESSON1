# Grocery Billing Queue Program
# Uses nested while loops, continue, and nested for loops

customers = []
all_items = []


def get_valid_int(prompt, minimum=0):
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("Empty input")

            number = int(value)
            if number < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue

            return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except EOFError:
            print("\nInput cancelled. Exiting program.")
            raise SystemExit(0)


def get_valid_price(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("Empty input")

            price = float(value)
            if price <= 0:
                print("Invalid price. Try again.")
                continue

            return price
        except ValueError:
            print("Invalid input. Please enter a valid price.")
        except EOFError:
            print("\nInput cancelled. Exiting program.")
            raise SystemExit(0)


try:
    total_customers = get_valid_int("Enter number of customers: ", minimum=0)
except SystemExit:
    raise

if total_customers == 0:
    print("No customers to process.")
    raise SystemExit(0)

customer_count = 0

# Outer while loop - handles customers
while customer_count < total_customers:
    print(f"\nCustomer {customer_count + 1}")

    items = []
    customer_total = 0

    item_count = get_valid_int("Enter number of grocery items: ", minimum=0)

    current_item = 0

    # Inner while loop - handles grocery items
    while current_item < item_count:
        item_name = input("Enter item name: ").strip()
        if not item_name:
            print("Item name cannot be empty. Try again.")
            continue

        price = get_valid_price("Enter item price: ")

        items.append((item_name, price))
        all_items.append((item_name, price))
        customer_total += price

        current_item += 1

    customers.append(customer_total)

    print(f"Customer {customer_count + 1} Total: ${customer_total:.2f}")

    customer_count += 1


# Final Price Category Report
print("\n===== Price Category Report =====")

categories = {
    "Low Price Items": [],
    "Medium Price Items": [],
    "High Price Items": []
}

# Nested for loops
for item in all_items:
    name, price = item

    for category in categories:
        if category == "Low Price Items" and price < 10:
            categories[category].append(name)

        elif category == "Medium Price Items" and 10 <= price <= 50:
            categories[category].append(name)

        elif category == "High Price Items" and price > 50:
            categories[category].append(name)


# Display report
for category, items in categories.items():
    print("\n" + category)

    if items:
        for item in items:
            print("-", item)
    else:
        print("No items")


# Final billing summary
print("\n===== Billing Summary =====")

for index, total in enumerate(customers):
    print(f"Customer {index + 1}: ${total:.2f}")

print(f"\nTotal Customers Served: {total_customers}")
print(f"Total Revenue: ${sum(customers):.2f}")
print("\nFinal Price Category Report:")

low_items = len(categories["Low Price Items"])
medium_items = len(categories["Medium Price Items"])
high_items = len(categories["High Price Items"])

categories_list = ["Low Price Items", "Medium Price Items", "High Price Items"]
amounts = [low_items, medium_items, high_items]

for slot in range(3):   # outer for loop - categories
    print(f"{categories_list[slot]}: {amounts[slot]}")
    for _ in range(amounts[slot]):   # inner for loop - symbols
        print("*", end="")
    print()

customers_served = total_customers
total_sales = sum(customers)

print("\nDaily Grocery Summary:")
print(f"Customers served: {customers_served}")
print(f"Total sales: ${total_sales:.2f}")
print("Thank you for shopping!")
print("Grocery billing session closed. Goodbye!")
