let registerButton = document.getElementById("registerButton")
registerButton.addEventListener("click", function () { window.location.href = "/registerFoodCompany"; });

let userLocationIcon = document.createElement("img");
userLocationIcon.src = "static/images/user.png";
userLocationIcon.style.width = "40px";
userLocationIcon.style.height = "40px";

let foodTruckIcon = document.createElement("img");
foodTruckIcon.src = "static/images/food-truck.png";
foodTruckIcon.style.width = "40px";
foodTruckIcon.style.height = "40px";

let newMap;
let geocoder;

foodTrucksList = [
    {
        title: "Bandido Mexican Grill",
        position: { lat: 47.67601522248604, lng: -122.12250027702324 },
    },
    {
        title: "Los Chilangos",
        position: { lat: 47.680114505286454, lng: -122.12521813498681 },
    }
] //to do: connect to database to bring food trucks addresses and names

//create a map
async function initMap() {

    let userLocation = { lat: 47.67731658055798, lng: -122.12261041757242 } //to do: use the geolocation api here

    //google libraries
    const mapLibrary = await google.maps.importLibrary("maps");
    const Map = mapLibrary.Map;
    const markerLibrary = await google.maps.importLibrary("marker");
    const AdvancedMarkerElement = markerLibrary.AdvancedMarkerElement;

    //code for geocoding------! 
    const geocodingLibrary = await google.maps.importLibrary("geocoding");
    geocoder = new google.maps.Geocoder();

    //Create map object:
    newMap = new Map(document.getElementById("map"), {
        zoom: 15,
        center: userLocation,
        mapId: "679343f29f0f9fcf" //
    });

    //marker object for the user location:
    let userMarker = new AdvancedMarkerElement({
        map: newMap,
        position: userLocation,
        title: "My location",
        content: userLocationIcon
    });

    //marker object for the food trucks:
    foodTrucksList.forEach(truck => {
        let sameFoodTruckIcon = foodTruckIcon.cloneNode(true);
        new AdvancedMarkerElement({
            map: newMap,
            title: truck.title,
            position: truck.position,
            content: sameFoodTruckIcon
        })
    });

}

//code for geocoding---------------!
let foodTruckName = "La Chingona Taqueria Seattle";
let foodTruckAddress = "2940 SW Avalon Way, Seattle, WA 98126";

//geocoding function hard coded right now
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

                map: newMap,
                title: foodTruckName,
                position: results[0].geometry.location,
                content: sameFoodTruckIcon
            });
            console.log(results[0]);
            console.log(results);

        } else {
            alert('something is wrong with the geocode function: ' + status);
        }
    });
}


initMap().then(() => {
    geoCodingAddress(foodTruckName, foodTruckAddress);
});


