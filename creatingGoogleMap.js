let newMap;

let foodTruckIcon = document.createElement("img"); //icon to the used for the marker
foodTruckIcon.src = "food-truck.png";
foodTruckIcon.style.width = "40px"; 
foodTruckIcon.style.height = "40px";

//this function is used to create a map
async function initMap() {
    let foodTruckLocation = { lat: 47.608893691960496, lng: -122.14349921135684 };
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    //Create map object from the maps javascript API:
    newMap = new Map(document.getElementById("map"), {
        zoom: 17,
        center: foodTruckLocation,
        mapId: "la_chingona_taqueria",
    });

    //Create the marker object for the food truck:
    const marker = new AdvancedMarkerElement({
        map: newMap,
        position: foodTruckLocation,
        title: "La chingona taqueria",
        content: foodTruckIcon
        
    });
}

initMap();

