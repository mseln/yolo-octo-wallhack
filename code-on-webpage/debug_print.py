# Example usage:
print(a) # Prints the value of the variable a

# What if I want to print two variables on the same line?
print(a + b) # Prints the sum of a and b, if they are compatible
print(a + ' ' + b) # Only works if a and b are strings
# So what's the solution? Easy, simply convert the values to strings.
print(str(a) + ' ' + str(b))
