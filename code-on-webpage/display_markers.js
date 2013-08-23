function displayMarkers(map) {
    {% for coord in COORDS %}
        createMarker(map, new google.maps.LatLng({{coord.lat}},
                                                 {{coord.lng}}),
                                                 ""+{{coord.id}});
    {% endfor %}
}
