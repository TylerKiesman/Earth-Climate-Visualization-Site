function showPlot(graphs, id){
    data = graphs[0].data;
    layout = graphs[0].layout;
    Plotly.newPlot(id, data, layout);
}

function updatePeriod(periodNumber){
    var request = new XMLHttpRequest();

    request.open("GET", "updatePeriod?number=" + periodNumber);

    request.onreadystatechange = function() {
        if(this.readyState === 4 && this.status === 200) {
            showPlot(JSON.parse(request.response), 'period');
        }
    };

    request.send();
}