<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>AI Production Engineer Roadmap — README</title>

  <!-- Google Font (optional) -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">

  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --muted:#9aa6b2;
      --accent:#6ee7b7;
      --accent-2:#60a5fa;
      --glass: rgba(255,255,255,0.03);
      --radius:14px;
      --maxwidth:1100px;
      color-scheme: dark;
    }
    *{box-sizing:border-box;font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;}
    body{
      margin:0;
      padding:32px;
      background: linear-gradient(180deg,#071025 0%, #071a2a 70%);
      color:#e6eef6;
      display:flex;
      justify-content:center;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
    }
    .wrap{
      width:100%;
      max-width:var(--maxwidth);
      background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius:18px;
      padding:28px;
      box-shadow: 0 8px 40px rgba(2,6,23,0.6);
      border: 1px solid rgba(255,255,255,0.03);
    }

    header{
      display:flex;
      gap:16px;
      align-items:center;
      justify-content:space-between;
      margin-bottom:18px;
    }
    .title {
      display:flex;
      gap:14px;
      align-items:center;
    }
    .logo {
      width:64px;height:64px;background:linear-gradient(135deg,var(--accent),var(--accent-2));
      border-radius:12px; display:flex;align-items:center;justify-content:center;
      font-weight:700;color:#021124;font-size:28px;
      box-shadow: 0 6px 20px rgba(96,165,250,0.08), inset 0 -4px 12px rgba(255,255,255,0.05);
    }
    h1{margin:0;font-size:20px;letter-spacing:-0.2px}
    p.lead{margin:0;color:var(--muted);font-size:13.5px;max-width:820px}

    .badges {display:flex; gap:8px; align-items:center; margin-top:8px;}
    .badge{
      background:var(--glass);
      padding:6px 10px;
      border-radius:999px;
      border:1px solid rgba(255,255,255,0.03);
      color:var(--muted);
      font-size:12px;
    }

    main{margin-top:20px; display:grid; gap:20px;}

    /* Phase cards grid */
    .phases {
      display:grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap:14px;
    }
    .phase{
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      padding:16px;border-radius:12px;border:1px solid rgba(255,255,255,0.03);
      min-height:120px;
    }
    .phase h3{margin:0 0 8px 0;font-size:15px}
    .phase ul{margin:0;padding-left:18px;color:var(--muted);font-size:13px}

    /* Two-column area */
    .grid-2{
      display:grid;
      grid-template-columns: 1fr 360px;
      gap:18px;
    }
    @media (max-width:980px){ .grid-2{ grid-template-columns: 1fr; } }

    /* Repo structure */
    .card{
      background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.005));
      border-radius:12px;padding:16px;border:1px solid rgba(255,255,255,0.02);
    }
    pre.code{
      background:linear-gradient(180deg, rgba(2,6,23,0.6), rgba(3,10,30,0.6));
      padding:12px;border-radius:10px;overflow:auto;margin:8px 0;color:#cfe8ff;font-size:13px;
      border:1px solid rgba(255,255,255,0.03);
    }

    /* Progress table */
    table{
      width:100%;border-collapse:collapse;font-size:13px;
    }
    th, td{
      text-align:left;padding:10px;border-bottom:1px dashed rgba(255,255,255,0.03);
      color:var(--muted);
    }
    th{color:#dbeafe;font-weight:600;font-size:13px}
    .status-starting{color:#a3e635;font-weight:700}
    .status-planned{color:#f59e0b;font-weight:700}
    .status-complete{color:#60a5fa;font-weight:700}

    /* Footer CTA */
    .actions{display:flex;gap:10px;margin-top:10px;flex-wrap:wrap}
    .btn{
      padding:10px 14px;border-radius:10px;border:none;cursor:pointer;font-weight:600;
      background:linear-gradient(90deg,var(--accent),var(--accent-2)); color:#011522; text-decoration:none;
      box-shadow: 0 6px 18px rgba(96,165,250,0.06);
    }
    .btn-ghost{background:transparent;border:1px solid rgba(255,255,255,0.04);color:var(--muted)}

    .muted-note{font-size:13px;color:var(--muted);margin-top:8px}
    footer{margin-top:18px;color:var(--muted);font-size:13px;display:flex;justify-content:space-between;align-items:center}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="title">
        <div class="logo">AI</div>
        <div>
          <h1>AI Production Engineer Roadmap</h1>
          <p class="lead">From Python foundations to deployed, agentic AI systems — day-by-day practical learning, projects and production thinking.</p>
          <div class="badges" aria-hidden="true">
            <span class="badge">Status — In Progress</span>
            <span class="badge">Duration — 14–17 weeks</span>
            <span class="badge">Daily — 3–4 hours</span>
            <span class="badge">Focus — Python · GenAI · Agentic AI · MLOps</span>
          </div>
        </div>
      </div>

      <div style="text-align:right">
        <a class="btn" href="AI_Master_Roadmap.pdf" download>Download Full Roadmap</a>
        <div class="muted-note">Source: roadmap PDF. :contentReference[oaicite:1]{index=1}</div>
      </div>
    </header>

    <main>
      <!-- Overview -->
      <section class="card">
        <strong style="display:block;margin-bottom:8px">Overview</strong>
        <div style="color:var(--muted);font-size:14px;line-height:1.45">
          This repository documents a structured learning path to become an AI Production Engineer. The roadmap progresses across four phases — Foundations, GenAI/RAG, Agentic AI, and MLOps & Production. Each day contains hands-on practice, notes, and resources. Use the repo structure below to navigate and contribute your daily work.
        </div>
      </section>

      <!-- Phases -->
      <section class="phases" aria-label="Phases overview">
        <div class="phase card">
          <h3>Phase 1 — Foundations</h3>
          <ul>
            <li>Weeks 1–6: Python, NumPy, Pandas, Matplotlib</li>
            <li>Math, classic ML, intro deep learning</li>
            <li>Basic GenAI & prompt engineering</li>
          </ul>
        </div>

        <div class="phase card">
          <h3>Phase 2 — GenAI & RAG</h3>
          <ul>
            <li>Weeks 7–10: RAG, embeddings, vector DBs</li>
            <li>LangChain, evaluation & hallucination control</li>
            <li>Multimodal AI projects</li>
          </ul>
        </div>

        <div class="phase card">
          <h3>Phase 3 — Agentic AI</h3>
          <ul>
            <li>Weeks 11–14: Agentic systems, multi-agent</li>
            <li>Protocols (MCP/A2A), safety & governance</li>
            <li>Domain-specific agents</li>
          </ul>
        </div>

        <div class="phase card">
          <h3>Phase 4 — MLOps & Production</h3>
          <ul>
            <li>Weeks 15–17: FastAPI, Docker, cloud deployment</li>
            <li>Monitoring, drift detection, retraining</li>
            <li>End-to-end production systems</li>
          </ul>
        </div>
      </section>

      <!-- Two-column: repo structure + progress -->
      <div class="grid-2">
        <div class="card">
          <strong>Repository Structure</strong>
          <pre class="code">
AI-Production-Engineer-Roadmap/
├── README.md                      # Landing overview (this file)
├── AI_Master_Roadmap.pdf          # Full roadmap (downloadable)
├── Phase-1-Foundations/
│   └── Week-1-Python/
│       └── Day-2-Environment/
├── Phase-2-GenAI/
├── Phase-3-AgenticAI/
├── Phase-4-MLOps/
└── progress-tracker/
          </pre>

          <div class="muted-note">
            Each <code>Day-X</code> folder should include: practice scripts / notebooks, <code>notes.md</code>, and <code>resources.md</code>.
          </div>

          <div style="margin-top:12px" class="actions">
            <a class="btn" href="#progress">Update Progress</a>
            <a class="btn-ghost" href="CONTRIBUTING.md">How to contribute</a>
          </div>
        </div>

        <aside id="progress" class="card">
          <strong>Progress Snapshot</strong>
          <table aria-label="Progress table">
            <thead>
              <tr><th>Phase</th><th>Week</th><th>Focus</th><th>Days</th><th>Status</th></tr>
            </thead>
            <tbody>
              <tr>
                <td>Phase 1 — Foundations</td>
                <td>Week 1</td>
                <td>Python setup & basics</td>
                <td>0 / 7</td>
                <td class="status-starting">Starting</td>
              </tr>
              <tr>
                <td>Phase 2 — GenAI & RAG</td>
                <td>Week 4</td>
                <td>LangChain, RAG pipeline</td>
                <td>0 / 7</td>
                <td class="status-planned">Planned</td>
              </tr>
              <tr>
                <td>Phase 3 — Agentic AI</td>
                <td>Week 11</td>
                <td>Multi-agent systems</td>
                <td>0 / 7</td>
                <td class="status-planned">Planned</td>
              </tr>
              <tr>
                <td>Phase 4 — MLOps</td>
                <td>Week 15</td>
                <td>Deployment & monitoring</td>
                <td>0 / 7</td>
                <td class="status-planned">Planned</td>
              </tr>
            </tbody>
          </table>

          <div class="muted-note" style="margin-top:10px">
            Tip: Keep this table accurate. A clear public progress log builds trust and shows consistency.
          </div>
        </aside>
      </div>

      <!-- Goals -->
      <section class="card">
        <strong>Goals</strong>
        <ul style="color:var(--muted);font-size:14px">
          <li>Document a daily learning journey across the AI stack.</li>
          <li>Deliver multiple deployable GenAI / Agent projects with MLOps.</li>
          <li>Build a portfolio demonstrating production thinking and consistency.</li>
        </ul>

        <div style="margin-top:12px; display:flex;gap:10px;flex-wrap:wrap">
          <a class="btn" href="AI_Master_Roadmap.pdf">Open Roadmap PDF</a>
          <a class="btn-ghost" href="#progress">Edit progress</a>
        </div>
      </section>

    </main>

    <footer>
      <div>Learning in public • One day, one commit, one production skill at a time.</div>
      <div style="font-size:12px;color:var(--muted)">Roadmap PDF: :contentReference[oaicite:2]{index=2}</div>
    </footer>
  </div>
</body>
</html>
