document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('myChart').getContext('2d');
    let chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Insights',
                data: [],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    function fetchData() {
        const sector = document.getElementById('sector').value;
        const country = document.getElementById('country').value;
        const topic = document.getElementById('topic').value;
        const region = document.getElementById('region').value;
        const pestle = document.getElementById('pestle').value;
        const source = document.getElementById('source').value;
        const intensity = document.getElementById('intensity').value;
        const likelihood = document.getElementById('likelihood').value;
        const relevance = document.getElementById('relevance').value;
        const end_year = document.getElementById('end_year').value;
        const start_year = document.getElementById('start_year').value;
        const url = new URL('/data', window.location.origin);
        
        if (sector) url.searchParams.append('sector', sector);
        if (country) url.searchParams.append('country', country);
        if (topic) url.searchParams.append('topic', topic);
        if (region) url.searchParams.append('region', region);
        if (pestle) url.searchParams.append('pestle', pestle);
        if (source) url.searchParams.append('source', source);
        if (intensity) url.searchParams.append('intensity', intensity);
        if (likelihood) url.searchParams.append('likelihood', likelihood);
        if (relevance) url.searchParams.append('relevance', relevance);
        if (end_year) url.searchParams.append('end_year', end_year);
        if (start_year) url.searchParams.append('start_year', start_year);

        fetch(url)
            .then(response => response.json())
            .then(data => {
                const labels = data.map(item => item.title);
                const values = data.map(item => item.relevance);

                chart.data.labels = labels;
                chart.data.datasets[0].data = values;
                chart.update();
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    document.getElementById('apply-filters').addEventListener('click', fetchData);

    fetchData();  // Fetch data initially
});
