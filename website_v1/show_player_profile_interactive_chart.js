


document.addEventListener("DOMContentLoaded", () => {
    // === Setup constants ===
    const availableMetrics = [
    { key: "AVG", label: "打擊率 (AVG)" },
    { key: "HR", label: "全壘打 (HR)" },
    { key: "RBI", label: "打點 (RBI)" },
    { key: "OBP", label: "上壘率 (OBP)" },
    { key: "ERA", label: "防禦率 (ERA)" },
    { key: "K", label: "三振 (K)" },
    { key: "W", label: "勝場 (W)" },
    ];

    // Example: from your processed data
    // Replace this with your real `seasons` array
    const seasons = [
    { year: "2023", AVG: 0.298, HR: 22, RBI: 78, OBP: 0.365, ERA: 3.12, K: 152, W: 12 },
    { year: "2024", AVG: 0.305, HR: 26, RBI: 81, OBP: 0.378, ERA: 2.95, K: 168, W: 14 },
    { year: "2025", AVG: 0.312, HR: 28, RBI: 86, OBP: 0.392, ERA: 2.84, K: 176, W: 15 },
    ];

    // === Populate dropdowns ===
    const selectA = document.getElementById("trendMetricA");
    const selectB = document.getElementById("trendMetricB");
    const selectType = document.getElementById("trendChartType");
    const applyBtn = document.getElementById("applyTrendBtn");
    const canvas = document.getElementById("customTrendChart");
    let chartInstance = null;

    availableMetrics.forEach(m => {
    const optA = document.createElement("option");
    const optB = document.createElement("option");
    optA.value = optB.value = m.key;
    optA.textContent = optB.textContent = m.label;
    selectA.appendChild(optA);
    selectB.appendChild(optB);
    });

    // Default selections
    selectA.value = "AVG";
    selectB.value = "ERA";

    // === Drag & Drop Swapping ===
    [selectA, selectB].forEach(sel => {
    sel.setAttribute("draggable", "true");
    sel.addEventListener("dragstart", e => {
        e.dataTransfer.setData("metric", sel.id);
        sel.style.opacity = 0.6;
    });
    sel.addEventListener("dragend", () => (sel.style.opacity = 1));
    });

    selectB.addEventListener("dragover", e => e.preventDefault());
    selectA.addEventListener("dragover", e => e.preventDefault());

    selectB.addEventListener("drop", e => swapMetrics(e, selectA, selectB));
    selectA.addEventListener("drop", e => swapMetrics(e, selectB, selectA));

    function swapMetrics(e, fromSel, toSel) {
    e.preventDefault();
    const temp = fromSel.value;
    fromSel.value = toSel.value;
    toSel.value = temp;
    }

    // === Chart.js Render ===
    function renderChart(metricA, metricB, chartType) {
    const years = seasons.map(s => s.year);
    const dataA = seasons.map(s => s[metricA]);
    const dataB = seasons.map(s => s[metricB]);

    if (chartInstance) chartInstance.destroy();

    chartInstance = new Chart(canvas, {
        type: chartType,
        data: {
        labels: years,
        datasets: [
            {
            label: availableMetrics.find(m => m.key === metricA)?.label || metricA,
            data: dataA,
            borderWidth: 2,
            borderColor: "rgba(99, 102, 241, 1)",
            backgroundColor: "rgba(99, 102, 241, 0.3)",
            fill: false,
            tension: 0.3,
            },
            {
            label: availableMetrics.find(m => m.key === metricB)?.label || metricB,
            data: dataB,
            borderWidth: 2,
            borderColor: "rgba(244, 114, 182, 1)",
            backgroundColor: "rgba(244, 114, 182, 0.3)",
            fill: false,
            tension: 0.3,
            },
        ],
        },
        options: {
        responsive: true,
        interaction: { mode: "index", intersect: false },
        plugins: {
            legend: { position: "top" },
            title: { display: true, text: "球員年度數據趨勢" },
            tooltip: {
            callbacks: {
                label: ctx => `${ctx.dataset.label}: ${ctx.parsed.y.toFixed(3)}`,
            },
            },
        },
        scales: {
            y: { beginAtZero: true },
        },
        },
    });
    }

    // === Apply button handler ===
    applyBtn.addEventListener("click", () => {
    const metricA = selectA.value;
    const metricB = selectB.value;
    const chartType = selectType.value;
    renderChart(metricA, metricB, chartType);
    });

    // Render default chart on load
    renderChart("AVG", "ERA", "line");
});