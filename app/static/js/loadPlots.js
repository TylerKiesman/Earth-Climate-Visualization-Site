function showPlot(graphs, id){
    data = graphs[0].data;
    layout = graphs[0].layout;
    Plotly.plot(id, data, layout);
}