import pandas as pd
import math
import os
from datetime import datetime

# Compute RICE score per row
def compute_rice(row):
    manual_score = row.get('ManualScore')
    if pd.notna(manual_score):
        return float(manual_score)

    try:
        reach = float(row.get('Reach', 0))
        impact = float(row.get('Impact', 0))
        confidence = float(row.get('Confidence', 0))
        effort = float(row.get('Effort', 1)) or 1  # Avoid divide by zero

        score = (reach * impact * confidence) / effort
        return round(score, 2)
    except Exception as e:
        print(f"[RICE Error] for task '{row.get('Task', 'Unknown')}': {e}")
        return 0.0

def score_backlog(csv_path: str, output_path: str = None):
    print("\n📊 Starting RICE scoring engine...")
    print(f"📂 Reading backlog from: {csv_path}")

    df = pd.read_csv(csv_path)
    rice_scores = []

    for _, row in df.iterrows():
        print(f"🔎 Scoring task: {row['Task']}...", end=" ")
        if pd.notna(row.get('ManualScore')):
            print(f"✅ Using manual override: {row['ManualScore']}")
        else:
            print("🧮 Calculating RICE score...")

        score = compute_rice(row)
        rice_scores.append(score)

    df['RICE Score'] = rice_scores

    print("\n🎉 Scoring complete! Here's a preview:")
    print(df[['Task', 'RICE Score']].head(10))

    if not output_path:
        os.makedirs("outputs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"outputs/scored_backlog_{timestamp}.csv"

    df.to_csv(output_path, index=False)
    print(f"💾 Scored backlog saved to: {output_path}")

    return df
