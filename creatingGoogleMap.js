let userLocationIcon = document.createElement("img");
userLocationIcon.src = "user.png";
userLocationIcon.style.width = "40px";
userLocationIcon.style.height = "40px";

let foodTruckIcon = document.createElement("img");
foodTruckIcon.src = "food-truck.png";
foodTruckIcon.style.width = "40px";
foodTruckIcon.style.height = "40px";

let newMap;

foodTrucksList = [
    {
        title: "Bandido Mexican Grill",
        position: { lat: 47.67601522248604, lng: -122.12250027702324 },
    },
    {
        title: "Los Chilangos",
        position: { lat: 47.680114505286454, lng: -122.12521813498681 },
    }
]

//this function is used to create a map
async function initMap() {

    let userLocation = { lat: 47.67731658055798, lng: -122.12261041757242 }

    //google libraries
    const mapLibrary = await google.maps.importLibrary("maps");
    const Map = mapLibrary.Map;
    const markerLibrary = await google.maps.importLibrary("marker");
    const AdvancedMarkerElement = markerLibrary.AdvancedMarkerElement;

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
        let sameFoodTruckIcon = foodTruckIcon.cloneNode(true); // to reuse the same DOM element (food truck icon)
        new AdvancedMarkerElement({
            map: newMap,
            title: truck.title,
            position: truck.position,
            content: sameFoodTruckIcon
        })
    });

}

initMap();

