valid = False

while not valid:
    try:
        # Ask for shopping bill details
        bill_amount, discount_percent, people = input(
            "Enter bill amount, discount percentage, and number of people separated by commas: "
        ).split(",")

        # Convert the values
        bill_amount = float(bill_amount)
        discount_percent = float(discount_percent)
        people = int(people)

        # Check for invalid values
        if bill_amount <= 0 or discount_percent < 0 or people < 0:
            raise ValueError("Invalid values entered.")

        # Calculate discount
        discount_amount = bill_amount * (discount_percent / 100)
        final_amount = bill_amount - discount_amount

        # Calculate amount per person
        amount_each = final_amount / people

    except ValueError:
        print("Error: Please enter valid numbers and make sure the values are not negative.")

    except ZeroDivisionError:
        print("Error: The number of people cannot be 0.")

    else:
        print()
        print("================================")
        print("     SHOPPING DISCOUNT SUMMARY")
        print("================================")
        print("Original Bill: $", bill_amount)
        print("Discount: ", discount_percent, "%")
        print("Discount Amount: $", discount_amount)
        print("Final Bill: $", final_amount)
        print("Number of People:", people)
        print("Amount Each Person Pays: $", amount_each)
        print("================================")

        valid = True

    finally:
        print("Attempt completed.")
        print()
