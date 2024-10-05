def infinite_recursion(n):
    if n < 10:  # Base case to stop recursion
        return infinite_recursion(n + 1)
    return n  # Return a value when base case is reached

result = infinite_recursion(0)
print(result)
