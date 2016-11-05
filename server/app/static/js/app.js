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

    var map = init_map();

    var info = L.control();

    info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info');
        this.update();
        return this._div;
    };

    info.update = function (props) {
        // this._div.innerHTML = props.population;
        this._div.innerHTML = '<h4>Population: ' + (props ? props.population : '-') + '</h4>'
    };

    info.addTo(map);

    function highlightFeature(e) {
        var layer = e.target;

        layer.setStyle({
            weight: 5,
            color: '#666',
            dashArray: '',
            fillOpacity: 0.7
        });

        info.update(layer.feature.properties);
    }

    function resetHighlight(e) {
        var layer = e.target;
        L.geoJSON(null, {
            style: style,
            onEachFeature: onEachFeature
        }).resetStyle(e.target);
        info.update();
    }

    function onEachFeature(feature, layer) {
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight,
        });
    }
    function mapRound(x){
        return Math.ceil(x / 100.0) * 100
    }

    // get color depending on population density value
    var max_workers_diff = 0;
    window.tmp = max_workers_diff;
    var min_workers_diff = 0;

    function getColor(d) {
        return d > mapRound(0.90*max_workers_diff) ? '#800026' :
                //d > mapRound(0.75*max_workers_diff)  ? '#BD0026' :
                d > mapRound(0.65*max_workers_diff)  ? '#E31A1C' :
                //d > mapRound(0.45*max_workers_diff)  ? '#FC4E2A' :
                d > mapRound(0.40*max_workers_diff)   ? '#FD8D3C' :
                //d > mapRound(0.15*max_workers_diff)   ? '#FEB24C' :
                d > mapRound(0.15*max_workers_diff)   ? '#FED976' :
                d > 1 ? '#FFEDA0' : '#FFFFFF';
    }

    function style(feature) {
        return {
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.7,
            fillColor: getColor(feature.properties.population)
        };
    }

    // var overlayMaps = init_map_layers(map)

    // $.get('/api/census/')
    //     .then(function (data) {
    //         add_head_map_data_points(map, overlayMaps, data)
    //     })

    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

        var div = L.DomUtil.create('div', 'info legend'),
            //grades = [0, mapRound(0.05*max_workers_diff), mapRound(0.15*max_workers_diff), mapRound(0.30*max_workers_diff), mapRound(0.45*max_workers_diff), mapRound(0.60*max_workers_diff), mapRound(0.75*max_workers_diff), mapRound(0.90*max_workers_diff)],
            grades = [
                min_workers_diff,
                mapRound(0.15*max_workers_diff),
                mapRound(0.40*max_workers_diff),
                mapRound(0.65*max_workers_diff),
                mapRound(0.90*max_workers_diff)
            ],

            labels = [],
            from, to;

        for (var i = 0; i < grades.length; i++) {
            from = grades[i];
            to = grades[i + 1];

            labels.push(
                '<i style="background:' + getColor(from + 1) + '"></i> ' +
                from + (to ? '&ndash;' + to : '+'));
        }

        div.innerHTML = labels.join('<br>');
        return div;
    };

    $.get('/api/tract_populations/')
        .then(function(data) {
            _.each(data, function(item) {
                var item_population = parseInt(item.properties.population, 10);
                if (item_population > max_workers_diff) {
                    max_workers_diff = item_population;
                }
            })
            return data
        })
        .then(function(data) {
            _.each(data, function(item) {
                L.geoJSON(item, {
                    style: style,
                    onEachFeature: onEachFeature
                }).addTo(map)
            })

        }).then(function() {
            legend.addTo(map);
        });
})
