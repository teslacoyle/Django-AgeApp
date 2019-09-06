$(document).ready(function () {
    var chartCanvas = $('#ageHistogram');
    var ageHist = new Chart(chartCanvas, {
        type: 'bar',
        data: {
            labels: [axisLabels],
            datasets: [{
                label: "Age",
                data: [axisValues],
                backgroundColor: [Html.Raw(colorValues)]
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    barPercentage: 1.0
                }],
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
});