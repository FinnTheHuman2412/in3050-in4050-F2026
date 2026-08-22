# IN3050 / IN4050 — Group Sessions

Student-facing material for the University of Oslo course **Introduction to Artificial Intelligence and Machine Learning**.

The repository is organized around one principle: each group session should turn abstract lecture concepts into something you can **see, change, and explain**.

## Start here

1. Open the notebook for the current week.
2. Read the short learning goals.
3. Predict what will happen before running each experiment.
4. Change the parameters and explain the result to someone else.
5. Finish the exit ticket without looking at the solution.

## Repository map

| Path | Purpose |
|---|---|
| `weeks/` | Weekly interactive notebooks and exercise material |
| `exercises/` | Short reusable problems and exam-style questions |
| `resources/` | Formula sheets, terminology and recommended links |
| `solutions/` | TA-only solution area; not published to students by default |
| `assets/` | Images and figures used by notebooks |

## Weekly roadmap

| Week | Theme | Status |
|---|---|---|
| 01 | Vectors, matrices and linear decision boundaries | Starter notebook ready |
| 02 | Search and problem formulation | Planned |
| 03 | Heuristic search | Planned |
| 04 | Games and adversarial search | Planned |
| 05 | Constraint satisfaction | Planned |
| 06 | Probability and uncertainty | Planned |
| 07 | Bayesian reasoning | Planned |
| 08 | Machine-learning foundations | Planned |
| 09 | Linear models and evaluation | Planned |
| 10 | Neural networks | Planned |
| 11 | Unsupervised learning | Planned |
| 12 | Reinforcement learning | Planned |
| 13 | Exam synthesis and review | Planned |

The roadmap is intentionally easy to adjust once the official Autumn 2026 lecture plan is final.

## Run locally

Python 3.11 is recommended.

```bash
python -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

Then open `weeks/week-01/01-vectors-matrices-decision-boundaries.ipynb`.

## For students

- You are expected to make mistakes in the notebooks.
- A correct prediction is useful; a wrong prediction followed by a good explanation is often more useful.
- IN4050 students should also complete the marked **IN4050 extension** prompts.
- Do not memorize plots. Learn what causes their shape to change.

## For teaching assistants

See [TEACHING.md](TEACHING.md) for the repeatable session structure and preparation checklist. Keep full solutions outside the public branch until after the relevant deadline.

## Course and copyright note

This is supplementary group-teaching material, not an official course repository. Official announcements, curriculum and deadlines on UiO course pages take precedence. Do not commit copyrighted lecture slides, solution manuals, student submissions, personal data, API keys or credentials.

## License

Original code and prose in this repository are released under the MIT License. Third-party course material retains its original ownership and must not be copied here without permission.
