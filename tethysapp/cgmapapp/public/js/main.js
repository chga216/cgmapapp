var featureLayer;
var mapLayer

require([
      "esri/Map",
      "esri/layers/FeatureLayer",
	  "esri/layers/MapImageLayer",
      "esri/views/MapView",
      "dojo/domReady!"
    ], function(
      Map,
      FeatureLayer,
	  MapImageLayer,
      MapView
    ) {

      // Create the map
      var map = new Map({
        basemap: "streets"
      });

      // Create the MapView
      var view = new MapView({
        container: "viewDiv",
        map: map,
        center: [-111.1, 39.1],
        zoom: 6
      });

      var template = { // autocasts as new PopupTemplate()
        title: "Speed Limit on Road: {route}",
        content: "As of 2016, the speed limit on {route} was {speedlimit} mph.",
        fieldInfos: [{
          fieldName: "speedlimit",

		// In the future, I want to (maybe) add a part where it shows the average daily traffic flow on the road segment

		}]
      };

      // Reference the popupTemplate instance in the
      // popupTemplate property of FeatureLayer
    featureLayer = new FeatureLayer({
        url: "http://geoserver2.byu.edu/arcgis/rest/services/StorminMormons/Utah_2016_Speed_Limits/FeatureServer/0",
        outFields: ["*"],
        popupTemplate: template
      });
    mapLayer = new MapImageLayer({
        url: "http://geoserver2.byu.edu/arcgis/rest/services/StorminMormons/DEM/MapServer"
     });

	  map.layers.add(mapLayer);
      map.add(featureLayer);

	  featureLayer.visible=true;
      mapLayer.visible=true;

    });

function brc() {
    window.open('https://bikeleague.org/content/state-report-cards','_blank');
}

function toggle_roads() {

    featureLayer.visible = !featureLayer.visible;
}

function toggle_dem () {
    mapLayer.visible = !mapLayer.visible;
}

function get_grade_value () {
    // var gradeval= want to set equal to the value of the slider
    alert("123");
}
