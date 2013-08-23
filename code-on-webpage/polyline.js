function createPolyline(map, path) {
  var polyline = new google.maps.Polyline({
    path: path,
    map: map
  });
}
function displayRoads(map) {
  var points = new google.maps.MVCArray();
  points.push(new google.maps.LatLng(58.3970323, 15.5738155));
  points.push(new google.maps.LatLng(58.3976588, 15.5738047));
  createPolyline(map, points);
}
