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

function make_info_control(title, key) {
    var info = L.control();

    info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info');
        this.update();
        return this._div;
    };

    info.update = function (props) {
        this._div.innerHTML = '<h4>' + title + ': ' + (props ? _.get(props, key) : '-') + '</h4>'
    };

    return info;

}

function make_legend(max_workers_diff) {
    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

        var div = L.DomUtil.create('div', 'info legend'),
            grades = [
                0,
                Math.ceil(0.15 * max_workers_diff),
                Math.ceil(0.40 * max_workers_diff),
                Math.ceil(0.65 * max_workers_diff),
                Math.ceil(0.90 * max_workers_diff)
            ],

            labels = [],
            from, to;

        for (var i = 0; i < grades.length; i++) {
            from = grades[i];
            to = grades[i + 1];

            labels.push(
                '<i style="background:' + getColor(max_workers_diff, from + 1) + '"></i> ' +
                from + (to ? '&ndash;' + to : '+'));
        }

        div.innerHTML = labels.join('<br>');
        return div;
    };

    return legend;
};

function getColor(max_workers_diff, d) {
    return  d > Math.ceil(0.90*max_workers_diff) ? '#800026' :
            d > Math.ceil(0.65*max_workers_diff) ? '#E31A1C' :
            d > Math.ceil(0.40*max_workers_diff) ? '#FD8D3C' :
            d > Math.ceil(0.15*max_workers_diff) ? '#FED976' :
            d > 1                                              ? '#FFEDA0' :
                                                                 '#FFFFFF';
}

function style(max_workers_diff, key, feature) {
    return {
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7,
        fillColor: getColor(max_workers_diff, _.get(feature.properties, key))
    };
}

function highlightFeature(info, e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    info.update(layer.feature.properties);
}

function resetHighlight(info, max_workers_diff, key, e) {
    var layer = e.target;
    L.geoJSON(null, {
        style: _.partial(style, max_workers_diff, key),
        onEachFeature: _.partial(onEachFeature, info, max_workers_diff, key)
    }).resetStyle(e.target);
    info.update();
}

function onEachFeature(info, max_workers_diff, key, feature, layer) {
    layer.on({
        mouseover: _.partial(highlightFeature, info),
        mouseout: _.partial(resetHighlight, info, max_workers_diff, key),
    });
}

function addGeoJSONItem(map, max_workers_diff, info, key, item) {
    L.geoJSON(item, {
        style: _.partial(style, max_workers_diff, key),
        onEachFeature: _.partial(onEachFeature, info, max_workers_diff, key)
    }).addTo(map)
}

function getPopulation(item) {
    return parseInt(item.properties.population, 10)
}

function getData(key, item) {
    return parseInt(_.get(item.properties, key), 10)
}

function main(key, description) {
    var url = '/api/census/' + key;
    var map = init_map();
    $.get(url)
        .then(function(data) {
            var max_workers_diff = _.max(_.map(data, _.partial(getData, key)));
            var info = make_info_control(description, key);
            _.each(data, _.partial(addGeoJSONItem, map, max_workers_diff, info, key));
            var legend = make_legend(max_workers_diff);
            info.addTo(map);
            legend.addTo(map);
        });
}
