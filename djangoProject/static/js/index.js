// map.js

document.addEventListener("DOMContentLoaded", function () {

    // 🇮🇳 India bounds
    const indiaBounds = [
        [6.5, 68.0],   // Southwest corner
        [37.5, 97.5]   // Northeast corner
    ];

    // Initialize map
    var map = L.map('map', {
        maxBounds: indiaBounds,
        maxBoundsViscosity: 1.0, // hard bounds
        minZoom: 5,
        maxZoom: 18
    });

    // Fit map to India
    map.fitBounds(indiaBounds);

    // Tile layer
    L.tileLayer(
        'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
        {
            attribution: '&copy; OpenStreetMap contributors',
            noWrap: true
        }
    ).addTo(map);

    map.attributionControl.setPrefix(false);

    var selectedMarker;

    // Click to select location
    map.on('click', function(e) {

        var lat = e.latlng.lat;
        var lng = e.latlng.lng;

        // Remove previous marker
        if (selectedMarker) {
            map.removeLayer(selectedMarker);
        }

        // Add new marker
        selectedMarker = L.marker([lat, lng]).addTo(map);

        // Save coordinates
        var latInput = document.getElementById("lat");
        var lngInput = document.getElementById("lng");

        if (latInput && lngInput) {
            latInput.value = lat;
            lngInput.value = lng;
        }

    });

});