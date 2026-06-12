# ASCII Value Checker

print("ASCII Value Checker")
print("=" * 40)

# Get input
char = input("Enter a single character: ")

# Validate input
if type(char) is str and len(char) == 1:

    # Get ASCII value
    ascii_val = ord(char)

    # Display results
    print(f"\nCharacter: '{char}'")
    print(f"ASCII Value: {ascii_val}")

    # Identify character type
    print("\nCharacter Type: ", end="")

    if ascii_val >= 65 and ascii_val <= 90:
        print("Uppercase Letter")

    elif ascii_val >= 97 and ascii_val <= 122:
        print("Lowercase Letter")

    elif ascii_val >= 48 and ascii_val <= 57:
        print("Digit")

    elif ascii_val == 32:
        print("Space")

    else:
        print("Special Character")

else:
    print("\nError: Please enter exactly ONE character!")





    ASCII Value Checker
========================================
Enter a single character: A

Character: 'A'
ASCII Value: 65

Character Type: Uppercase Letter

ASCII Value Checker
========================================
Enter a single character: 5

Character: '5'
ASCII Value: 53

Character Type: Digit

ASCII Value Checker
========================================
Enter a single character: @

Character: '@'
ASCII Value: 64

Character Type: Special Character

ASCII Value Checker
========================================
Enter a single character: ABC

Error: Please enter exactly ONE character!
