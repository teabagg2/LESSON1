# Art Supplies Billing Tool

# Step 1: Greeting Function
def greet_customer():
    print("===================================")
    print("Welcome to the Art Supplies Store!")
    print("We have everything you need for your creativity.")
    print("===================================\n")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative whole number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


def calculate_total(price, items):
    return price * items


def calculate_change(paid, total):
    return paid - total


def thank_you_message(items):
    if items >= 10:
        return "Thank you for your large order! We appreciate your support."
    return "Thank you for shopping with us! Enjoy your art supplies."


def print_bill(price, items, total_cost, paid, change_due):
    print("\n========== ART SUPPLIES BILL ==========")
    print(f"Price per Item : ${price:.2f}")
    print(f"Items Bought   : {items}")
    print(f"Total Cost     : ${total_cost:.2f}")
    print(f"Amount Paid    : ${paid:.2f}")
    if change_due >= 0:
        print(f"Change Due     : ${change_due:.2f}")
    else:
        print(f"Amount Due     : ${abs(change_due):.2f}")
    print("---------------------------------------")
    print(thank_you_message(items))
    print("=======================================")


greet_customer()

price = get_positive_float("Enter the price per art item: $")
items = get_non_negative_int("Enter the number of items bought: ")

total_cost = round(calculate_total(price, items), 2)
paid = get_positive_float("Enter the amount paid: $")
change_due = round(calculate_change(paid, total_cost), 2)

print_bill(price, items, total_cost, paid, change_due)