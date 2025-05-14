let userLocationIcon = document.createElement("img");
userLocationIcon.src = "static/images/user.png";
userLocationIcon.style.width = "40px";
userLocationIcon.style.height = "40px";

let foodTruckIcon = document.createElement("img");
foodTruckIcon.src = "static/images/food-truck.png";
foodTruckIcon.style.width = "40px";
foodTruckIcon.style.height = "40px";

let mapForFT;
let geocoder;

// Create a map
async function initMap() {

    let userLocation = { lat: 47.67731658055798, lng: -122.12261041757242 };

    const mapLibrary = await google.maps.importLibrary("maps");
    const Map = mapLibrary.Map;
    const markerLibrary = await google.maps.importLibrary("marker");
    const AdvancedMarkerElement = markerLibrary.AdvancedMarkerElement;

    await google.maps.importLibrary("geocoding");
    geocoder = new google.maps.Geocoder();

    mapForFT = new Map(document.getElementById("map"), {
        zoom: 12,
        center: userLocation,
        mapId: "679343f29f0f9fcf"
    });

    userMarker = new AdvancedMarkerElement({
        map: mapForFT,
        position: userLocation,
        title: "My location",
        content: userLocationIcon
    });
}

// Geocoding function
async function geoCodingAddress(foodTruckName, foodTruckAddress) {

    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    geocoder.geocode({
        address: foodTruckAddress,
        region: "US",
        componentRestrictions: {
            country: "US",
            administrativeArea: "WA"
        }
    }, function (results, status) {
        if (status === 'OK') {
            let sameFoodTruckIcon = foodTruckIcon.cloneNode(true);
            new AdvancedMarkerElement({
                map: mapForFT,
                title: foodTruckName,
                position: results[0].geometry.location,
                content: sameFoodTruckIcon
            });
        } else {
            alert('something is wrong with the geocode function: ' + status);
        }
    });
}

//get food trucks from database
function fetchFoodTrucks() {
    fetch('/fetchFoodTrucks')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(foodTrucksList => {
            //console.log("hahaha si funciona");
            foodTrucksList.forEach(truck => {
                geoCodingAddress(truck.food_truck_name, truck.full_address);
                console.log(truck.food_truck_name);
                console.log(truck.full_address);
            });
        })
        .catch(error => {
            console.error("Error fetching the food trucks:", error);
        });
}

document.addEventListener("DOMContentLoaded", function () {

    let registerButton = document.getElementById("registerButton");
    if (registerButton) {
        registerButton.addEventListener("click", function () {
            window.location.href = "/registerFoodCompany";
        });
    }

    let logInForCompany = document.getElementById("logInButton");
    if (logInForCompany) {
        logInForCompany.addEventListener("click", function () {
            window.location.href = "/logInPage";
        });
    }

    initMap().then(() => {
        fetchFoodTrucks();
    });

});
