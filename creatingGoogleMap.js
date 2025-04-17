let userLocationIcon = document.createElement("img");
userLocationIcon.src = "user.png";
userLocationIcon.style.width = "40px";
userLocationIcon.style.height = "40px";

let foodTruckIcon1 = document.createElement("img");
foodTruckIcon1.src = "food-truck.png";
foodTruckIcon1.style.width = "40px";
foodTruckIcon1.style.height = "40px";

let foodTruckIcon2 = document.createElement("img");
foodTruckIcon2.src = "food-truck.png";
foodTruckIcon2.style.width = "40px";
foodTruckIcon2.style.height = "40px";

let newMap;

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
        mapId: "user location",
    });

    //marker object for the user location:
    let userMarker = new AdvancedMarkerElement({
        map: newMap,
        position: userLocation,
        title: "My location",
        content: userLocationIcon
    });

    //marker object for the food trucks:
    foodTruck1 = { lat: 47.67601522248604, lng: -122.12250027702324 }
    let foodTruckMarker1 = new AdvancedMarkerElement({
        map: newMap,
        position: foodTruck1,
        title: "Bandido Mexican Grill",
        content: foodTruckIcon1
    });

    //marker object for the food trucks:
    foodTruck2 = { lat: 47.680114505286454, lng: -122.12521813498681 }
    let foodTruckMarker2 = new AdvancedMarkerElement({
        map: newMap,
        position: foodTruck2,
        title: "Los Chilangos",
        content: foodTruckIcon2
    });
}

initMap();

