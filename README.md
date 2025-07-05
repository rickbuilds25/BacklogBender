# 📦 Backlog Bender v1.0

> An AI agent that turns messy backlogs into clean, prioritized, timeline-ready roadmaps.

Built for product managers who are tired of spreadsheets, sticky notes, and decision fatigue.

---

## 🧠 What It Does

Backlog Bender takes in:
- ✅ Your product goals or OKRs (as `.txt` or `.docx`)
- ✅ A raw backlog (`.csv`) with tasks and effort only

And gives you:
- 📊 AI-assisted Impact scores based on your goals
- 📂 Grouped tasks by Now / Next / Later
- 🏷 MoSCoW tags (Must, Should, Could, Won’t)
- 🗓 A clean roadmap in Markdown, CSV, and plaintext formats

---

## 🚀 How to Use

```bash
# Step 1: Clone the repo
$ git clone https://github.com/rickbuilds25/BacklogBender.git
$ cd BacklogBender

# Step 2: Drop your input files
- Place your backlog CSV into `data/sample_backlog_v2.csv`
- Place your goals file into `data/goals.txt`

# Step 3: Run the agent
$ python main.py --backlog data/sample_backlog_v2.csv --goals data/goals.txt

# Step 4: Check your roadmap in `output/`
```

---

## 📅 Input Format

### sample_backlog_v2.csv
| Task | Impact | Effort | Notes |
|------|--------|--------|-------|
| Add audit logging | (leave blank) | 3 | Enterprise ask |

> ⚠️ *Impact is auto-generated based on alignment to your goals.*
> 
> Tasks with vague descriptions will trigger a warning and may score low.

### goals.txt
```
- Increase new user activation rate from 55% to 75% in Q3
- Improve system reliability and reduce incident count by 40%
- Launch enterprise-readiness features to support 3 upcoming sales demos
- Reduce churn among power users by 15% through targeted engagement
- Improve security posture and achieve SOC 2 readiness by end of quarter
```

---

## 🧩 Modules (Jira Linked)

| Module | Jira Task | Description |
|--------|-----------|-------------|
| `parser/backlog_parser.py` | AABB-5 | Parse backlog, compute AI impact from goals |
| `engine/scoring.py` | AABB-6 | RICE/ICE priority scoring |
| `engine/dependency_mapper.py` | AABB-7 | Analyze task dependencies |
| `engine/roadmap_builder.py` | AABB-8 | Build grouped roadmap |
| `ui/exporter.py` | AABB-9 | Export roadmap to MD, CSV, TXT |
| `engine/velocity_planner.py` | AABB-10 | Optional: capacity-aware planning |
| `utils/jira_sync.py` | AABB-11 | Optional: Sync to Jira |

---

## 🛠 Requirements
- Python 3.10+
- See `requirements.txt` for dependencies

Install with:
```bash
pip install -r requirements.txt
```

---

## 🧪 Sample Output
Outputs go into the `output/` folder and include:
- `roadmap.md`
- `prioritized_backlog.csv`
- `summary.txt`

---

## 🧠 Why We Built This
Because PMs should spend less time cleaning backlogs and more time shipping real product work. Backlog Bender is part of a growing suite of AI agents under **The Product Geek**.

> PMs deserve better tools. So we’re building them.

---

## 👨‍💻 Author
**Arindam (a.k.a RickBuilds25)**  
[@the.productgeek](https://www.instagram.com/the.productgeek) on Instagram

---

## 🛡 License
MIT
