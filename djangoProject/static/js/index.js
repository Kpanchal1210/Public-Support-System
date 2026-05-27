// ================= PAGE LOAD =================

document.addEventListener("DOMContentLoaded", function () {

    // =====================================================
    // INDIA BOUNDS
    // =====================================================

    const indiaBounds = [

        [6.5, 68.0],
        [37.5, 97.5]

    ];


    // =====================================================
    // MAP INITIALIZATION
    // =====================================================

    const map = L.map('map', {

        maxBounds: indiaBounds,

        maxBoundsViscosity: 1.0,

        minZoom: 5,

        maxZoom: 18

    });


    // FIT INDIA

    map.fitBounds(indiaBounds);


    // =====================================================
    // TILE LAYER
    // =====================================================

    L.tileLayer(

        'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',

        {

            attribution:
                '&copy; OpenStreetMap contributors',

            noWrap: true

        }

    ).addTo(map);


    // REMOVE LEAFLET PREFIX

    map.attributionControl.setPrefix(false);



    // =====================================================
    // SERVICE COLORS
    // =====================================================

    const serviceColors = {

        roads: {

            border: "#9a3412",

            fill: "#fdba74"
        },


        water: {

            border: "#0284c7",

            fill: "#7dd3fc"
        },


        electricity: {

            border: "#ca8a04",

            fill: "#fde047"
        },


        garbage: {

            border: "#15803d",

            fill: "#86efac"
        },


        traffic: {

            border: "#dc2626",

            fill: "#fca5a5"
        },


        health: {

            border: "#db2777",

            fill: "#f9a8d4"
        },


        parks: {

            border: "#0f766e",

            fill: "#5eead4"
        },

        transport: {

        border: "#2563eb",

        fill: "#93c5fd"
        }

    };



    // =====================================================
    // SERVICES DATA
    // =====================================================

    const services = {

    // ================= ROADS =================

    roads: [

        {
            lat: 22.6916,
            lng: 72.8634,
            location: "Ahmedabad, Gujarat"
        },

        {
            lat: 19.0760,
            lng: 72.8777,
            location: "Mumbai, Maharashtra"
        },

        {
            lat: 28.7041,
            lng: 77.1025,
            location: "Delhi"
        },

        {
            lat: 23.2599,
            lng: 77.4126,
            location: "Indore, Madhya Pradesh"
        },

        {
            lat: 26.9124,
            lng: 75.7873,
            location: "Jaipur, Rajasthan"
        },

        {
            lat: 13.0827,
            lng: 80.2707,
            location: "Chennai, Tamil Nadu"
        },

        {
            lat: 15.4909,
            lng: 73.8278,
            location: "Goa"
        },

        {
            lat: 17.3850,
            lng: 78.4867,
            location: "Hyderabad, Telangana"
        },

        {
            lat: 22.5726,
            lng: 88.3639,
            location: "Kolkata, West Bengal"
        }

    ],


    // ================= WATER =================

    water: [

        {
            lat: 28.6139,
            lng: 77.2090,
            location: "Delhi"
        },

        {
            lat: 23.0225,
            lng: 72.5714,
            location: "Ahmedabad, Gujarat"
        },

        {
            lat: 21.1702,
            lng: 72.8311,
            location: "Surat, Gujarat"
        },

        {
            lat: 26.8467,
            lng: 80.9462,
            location: "Lucknow, Uttar Pradesh"
        },

        {
            lat: 19.0760,
            lng: 72.8777,
            location: "Mumbai, Maharashtra"
        },

        {
            lat: 15.2993,
            lng: 74.1240,
            location: "Belgaum, Karnataka"
        },

        {
            lat: 10.8505,
            lng: 76.2711,
            location: "Kochi, Kerala"
        },

        {
            lat: 30.7333,
            lng: 76.7794,
            location: "Chandigarh"
        },

        {
            lat: 9.9312,
            lng: 76.2673,
            location: "Thiruvananthapuram, Kerala"
        }

    ],


    // ================= ELECTRICITY =================

    electricity: [

        {
            lat: 13.0827,
            lng: 80.2707,
            location: "Chennai, Tamil Nadu"
        },

        {
            lat: 18.5204,
            lng: 73.8567,
            location: "Pune, Maharashtra"
        },

        {
            lat: 22.5726,
            lng: 88.3639,
            location: "Kolkata, West Bengal"
        },

        {
            lat: 17.3850,
            lng: 78.4867,
            location: "Hyderabad, Telangana"
        },

        {
            lat: 28.7041,
            lng: 77.1025,
            location: "Delhi"
        },

        {
            lat: 23.1815,
            lng: 79.9864,
            location: "Jabalpur, Madhya Pradesh"
        },

        {
            lat: 12.9716,
            lng: 77.5946,
            location: "Bangalore, Karnataka"
        },

        {
            lat: 31.1471,
            lng: 77.1788,
            location: "Shimla, Himachal Pradesh"
        },

        {
            lat: 26.2389,
            lng: 73.0243,
            location: "Jodhpur, Rajasthan"
        }

    ],


    // ================= GARBAGE =================

    garbage: [

        {
            lat: 26.9124,
            lng: 75.7873,
            location: "Jaipur, Rajasthan"
        },

        {
            lat: 17.3850,
            lng: 78.4867,
            location: "Hyderabad, Telangana"
        },

        {
            lat: 15.4909,
            lng: 73.8278,
            location: "Goa"
        },

        {
            lat: 11.0168,
            lng: 76.9558,
            location: "Coimbatore, Tamil Nadu"
        },

        {
            lat: 22.6916,
            lng: 72.8634,
            location: "Ahmedabad, Gujarat"
        },

        {
            lat: 28.7041,
            lng: 77.1025,
            location: "Delhi"
        },

        {
            lat: 19.0760,
            lng: 72.8777,
            location: "Mumbai, Maharashtra"
        },

        {
            lat: 23.1815,
            lng: 79.9864,
            location: "Jabalpur, Madhya Pradesh"
        },

        {
            lat: 25.4358,
            lng: 88.3963,
            location: "Patna, Bihar"
        }

    ],


    // ================= TRAFFIC =================

    traffic: [

        {
            lat: 12.9716,
            lng: 77.5946,
            location: "Bangalore, Karnataka"
        },

        {
            lat: 19.2183,
            lng: 72.9781,
            location: "Mumbai, Maharashtra"
        },

        {
            lat: 25.5941,
            lng: 85.1376,
            location: "Patna, Bihar"
        },

        {
            lat: 28.7041,
            lng: 77.1025,
            location: "Delhi"
        },

        {
            lat: 22.6916,
            lng: 72.8634,
            location: "Ahmedabad, Gujarat"
        },

        {
            lat: 13.0827,
            lng: 80.2707,
            location: "Chennai, Tamil Nadu"
        },

        {
            lat: 17.3850,
            lng: 78.4867,
            location: "Hyderabad, Telangana"
        },

        {
            lat: 22.5726,
            lng: 88.3639,
            location: "Kolkata, West Bengal"
        }

    ],


    // ================= HEALTH =================

    health: [

        {
            lat: 22.3039,
            lng: 70.8022,
            location: "Vadodara, Gujarat"
        },

        {
            lat: 30.7333,
            lng: 76.7794,
            location: "Chandigarh"
        },

        {
            lat: 9.9312,
            lng: 76.2673,
            location: "Thiruvananthapuram, Kerala"
        },

        {
            lat: 18.5204,
            lng: 73.8567,
            location: "Pune, Maharashtra"
        },

        {
            lat: 28.7041,
            lng: 77.1025,
            location: "Delhi"
        },

        {
            lat: 23.1815,
            lng: 79.9864,
            location: "Jabalpur, Madhya Pradesh"
        },

        {
            lat: 21.1702,
            lng: 72.8311,
            location: "Surat, Gujarat"
        },

        {
            lat: 26.1445,
            lng: 91.7362,
            location: "Guwahati, Assam"
        },

        {
            lat: 22.5726,
            lng: 88.3639,
            location: "Kolkata, West Bengal"
        }

    ],


    // ================= PARKS =================

    parks: [

        {
            lat: 15.2993,
            lng: 74.1240,
            location: "Belgaum, Karnataka"
        },

        {
            lat: 28.5355,
            lng: 77.3910,
            location: "Delhi NCR"
        },

        {
            lat: 10.8505,
            lng: 76.2711,
            location: "Kochi, Kerala"
        },

        {
            lat: 19.0760,
            lng: 72.8777,
            location: "Mumbai, Maharashtra"
        },

        {
            lat: 13.0827,
            lng: 80.2707,
            location: "Chennai, Tamil Nadu"
        },

        {
            lat: 17.3850,
            lng: 78.4867,
            location: "Hyderabad, Telangana"
        },

        {
            lat: 26.9124,
            lng: 75.7873,
            location: "Jaipur, Rajasthan"
        },

        {
            lat: 30.7333,
            lng: 76.7794,
            location: "Chandigarh"
        },

        {
            lat: 22.5726,
            lng: 88.3639,
            location: "Kolkata, West Bengal"
        }

    ],


    // ================= TRANSPORT =================

    transport: [

        {
            lat: 28.7041,
            lng: 77.1025,
            location: "Delhi"
        },

        {
            lat: 18.9388,
            lng: 72.8354,
            location: "Mumbai, Maharashtra"
        },

        {
            lat: 13.0674,
            lng: 80.2376,
            location: "Chennai, Tamil Nadu"
        },

        {
            lat: 22.6916,
            lng: 72.8634,
            location: "Ahmedabad, Gujarat"
        },

        {
            lat: 17.3850,
            lng: 78.4867,
            location: "Hyderabad, Telangana"
        },

        {
            lat: 12.9716,
            lng: 77.5946,
            location: "Bangalore, Karnataka"
        },

        {
            lat: 23.1815,
            lng: 79.9864,
            location: "Jabalpur, Madhya Pradesh"
        },

        {
            lat: 26.1445,
            lng: 91.7362,
            location: "Guwahati, Assam"
        },

        {
            lat: 31.7683,
            lng: 75.8430,
            location: "Amritsar, Punjab"
        }

    ]

};



    // =====================================================
    // CURRENT LAYERS
    // =====================================================

    let currentLayers = [];



    // =====================================================
    // SHOW SERVICE FUNCTION
    // =====================================================

    function showService(serviceName){

        // REMOVE OLD CIRCLES

        currentLayers.forEach(layer => {

            map.removeLayer(layer);

        });


        currentLayers = [];


        // GET SERVICE DATA

        const places =
            services[serviceName];


        // GET COLORS

        const colors =
            serviceColors[serviceName];


        // CREATE CIRCLES

        places.forEach(place => {

            const circle = L.circle(

                [place.lat, place.lng],

                {

                    color: colors.border,

                    fillColor: colors.fill,

                    fillOpacity: 0.35,

                    radius: 25000,

                    weight: 2

                }

            )

            .addTo(map);

            currentLayers.push(circle);

        });

    }



    // =====================================================
    // BUTTON EVENTS
    // =====================================================

    const buttons =
        document.querySelectorAll(".service-btn");


    buttons.forEach(button => {

        button.addEventListener("click", () => {

            // REMOVE ACTIVE

            buttons.forEach(btn => {

                btn.classList.remove("active");

            });


            // ADD ACTIVE

            button.classList.add("active");


            // GET SERVICE NAME

            const service =
                button.dataset.service;


            // SHOW SERVICE

            showService(service);

        });

    });



    // =====================================================
    // DEFAULT SERVICE
    // =====================================================

    showService("roads");



    // =====================================================
    // REPORT CARD TILT EFFECT
    // =====================================================

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