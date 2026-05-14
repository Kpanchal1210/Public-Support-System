// ================= MAP + PARALLAX =================

document.addEventListener("DOMContentLoaded", function () {

    // ================= INDIA MAP =================

    const indiaBounds = [
        [6.5, 68.0],
        [37.5, 97.5]
    ];

    // MAP INIT

    const map = L.map('map', {
        maxBounds: indiaBounds,
        maxBoundsViscosity: 1.0,
        minZoom: 5,
        maxZoom: 18
    });

    // FIT INDIA

    map.fitBounds(indiaBounds);

    // TILE LAYER

    L.tileLayer(
        'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
        {
            attribution: '&copy; OpenStreetMap contributors',
            noWrap: true
        }
    ).addTo(map);

    map.attributionControl.setPrefix(false);

    let selectedMarker;

    // MAP CLICK

    map.on('click', function(e) {

        const lat = e.latlng.lat;
        const lng = e.latlng.lng;

        // REMOVE OLD MARKER

        if (selectedMarker) {
            map.removeLayer(selectedMarker);
        }

        // ADD NEW MARKER

        selectedMarker = L.marker([lat, lng]).addTo(map);

        // SAVE COORDINATES

        const latInput =
            document.getElementById("lat");

        const lngInput =
            document.getElementById("lng");

        if (latInput && lngInput) {

            latInput.value = lat;
            lngInput.value = lng;
        }

    });

    // ================= HERO PARALLAX =================

    const hero =
        document.querySelector(".hero");

    const heroMap =
        document.querySelector(".hero-map");

    const heroContent =
        document.querySelector(".hero-content");

    const shapes =
        document.querySelectorAll(".floating-shape");

    // SAFETY CHECK

    if (hero && heroMap && heroContent) {

        hero.addEventListener("mousemove", (e) => {

            const rect =
                hero.getBoundingClientRect();

            const x =
                e.clientX - rect.left;

            const y =
                e.clientY - rect.top;

            const moveX =
                (rect.width / 2 - x) / 35;

            const moveY =
                (rect.height / 2 - y) / 35;

            // HERO MAP

            heroMap.style.transform = `
                translate(${moveX}px, ${moveY}px)
                rotateY(${-moveX / 2}deg)
                rotateX(${moveY / 2}deg)
            `;

            // HERO TEXT

            heroContent.style.transform = `
                translate(${moveX / 2}px, ${moveY / 2}px)
            `;

            // FLOATING SHAPES

            shapes.forEach((shape, index) => {

                const speed =
                    (index + 1) * 12;

                shape.style.transform = `
                    translate(
                        ${moveX * speed / 20}px,
                        ${moveY * speed / 20}px
                    )
                `;
            });

        });

        // RESET EFFECT

        hero.addEventListener("mouseleave", () => {

            heroMap.style.transform =
                `translate(0,0)
                 rotateX(0)
                 rotateY(0)`;

            heroContent.style.transform =
                `translate(0,0)`;

            shapes.forEach(shape => {

                shape.style.transform =
                    `translate(0,0)`;
            });

        });

    }

    // ================= REPORT CARD TILT =================

    const cards =
        document.querySelectorAll(".report-card");

    cards.forEach(card => {

        card.addEventListener("mousemove", (e) => {

            const rect =
                card.getBoundingClientRect();

            const x =
                e.clientX - rect.left;

            const y =
                e.clientY - rect.top;

            const rotateY =
                (x - rect.width / 2) / 18;

            const rotateX =
                -(y - rect.height / 2) / 18;

            card.style.transform = `
                rotateX(${rotateX}deg)
                rotateY(${rotateY}deg)
                translateY(-6px)
            `;
        });

        // RESET

        card.addEventListener("mouseleave", () => {

            card.style.transform =
                `rotateX(0)
                 rotateY(0)
                 translateY(0)`;
        });

    });

});