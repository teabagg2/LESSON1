"""
FUNCTION.PY
===========
This file demonstrates how to use FUNCTIONS in Python.

A function is a reusable block of code that:
  - Performs a specific task
  - Can take inputs (called parameters/arguments)
  - Can return an output (using the `return` keyword)

We'll build a complete "Weather Outfit Picker" using functions,
which is a great real-world example.
"""


# ---------------------------------------------------------------
# 1) A simple function with NO parameters and NO return value
# ---------------------------------------------------------------
def print_heading():
    """Prints a heading for the program."""
    print("=" * 40)
    print("        WEATHER OUTFIT PICKER")
    print("=" * 40)


# ---------------------------------------------------------------
# 2) A function WITH a parameter and a return value
# ---------------------------------------------------------------
def choose_outfit(temp):
    """
    Decides the main outfit based on temperature.
    Returns a string describing the outfit.
    """
    if temp < 20:
        return "a warm jacket"
    else:
        return "a t-shirt"


# ---------------------------------------------------------------
# 3) A function that checks if an umbrella is needed
# ---------------------------------------------------------------
def check_umbrella(is_raining):
    """Returns True if an umbrella is needed."""
    if is_raining.lower() == "yes":
        return True
    else:
        return False


# ---------------------------------------------------------------
# 4) A function that decides about a windbreaker
# ---------------------------------------------------------------
def check_windbreaker(wind_speed):
    """Returns a message about whether a windbreaker is needed."""
    if wind_speed > 30:
        return "needed"
    else:
        return "not needed"


# ---------------------------------------------------------------
# 5) A function that chooses shoes based on puddles
# ---------------------------------------------------------------
def choose_shoes(has_puddles):
    """Returns the recommended type of shoes."""
    if has_puddles.lower() == "yes":
        return "boots"
    else:
        return "sneakers"


# ---------------------------------------------------------------
# 6) The MAIN function that ties everything together
# ---------------------------------------------------------------
def main():
    """Runs the entire weather outfit picker program."""
    print_heading()
    print()

    # 1) Ask for the temperature
    temp = int(input("Enter today's temperature (°C): "))

    # 2) Choose the main outfit
    outfit = choose_outfit(temp)

    # 3) Ask about rain
    is_raining = input("Is it raining? (yes/no): ")

    # 4) Add an umbrella reminder
    umbrella = check_umbrella(is_raining)

    # 5) Ask for wind speed
    wind_speed = int(input("Enter the wind speed (km/h): "))

    # 6) Decide about a windbreaker
    windbreaker = check_windbreaker(wind_speed)

    # 7) Ask about puddles
    has_puddles = input("Are there puddles on the ground? (yes/no): ")

    # 8) Choose the shoes
    shoes = choose_shoes(has_puddles)

    # 9) Completion message
    print()
    print("Weather check complete!")
    print()

    # 10) Final outfit summary
    print("=" * 40)
    print("           YOUR OUTFIT SUMMARY")
    print("=" * 40)
    print(f"Temperature    : {temp}°C")
    print(f"Main outfit    : {outfit}")
    print(f"Raining        : {is_raining}")
    print(f"Umbrella needed: {'Yes' if umbrella else 'No'}")
    print(f"Windbreaker    : {windbreaker}")
    print(f"Shoes          : {shoes}")
    print("=" * 40)
    print("Enjoy your day!")


# ---------------------------------------------------------------
# This ensures main() only runs when the file is executed directly
# ---------------------------------------------------------------
if __name__ == "__main__":
    main()
