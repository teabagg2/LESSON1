# Bill & Seating Helper

# Step 1: Create the Bill Function
def total_bill(bill_amount, tip_perc):
    tip = bill_amount * (tip_perc / 100)
    total = bill_amount + tip
    return total

# Step 2: Call the Function with Positional Arguments
bill = total_bill(150, 20)
print("Total Bill: $", bill)

# Step 3: Create the Recursive Seating Function
def seating_arrangements(guests):
    """
    Calculates the number of possible seating arrangements
    for a given number of guests using recursion.
    """

    # Step 4: Base Case
    if guests == 0 or guests == 1:
        return 1

    # Step 5: Recursive Case
    return guests * seating_arrangements(guests - 1)

# Step 6: Access the Docstring
print("\nFunction Docstring:")
print(seating_arrangements.__doc__)

# Step 7: Display Seating Results
print("Seating Arrangements:")
print("1 guest :", seating_arrangements(1))
print("2 guests:", seating_arrangements(2))
print("3 guests:", seating_arrangements(3))
print("5 guests:", seating_arrangements(5))

# Step 8: Run and Explore
# Change the values above to test different bills, tip percentages,
# and guest counts.