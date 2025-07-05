## 📦 Backlog Bender v1.0

An AI agent that turns messy backlogs into clean, prioritized, timeline-ready roadmaps

Built for PMs who are tired of juggling vague tasks, shifting stakeholder demands, and never-ending backlogs — this agent helps you bring **focus, structure, and clarity** to your product planning.

> “It’s not about doing more. It’s about knowing what not to do.” — Some Jobsian wisdom 🧘

Backlog Bender blends AI intelligence with product intuition. It lets you:
- Tie every task to an actual product goal
- Cut through the noise of ‘everything feels important’
- Ship roadmaps that feel like strategy, not to-do lists

---

## 🚀 What It Does

1. **🧾 Parses Backlog**: Accepts CSVs with tasks and optional effort values.
2. **📌 Connects to Goals**: Uses your product OKRs to estimate task impact.
3. **🧠 Embedding-Driven Relevance**: Matches tasks to goals using OpenAI embeddings.
4. **📊 Scores with RICE**: Calculates or overrides RICE scores using Reach, Impact, Confidence, Effort.
5. **🏷️ Labels Automatically**: Categorizes tasks as Must-Have, Nice-to-Have, Future, Optional based on rules.
6. **📋 Generates Output**:
   - Scored CSV with labels
   - Priority-based markdown roadmap
   - Timeline-aware sprint roadmap

---

## 📥 Inputs

### `data/sample_backlog_scored.csv`
- Required columns: `Task`, `Effort`
- Optional columns: `Reach`, `Confidence`, `ManualScore`

### `data/goals.txt`
- Each line is one product goal / OKR.

### `.env`
```
OPENAI_API_KEY=your-key-here
SPRINT_VELOCITY=10
```

---

## 🛠 Requirements

- Python 3.8+
- `openai`, `pandas`, `scikit-learn`, `python-dotenv`
- A valid OpenAI API key

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🧪 How to Run

### Step 1: Score the backlog
```bash
python3 -c "from engine.scoring import score_backlog; score_backlog('data/sample_backlog_scored.csv')"
```
- Produces: `outputs/scored_backlog_<timestamp>.csv`

### Step 2: Generate label-based roadmap
```bash
python3 -c "from engine.roadmap_builder import build_roadmap; build_roadmap('outputs/scored_backlog_<timestamp>.csv')"
```
- Produces: `outputs/roadmap_<timestamp>.md`

### Step 3: Generate timeline-based roadmap
```bash
python3 -c "from engine.roadmap_timeline import build_timeline_roadmap; build_timeline_roadmap('outputs/scored_backlog_<timestamp>.csv')"
```
- Produces: `outputs/roadmap_timeline_<timestamp>.md`

---

## ⚙️ Configs

### `config/scoring_rules.txt`
```
🚀 Must-Have: 400
🌱 Nice-to-Have: 200
🔮 Future: 75
🧪 Optional: 0
```

---

## 🧪 Sample Output

### 🗓️ Timeline Roadmap (Velocity-aware)

```
## Sprint 1
- [ ] Auto-assign tasks to engineers (🚀 Must-Have)
- [ ] Run performance audit (🚀 Must-Have)
- [ ] Clean unused API endpoints (🚀 Must-Have)
- [ ] Set up alerts for failed payments (🚀 Must-Have)
- [ ] Refactor billing module (🚀 Must-Have)

## Sprint 2
- [ ] Add changelog feature (🚀 Must-Have)
- [ ] Migrate to new auth provider (🌱 Nice-to-Have)
- [ ] Add audit logging (🌱 Nice-to-Have)
- [ ] Improve onboarding flow (🌱 Nice-to-Have)
- [ ] Fix mobile layout bugs (🌱 Nice-to-Have)

## Sprint 3
- [ ] Implement dark mode (🌱 Nice-to-Have)
- [ ] Enable 2FA login (🌱 Nice-to-Have)
- [ ] Revamp dashboard UI (🔮 Future)
- [ ] Launch referral program (🔮 Future)

## Sprint 4
- [ ] Segment power users (🔮 Future)
```

---

## 🧠 AI Inside

- Uses `text-embedding-3-small` to match tasks to goals.
- Warns users when task descriptions are too vague to embed.

---

**Made with 💕 by THE PRODUCT GEEK  |  theproductgeek.club  |  Instagram: @the.productgeek  |  LinkedIn: Arindam Nath**
