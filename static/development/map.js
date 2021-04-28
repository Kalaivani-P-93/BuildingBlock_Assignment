$( document ).ready(function() {
  //Setting Default Location
  var map = L.map('map', {
        center: [11.059821,  78.387451], 
        zoom: 4, 
        scrollWheelZoom: false,
        tap: false
    });

  /* Control panel to display map layers */
  var controlLayers = L.control.layers( null, null, {
    position: "topright",
    collapsed: false
  }).addTo(map);

  // display Carto basemap tiles with light features and labels
  var light = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: ''
  }).addTo(map); 
  controlLayers.addBaseLayer(light, 'Carto Light basemap');

  /* Stamen colored terrain basemap tiles with labels */
  var terrain = L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png', {
    attribution: ''
  });
  controlLayers.addBaseLayer(terrain, 'Stamen Terrain basemap');

$.ajax(
    {
        url : '/address_Data/',
        type : 'POST',
        timeout : 10000,
        async : false,
        data : {},
    }).done(
        function(json_data){
            var data = JSON.parse(json_data);
            for (var i in data) {
                var row = data[i];
                var marker = L.marker([row.latitude, row.longitude], {
                  opacity: 1,
                  icon: L.icon({
                    iconUrl: '/static/ui/css/images/marker.png',
                    iconSize: [40, 60]
                  })
                }).bindPopup(row.Title);
                marker.addTo(map);
              }
        });
            
})