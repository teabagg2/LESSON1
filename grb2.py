
#just the ending

print("\nFinal Price Category Report:")

low_items = 0
medium_items = 0
high_items = 0
customers_served = 0
total_sales = 0.0

categories = ["Low Price Items", "Medium Price Items", "High Price Items"]
amounts = [low_items, medium_items, high_items]

for slot in range(3):   # outer for loop - categories

    print(f"{categories[slot]}: {amounts[slot]}")

    for item in range(amounts[slot]):   # inner for loop - symbols

        print("*", end="")

    print()


print("\nDaily Grocery Summary:")
print(f"Customers served: {customers_served}")
print(f"Total sales: ${total_sales:.2f}")

print("Grocery billing session closed. Goodbye!")