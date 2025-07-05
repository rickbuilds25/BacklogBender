import pandas as pd
import os
from datetime import datetime

def build_roadmap(csv_path):
    print("\n🧭 Building roadmap from scored backlog...")

    df = pd.read_csv(csv_path)

    # Group tasks by label (bucket)
    grouped = df.groupby("Label")

    # Create markdown string
    roadmap_md = "# 🗺️ Product Roadmap\n\n"
    for label, group in grouped:
        roadmap_md += f"## {label}\n"
        for task in group["Task"]:
            roadmap_md += f"- [ ] {task}\n"
        roadmap_md += "\n"

    # Also print to terminal for CLI friendliness
    print("\n📋 Roadmap Preview:")
    print("-------------------")
    print(roadmap_md)

    # Save to outputs/
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"outputs/roadmap_{timestamp}.md"

    with open(output_path, "w") as f:
        f.write(roadmap_md)

    print(f"✅ Roadmap markdown saved to: {output_path}\n")
    return output_path
