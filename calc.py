def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

try:
    print("Calculator")
    print("1.  Add")
    print("2.  Subtract")
    print("3.  Multiply")
    print("4.  Divide")
    
    operation = input("Choose an operation (1-4): ")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if operation == "1":
        result = add(num1, num2)
    elif operation == "2":
        result = subtract(num1, num2)
    elif operation == "3":
        result = multiply(num1, num2)
    elif operation == "4":
        result = divide(num1, num2)
        
    else:
        print("Invalid operation")
        result = 0
    
    print("result", result)
    
except ValueError:
    print("Invalid input. please enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")
    
        
        
    
    
    
