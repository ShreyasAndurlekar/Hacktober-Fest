# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to square a number
def square(num):
    return num * num

# Input from the user 
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))

# Calculating the product and square
result_multiply = multiply(a, b)
result_square = square(a)

print(f"The product of {a} and {b} is {result_multiply}")
print(f"The square of {a} is {result_square}")
 
