# Of course should you write programs that don't crash but if they crash, you want them to
# crash in an expected way and give relevant information why they crashed. Even better would
# be if you could make so the program doesn't crash eventhough for instance a function get 
# the wrong datatype as parameter or you're trying to read a out of range for an array.

# A way of doing this is to add exceptions. 
# Read more about exceptions here: http://docs.python.org/2/library/exceptions.html
# You try something. If it succeds, good!, else you will have to handle the failure.

# below are some simple examples.

def bad_to_float(x):
	return float(x)

def good_to_float(x):
	try:
		return float(x)
	except (TypeError, ValueError):
		print 'Input is not convertable to float!'
		return None
		# Or do whatever you want if the user tries any illegal input.

a = bad_to_float('10')      # Risky!
# b = bad_to_float('Hello') # Will crash!
c = good_to_float('10')     # Safe
d = good_to_float('Hello')  # Won't crash

a = [1, 'a', 12.3]
def bad_get_by_index(x):
	return a[x]

def good_get_by_index(x):
	try:
		return a[x]
	except (IndexError):
		print 'Input is not in range!'
		return None
		# Or do whatever you want if the user tries any illegal input.

bad_get_by_index(0)      # Risky!
# bad_get_by_index(3)    # Will crash!
good_get_by_index(0)     # Safe
good_get_by_index(3)     # Won't crash