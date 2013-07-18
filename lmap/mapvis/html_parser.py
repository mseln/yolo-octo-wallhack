def get_float(request, name) :
	value = request.POST.get(name)
	try :
		float(value)
		return float(value)
	except TypeError:
		return None
	except ValueError:
		return None
