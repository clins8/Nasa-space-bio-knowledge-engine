function createCharts(data) {
    createOrganismChart(data);
    createEnvironmentChart(data);
    createTimelineChart(data);
}

function createOrganismChart(data) {
    const organismCounts = {};
    data.forEach(exp => {
        organismCounts[exp.organism_type] = (organismCounts[exp.organism_type] || 0) + 1;
    });

    const trace = {
        type: 'pie',
        labels: Object.keys(organismCounts),
        values: Object.values(organismCounts),
        marker: {
            colors: ['#6c63ff', '#4ecdc4', '#ff6b6b']
        }
    };

    const layout = {
        title: 'Studies by Organism Type',
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: 'white' },
        showlegend: true
    };

    Plotly.newPlot('chartContainer', [trace], layout, { responsive: true });
}

function createEnvironmentChart(data) {
    const envCounts = {};
    data.forEach(exp => {
        envCounts[exp.environment] = (envCounts[exp.environment] || 0) + 1;
    });

    const trace = {
        type: 'bar',
        x: Object.keys(envCounts),
        y: Object.values(envCounts),
        marker: {
            color: '#6c63ff'
        }
    };

    const layout = {
        title: 'Studies by Space Environment',
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: 'white' },
        xaxis: { tickangle: -45 }
    };

    Plotly.newPlot('chartContainer', [trace], layout, { responsive: true });
}

function createTimelineChart(data) {
    const yearCounts = {};
    data.forEach(exp => {
        yearCounts[exp.year] = (yearCounts[exp.year] || 0) + 1;
    });

    const years = Object.keys(yearCounts).sort();
    const counts = years.map(year => yearCounts[year]);

    const trace = {
        type: 'scatter',
        mode: 'lines+markers',
        x: years,
        y: counts,
        line: { color: '#4ecdc4', width: 3 },
        marker: { color: '#ff6b6b', size: 8 }
    };

    const layout = {
        title: 'Research Timeline',
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: 'white' }
    };

    Plotly.newPlot('chartContainer', [