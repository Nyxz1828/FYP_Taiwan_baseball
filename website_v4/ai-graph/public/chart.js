const chartCanvas = document.getElementById("chart");
const loader = document.getElementById("loader");

let currentChart = null;


// Create a status label
const status = document.createElement("p");
status.style.marginTop = "10px";
status.style.fontSize = "1rem";
status.style.color = "#555";
document.body.insertBefore(status, chartCanvas);

document.getElementById("generate").onclick = async () => {
  const prompt = document.getElementById("prompt").value.trim();
  if (!prompt) return alert("Please enter a prompt!");

  status.textContent = "🧠 Generating chart... please wait ⏳";

  try {
    const response = await fetch("/api/generate-graph", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });

    // Check network / API response
    if (!response.ok) {
      status.textContent = "❌ Server error while generating chart.";
      return;
    }

    const { jsCode } = await response.json();
    console.log("🧩 Generated Code:\n", jsCode);

    // Remove previous chart
    if (currentChart) currentChart.destroy();

    // Execute generated Chart.js code
    const func = new Function("Chart", "ctx", jsCode);
    currentChart = func(Chart, chartCanvas);

    status.textContent = "✅ Chart generated successfully!";
  } catch (error) {
    console.error("❌ Error:", error);
    status.textContent = "⚠️ Failed to generate chart. Check console for details.";
  }
};
