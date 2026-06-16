import sys

# Input 3 values from command line if provided, otherwise ask the user.
def get_value(prompt, arg_index):
    if len(sys.argv) > arg_index:
        return sys.argv[arg_index]
    try:
        return input(prompt)
    except EOFError:
        return f"value{arg_index}"

a = get_value("Enter first value: ", 1)
b = get_value("Enter second value: ", 2)
c = get_value("Enter third value: ", 3)

print("Before swapping:", a, b, c)

# Swap (rotate values)
temp = a
a = b
b = c
c = temp

print("After swapping:", a, b, c)

