print ("ATM Cash Dispenser")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0 
total_dispensed = 0
serving = True

while serving: 
    name = input("Enter customer name")
    amount = int(input("Enter the amount to withdraw:"))
    if amount <= 0:
        print("Invalid Amount")
        continue
    print(f"Dispensing {amount} for {name}")
    remaining = amount
    idx = 1
    
while idx <= 6:
    if idx == 1: value = 100
    elif idx == 2: value = 50
    elif idx == 3: value = 20
    elif idx == 4: value = 10
    elif idx == 5: value = 5
    else: value = 1
    count = remaining // value
    if count > 0:
        print(f"{count}x{value}")
        remaining -= count * value
        if idx == 1: total_100 += count 
        elif idx == 2: total_50 += count
        elif idx == 3: total_20 += count
        elif idx == 4: total_10 += count
        elif idx == 5: total_5 += count
        else: total_1 += count
    idx += 1
    customers_served += 1
    total_dispensed += amount
    print (f"Transaction complete for {name}.")
    again = input("Would you like to serve another customer? (yes/no):"). strip().lower()
    if again.lower() != "yes":
        serving = False
print ("Daily denomination report:")
for slot in range(1, 7): # outer for -- one denomination per loop

    if slot == 1: value, total = 100, total_100

    elif slot == 2: value, total = 50, total_50

    elif slot == 3: value, total = 20, total_20

    elif slot == 4: value, total = 10, total_10

    elif slot == 5: value, total = 5, total_5

    else: value, total = 1, total_1

    if total > 0:

        print(f" {value}-unit notes dispensed : {total} ", end="")

        for note in range(total): # inner for -- one symbol per note

            print("=", end="")

            print()

print(f"\nCustomers served : {customers_served}")

print(f"Total dispensed : {total_dispensed} units")

print("ATM session closed. Goodbye!")