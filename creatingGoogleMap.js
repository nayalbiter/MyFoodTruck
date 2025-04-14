let newMap;

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

    //Create the marker object from the maps javascript API:
    const marker = new AdvancedMarkerElement({
        map: newMap,
        position: foodTruckLocation,
        title: "La chingona taqueria",
        //icon: "C:/Users/carme/MyFoodTruck/food-truck.png"
        
    });
}

initMap();

