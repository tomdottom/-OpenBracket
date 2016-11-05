function init_map() {
    var wilmington_de_loc = [39.74, -75.545]
    var mymap = L.map('mapid').setView(wilmington_de_loc, 12);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
            '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        id: 'mapbox.streets'
    }).addTo(mymap);

    return mymap
}

function age(key, data) {
    return [ data.latitude, data.longditude, data[key] ]
}

function add_head_map_data_points(map, groups, data) {
    $.each(groups, function(name, layerGroup) {
        layerGroup.addLayer(
            L.heatLayer(data.map(layerGroup._extractor), {radius: 25}))
    })
}

function init_map_layers(map) {

    var description_function_pairs = {
        "Under 29": "age0to29",
        "30 to 54": "age30to54",
        "Above 55": "age55plus",
    }
    var overlayMaps = {};

    _.each(description_function_pairs, function (value, key) {
        overlayMaps[key] = L.layerGroup()
        overlayMaps[key]._extractor = _.partial(age, value)
        overlayMaps[key].addTo(map)
    })

    L.control.layers(null, overlayMaps).addTo(map);

    return overlayMaps
}

$(document).ready(function() {

    var map = init_map()

    var overlayMaps = init_map_layers(map)

    $.get('/api/census/')
        .then(function (data) {
            add_head_map_data_points(map, overlayMaps, data)
        })
})
