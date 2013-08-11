# Example of usage:
print(a) # Simply outputs the value of a
# What if I want to output two variables on the same line?
print(a + b) # Outputs the sum of a and b if they are compatible
print(a + ' ' + b) # Won't work if a and b aren't strings
# So what's the solution? Easy, simply convert the values to strings.
print(str(a) + ' ' + str(b))