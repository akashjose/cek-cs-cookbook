def add(x, y):
    """Function to calculate the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Function to calculate the difference of two numbers."""
    return x - y

def multiply(x, y):
    """Function to calculate the product of two numbers."""
    return x * y

def divide(x, y):
    """Function to calculate the division of two numbers."""
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# Example usage:
num1 = 10
num2 = 5

print("Sum:", add(num1, num2))
print("Difference:", subtract(num1, num2))
print("Product:", multiply(num1, num2))
print("Division:", divide(num1, num2))
