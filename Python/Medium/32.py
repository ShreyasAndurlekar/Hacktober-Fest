import sys

# Set a recursion limit (you might want to keep this high for practical uses)
sys.setrecursionlimit(1000)

def recursive_function(n):
    if n > 0:  # Base case to stop recursion
        return recursive_function(n - 1)
    return "Recursion has finished!"  # Message when recursion ends

# Start the recursion with a positive integer
result = recursive_function(10)
print(result)
