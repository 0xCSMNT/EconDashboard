function makeChart(canvasId, data, label="placeholder", type, unit, startDate=null, options = null) {
    const ctx = document.getElementById(canvasId);
    
    const defaultOptions = {
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: unit
                }  
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
                borderWidth: 1
            }]
        },
        options: options || defaultOptions
    });
}
