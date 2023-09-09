function makeChart(canvasId, data, label = 'Data', type = 'line', options = null) {
    const ctx = document.getElementById(canvasId);
    
    const defaultOptions = {
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'quarter'
                }  
            }
        }
    };
    
    new Chart(ctx, {
        type: type,
        data: {        
            datasets: [{
                label: label,
                data: data,
                borderWidth: 1
            }]
        },
        options: options || defaultOptions
    });
}
