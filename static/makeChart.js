function makeChart(canvasId, data, label="placeholder", type, unit, startDate=null, yMin=null, yMax=null, options = null, scaleType = 'linear') {
    const ctx = document.getElementById(canvasId);
    
    const defaultOptions = {
        scales: {
            // responsive: true,
            // maintainAspectRatio: false,
            x: {
                type: 'time',
                time: {
                    unit: unit
                }  
            },
            y: {
                min: yMin,
                max: yMax
            }
        },
        plugins: {
            legend: {
                display: false
            } 
        }
               
    };
    // If startDate is provided, filter the data from that date onwards
    if (startDate) {
        data = data.filter(item => new Date(item.x) >= new Date(startDate));
    }

    
    new Chart(ctx, {
        type: type,
        data: {        
            datasets: [{                
                label: label,
                data: data,                
                borderWidth: 3,
                pointRadius: 0
            }]
        },
        options: options || defaultOptions
    });
}
