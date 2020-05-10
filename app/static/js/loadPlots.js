function showPlot(graphs, id){
    data = graphs[0].data;
    layout = graphs[0].layout;
    Plotly.newPlot(id, data, layout);
}

function updatePeriod(periodNumber){
    var request = new XMLHttpRequest();

    // Instantiating the request object
    request.open("GET", "updatePeriod?number=" + periodNumber);

    // Defining event listener for readystatechange event
    request.onreadystatechange = function() {
        // Check if the request is compete and was successful
        if(this.readyState === 4 && this.status === 200) {
            // Inserting the response from server into an HTML element
            console.log(JSON.parse(request.response)[0])
            showPlot(JSON.parse(request.response), 'period');
        }
    };

    // Sending the request to the server
    request.send();
}