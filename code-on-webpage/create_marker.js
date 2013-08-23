function createMarker(map, latlng, title) {
    var marker = new google.maps.Marker({
        map: map,
        position: latlng,
        title: title
    });
}
