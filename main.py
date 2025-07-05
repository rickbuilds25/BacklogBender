import os
from dotenv import load_dotenv
from parser.backlog_parser import parse_backlog
from engine.scoring import score_backlog
from engine.roadmap_builder import build_roadmap
from engine.roadmap_timeline import build_timeline_roadmap
import time

def print_banner():
    print("""
===========================================
🚀 Backlog Bender v1.0 — Roadmap Builder Agent
===========================================
    """)

def run_pipeline(backlog_path, goals_path):
    print_banner()

    # Load environment variables
    load_dotenv()
    velocity = os.getenv("SPRINT_VELOCITY")
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("❌ OPENAI_API_KEY is missing. Please check your .env file.")
        return

    print("📥 Parsing backlog and goals...")
    parsed_tasks = parse_backlog(backlog_path, goals_path)

    print("\n📊 Scoring backlog...")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    scored_file = f"outputs/scored_backlog_{timestamp}.csv"
    score_backlog(backlog_path, output_path=scored_file)

    print("\n🛠 Generating roadmap (label-based)...")
    build_roadmap(scored_file)

    print("\n📆 Generating sprint-based timeline roadmap...")
    build_timeline_roadmap(scored_file)

    print("\n✅ All done! Your backlogs have been bent.")
    print("Check the 'outputs/' folder for generated files.")

if __name__ == "__main__":
    run_pipeline("data/sample_backlog_scored.csv", "data/goals.txt")
