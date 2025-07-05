from dotenv import load_dotenv
import os
import openai
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get embedding for a single string
def get_embedding(text: str) -> list:
    try:
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return response['data'][0]['embedding']
    except Exception as e:
        print(f"[Embedding Error] {e}")
        return None

# Compute cosine similarity between task and goals
def compute_similarity(task: str, goals: list[str]) -> tuple[float, str]:
    task_vec = get_embedding(task)
    goal_vecs = [get_embedding(goal) for goal in goals]

    if not task_vec or any(g is None for g in goal_vecs):
        return 0.0, "No valid goal match (embedding error)"

    try:
        task_vec = np.nan_to_num(task_vec)
        goal_vecs = [np.nan_to_num(vec) for vec in goal_vecs]

        similarity_scores = cosine_similarity(
            [task_vec],
            goal_vecs
        )[0]
        max_index = np.argmax(similarity_scores)
        max_score = similarity_scores[max_index]

        impact_score = round(float(max_score * 10), 2)
        return impact_score, goals[max_index]
    except Exception as e:
        print(f"[Warning] Cosine similarity error: {e}")
        return 0.0, "Similarity computation failed"

# Main parser logic
def parse_backlog(backlog_path: str, goals_path: str) -> pd.DataFrame:
    df = pd.read_csv(backlog_path)
    with open(goals_path, 'r') as f:
        goals = [line.strip() for line in f.readlines() if line.strip()]

    impact_scores = []
    goal_matches = []

    for _, row in df.iterrows():
        task = row['Task']
        similarity, matched_goal = compute_similarity(task, goals)
        impact_scores.append(similarity)
        goal_matches.append(matched_goal)

    df['Impact'] = impact_scores
    df['Matched Goal'] = goal_matches

    for _, row in df.iterrows():
        print(f"{row['Task']} → Impact: {row['Impact']} | Goal: {row['Matched Goal']}")

    return df
