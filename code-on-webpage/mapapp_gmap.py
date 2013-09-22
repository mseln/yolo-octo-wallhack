def mapapp(request):
    c = Context({'GMAPS_API_KEY': '+++YOUR_GMAPS_API_KEY+++'})
    return render_to_response('mapvis/mapapp.html', c)
