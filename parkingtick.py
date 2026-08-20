def calculate_change(paid, price):
    change = paid - price
    return change


# Ticket price
ticket_price = 30

print("================================")
print("   PARKING TICKET PAYMENT HELPER")
print("================================")
print("Ticket Price: $30")
print("Accepted coins: $1, $5, $10, $25")
print()

# Starting counters
total_inserted = 0
coins_inserted = 0

# Collect coins
while True:
    coin = int(input("Insert a coin ($1, $5, $10, or $25): "))

    # Skip invalid coins
    if coin not in (1, 5, 10, 25):
        print("Invalid coin. Please insert $1, $5, $10, or $25.")
        continue

    # Add valid coin
    total_inserted += coin
    coins_inserted += 1

    print("Total inserted: $", total_inserted)

    # Stop when enough money is inserted
    if total_inserted >= ticket_price:
        print("Enough money has been inserted.")
        break

# Calculate change
change_due = calculate_change(total_inserted, ticket_price)

if change_due == 0:
    pass
else:
    print("Change due: $", change_due)

# Final summary
print()
print("================================")
print("   PARKING TICKET PAYMENT SUMMARY")
print("================================")
print("Ticket Price: $", ticket_price)
print("Coins Inserted:", coins_inserted)
print("Total Paid: $", total_inserted)
print("Change Given: $", change_due)
print("================================")
print("Thank you for your payment!")
