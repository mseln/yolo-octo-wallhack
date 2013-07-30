# To make sure the POST parser work, you need to make sure that
# you have these things in your program to pass the CSRF check
# 
# 1) in view.py 
#    c = {}
#    c.update(csrf(request))
# 
# 2) in settings.py at MIDDLEWARE_CLASSES
#    'django.middleware.csrf.CsrfViewMiddleware',
# 
# 3) in mapapp.html after each <form action="" method="post"> add
#    {% csrf_token %}
#    so it looks like this
#    <form action="" method="post"> {% csrf_token %}
#        ...
#    </form>

def get_float(request, name) :
	value = request.POST.get(name)
	try :
		float(value)
		return float(value)
	except (TypeError, ValueError):
		return None

def get_str(request, name) :
	return request.POST.get(name)

class POST_parser :
	def __init__(self, request) :
		# You can here chose which variables you wan't to 
		# get from POST and what to call them.
		self.lat1 = get_float(request, 'lat1')
		self.lng1 = get_float(request, 'lng1')
		self.lat2 = get_float(request, 'lat2')
		self.lng2 = get_float(request, 'lng2')
	
		self.czoom = get_float(request, 'czoom')
		self.clat = get_float(request, 'clat')
		self.clng = get_float(request, 'clng')
