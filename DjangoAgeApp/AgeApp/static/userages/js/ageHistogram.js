
buildChart = function (axisLabels, axisValues, colorValues) {
    var chartCanvas = $("#ageHistogram");
    var ageHist = new Chart(chartCanvas, {
        type: 'bar',
        data: {
            labels: axisLabels,
            datasets: [{
                label: "Age",
                data: axisValues,
                backgroundColor: colorValues
            }]
        },
        options: {
            title: {
                display: true,
                text: 'User Age Histogram'
            },
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        stepSize: 1
                    }
                }]
            },
            tooltips: {
                enabled: false
            }
        }
    });
};

