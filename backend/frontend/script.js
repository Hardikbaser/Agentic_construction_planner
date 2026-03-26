const API = "http://127.0.0.1:8000";

function toggleLoading(show) {
  document.getElementById("loading").classList.toggle("hidden", !show);
}

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