# print is a very easy way to debug in python. It simply prints a given value to the console.
# If you're running the server it will print the output in the same window as the server is  
# running on.
# Doc: http://docs.python.org/2/library/functions.html?highlight=print#print

a=3
b=5
# Example of usage:
print a             # Simply outputs the value of a
# What if I want to output two variables on the same line?
print a + b         # Outputs the sum of a and b if they are are compatible
print a + ' ' + b   # Won't work if a and b aren't strings
# So what's the solution? Easy simply convert the values to strings.
print str(a) + ' ' + str(b)