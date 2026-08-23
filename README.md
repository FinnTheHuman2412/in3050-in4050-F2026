# IN3050 / IN4050 - Interactive group sessions

Student-facing material for the University of Oslo course **Introduction to Artificial Intelligence and Machine Learning**.

This repository turns course terminology into things students can **predict, see, change, break and explain**. It combines short Mentimeter diagnostics with executable Jupyter notebooks and exam-style transfer questions.

## Start here

| Item | Link |
|---|---|
| Course progression | [COURSE_MAP.md](COURSE_MAP.md) |
| Week 1 session | [weeks/week-01](weeks/week-01) |
| Week 1 notebook | [From numbers to a decision boundary](weeks/week-01/01-vectors-matrices-decision-boundaries.ipynb) |
| Week 1 Menti | [Menti build sheet](menti/week-01.md) |
| Teaching guide | [TEACHING.md](TEACHING.md) |

## Repository map

| Path | Purpose |
|---|---|
| `weeks/` | Complete weekly group-session packages |
| `menti/` | Exact questions, poll types, answers and timing |
| `mini_labs/` | Reusable 10-25 minute experiments |
| `datasets/` | Small documented teaching datasets |
| `shared/` | Plotting and notebook utilities |
| `exercises/` | Short unanswered problems and exam-style questions |
| `templates/` | Reusable structure for future sessions |
| `resources/` | Terminology and recommended links |
| `assets/` | Original figures used by notebooks |

## Current material

| Week | Theme | Material |
|---|---|---|
| 01 | Vectors, matrices and decision boundaries | Complete notebook, Menti and 90-minute plan |
| 02 | Search and optimization | Visual notebook foundation |
| 03 | kNN and supervised learning | Visual notebook foundation |
| 04 | Perceptron and linear regression | Planned |
| 05 | Evolutionary algorithms I | Planned |
| 06 | Evolutionary algorithms II | Planned |
| 07 | Logistic regression | Planned |
| 08 | Feed-forward networks and backpropagation | Planned |
| 09 | Unsupervised learning | Planned |
| 10 | CNN and general revision | Planned |

## Run in a browser

### GitHub Codespaces

Select **Code -> Codespaces -> Create codespace on main**. The included dev-container configuration installs the environment and Jupyter extension.

### Google Colab

Open a notebook through Colab by replacing its GitHub prefix with:

```text
https://colab.research.google.com/github/FinnTheHuman2412/in3050-in4050-F2026/blob/main/
```

For example, open the [Week 1 notebook in Colab](https://colab.research.google.com/github/FinnTheHuman2412/in3050-in4050-F2026/blob/main/weeks/week-01/01-vectors-matrices-decision-boundaries.ipynb).

## Run locally

```bash
git clone https://github.com/FinnTheHuman2412/in3050-in4050-F2026.git
cd in3050-in4050-F2026
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

Conda users can instead run:

```bash
conda env create -f environment.yml
conda activate in3050-in4050-f2026
jupyter lab
```

## Teaching rhythm

```text
predict -> vote -> discuss -> experiment -> break the model -> explain -> transfer
```

Each main notebook ends with:

- one deliberate failure case;
- one optional IN4050 extension;
- an exit ticket containing define, apply and diagnose questions.

## Public-repository policy

This is supplementary group-teaching material, not an official course repository. Official UiO pages take precedence. Do not publish mandatory-assignment solutions, exam solutions, student submissions, private TA notes, copyrighted lecture decks, personal data or credentials here.

Original code and prose are released under the MIT License. Third-party material retains its original ownership.
