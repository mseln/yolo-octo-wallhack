# As you may already have seen, the django error view contains a lot of info. It contains 
# all variables and their values. You can get this info by just adding assert(False) anywhere
# in your code. It will cause the program to "crash" and show all info about the current view.

from django.http import HttpResponse
import datetime

def debug(request):
	now = datetime.datetime.now()
	html = "<html><body>Hello world! It is now %s. </body></html>" %now
	assert(False)
	return HttpResponse (html)