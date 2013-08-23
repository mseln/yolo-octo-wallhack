google.maps.event.addListener(map, 'click', function(event) {
    createMarker(map, event.latLng, "Click: "+event.latLng);
});
