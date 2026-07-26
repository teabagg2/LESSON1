# Grocery Billing Queue Program
# Uses nested while loops, continue, and nested for loops

customers = []
all_items = []

total_customers = int(input("Enter number of customers: "))

customer_count = 0

# Outer while loop - handles customers
while customer_count < total_customers:
    print(f"\nCustomer {customer_count + 1}")

    items = []
    customer_total = 0

    item_count = int(input("Enter number of grocery items: "))

    current_item = 0

    # Inner while loop - handles grocery items
    while current_item < item_count:

        item_name = input("Enter item name: ")

        price = float(input("Enter item price: "))

        # Handle invalid prices using continue
        if price <= 0:
            print("Invalid price. Try again.")
            continue

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

print("Thank you for shopping!")