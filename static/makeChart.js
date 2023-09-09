function makeChart(canvasId, data, label = 'Data', type, unit, options = null) {
    const ctx = document.getElementById(canvasId);
    
    const defaultOptions = {
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: unit
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
