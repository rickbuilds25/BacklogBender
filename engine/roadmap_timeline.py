import pandas as pd
import os
from datetime import datetime
import math
from dotenv import load_dotenv

load_dotenv()

SPRINT_VELOCITY = int(os.getenv("SPRINT_VELOCITY", 10))  # default 10 effort units per sprint

# Define label priorities
label_priority = {
    "🚀 Must-Have": 1,
    "🌱 Nice-to-Have": 2,
    "🔮 Future": 3,
    "🧪 Optional": 4
}

def build_timeline_roadmap(csv_path):
    print("\n📆 Generating sprint-wise timeline roadmap...")

    df = pd.read_csv(csv_path)
    df["Priority"] = df["Label"].map(label_priority).fillna(99)  # fallback for unknown labels
    df = df.sort_values(by=["Priority", "RICE Score"], ascending=[True, False])

    # Track sprint buckets
    timeline = {}
    sprint = 1
    used = 0

    for _, row in df.iterrows():
        task = row["Task"]
        effort = row.get("Effort", 1)
        if pd.isna(effort) or effort == 0:
            effort = 1  # default fallback

        if used + effort > SPRINT_VELOCITY:
            sprint += 1
            used = 0

        sprint_label = f"Sprint {sprint}"
        if sprint_label not in timeline:
            timeline[sprint_label] = []

        timeline[sprint_label].append((task, row["Label"]))
        used += effort

    # Build markdown output
    md = "# 🗓️ Sprint-wise Roadmap (Velocity-aware)\n\n"
    for sprint, tasks in timeline.items():
        md += f"## {sprint}\n"
        for task, label in tasks:
            md += f"- [ ] {task} ({label})\n"
        md += "\n"

    # Print to CLI
    print("\n🧾 Timeline Preview:")
    print("------------------")
    print(md)

    # Save to file
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = f"outputs/roadmap_timeline_{timestamp}.md"

    with open(out_path, "w") as f:
        f.write(md)

    print(f"✅ Sprint-wise timeline roadmap saved to: {out_path}\n")
    return out_path
