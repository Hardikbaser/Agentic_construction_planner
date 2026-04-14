const API = "http://127.0.0.1:8000";

function toggleLoading(show) {
  document.getElementById("loading").classList.toggle("hidden", !show);
}

// =========================
// 📋 PLAN
// =========================
async function generatePlan() {
  const goal = document.getElementById("goalInput").value;
  toggleLoading(true);

  try {
    const res = await fetch(`${API}/plan`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ goal })
    });

    const data = await res.json();
    document.getElementById("planOutput").textContent = data.plan;

  } catch (err) {
    alert("Error generating plan");
    console.error(err);
  }

  toggleLoading(false);
}

// =========================
// 📅 SCHEDULE
// =========================
async function generateSchedule() {
  const goal = document.getElementById("goalInput").value;
  toggleLoading(true);

  try {
    const res = await fetch(`${API}/schedule`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ goal })
    });

    const data = await res.json();
    document.getElementById("scheduleOutput").textContent = data.schedule;

  } catch (err) {
    alert("Error generating schedule");
    console.error(err);
  }

  toggleLoading(false);
}

// =========================
// 🆕 SITE REPORT
// =========================
async function generateReport() {
  const goal = document.getElementById("goalInput").value;
  const type = document.getElementById("reportType")?.value || "site";

  toggleLoading(true);
  document.getElementById("reportOutput").textContent = "Generating report...";

  try {
    const res = await fetch(`${API}/generate-report`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        query: goal,
        type: type
      })
    });

    const data = await res.json();
    document.getElementById("reportOutput").textContent = data.final_report;

  } catch (err) {
    alert("Error generating report");
    console.error(err);
    document.getElementById("reportOutput").textContent = "Error generating report";
  }

  toggleLoading(false);
}

// =========================
// ⬇ DOWNLOAD REPORT
// =========================
function downloadReport() {
  const text = document.getElementById("reportOutput").textContent;

  if (!text || text.includes("appear here")) {
    alert("No report to download!");
    return;
  }

  const blob = new Blob([text], { type: "text/plain" });
  const link = document.createElement("a");

  link.href = URL.createObjectURL(blob);
  link.download = "site_report.txt";
  link.click();
}

// ✅ 🔥 GLOBAL SCOPE (MOVE HERE)
window.generatePlan = generatePlan;
window.generateSchedule = generateSchedule;
window.generateReport = generateReport;
window.downloadReport = downloadReport;