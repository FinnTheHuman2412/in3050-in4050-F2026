# IN3050 / IN4050 - Group Sessions

Student-facing material for the University of Oslo course **Introduction to Artificial Intelligence and Machine Learning**.

Each group session turns an abstract idea into something students can **see, change, break, and explain**.

## Start here

1. Install the environment.
2. Open the notebook for the current week.
3. Predict what will happen before running each experiment.
4. Change one parameter and explain the result.
5. Finish the exit ticket without looking up the answer.

The first notebook is [vectors, matrices and decision boundaries](weeks/week-01/01-vectors-matrices-decision-boundaries.ipynb). For a shorter experiment, try the [decision-boundary playground](mini_labs/decision-boundary-playground.ipynb).

## Repository map

| Path | Purpose |
|---|---|
| `weeks/` | Full weekly group-session notebooks |
| `mini_labs/` | Reusable 10-25 minute visual experiments |
| `datasets/` | Small documented teaching datasets |
| `shared/` | Plotting and notebook utilities |
| `exercises/` | Short problems and exam-style transfer questions |
| `resources/` | Terminology, formula sheets and recommended links |
| `assets/` | Images and figures used by notebooks |

Full assignment and exam solutions are deliberately not stored in this public repository.

## Learning arc

The notebooks are designed as one connected story:

```text
vectors and matrices
        -> search spaces and fitness
        -> exploration vs exploitation
        -> linear decision boundaries
        -> probability and loss
        -> overfitting and evaluation
        -> nonlinear models and neural networks
```

## Weekly roadmap

| Week | Theme | Status |
|---|---|---|
| 01 | Vectors, matrices and linear decision boundaries | Starter ready |
| 02 | Search, optimization and problem formulation | Planned |
| 03 | Hill climbing, simulated annealing and genetic algorithms | Planned |
| 04 | Supervised-learning foundations | Planned |
| 05 | Linear regression and gradient descent | Planned |
| 06 | Logistic regression and classification | Planned |
| 07 | Train, validation, test and feature scaling | Planned |
| 08 | Multiclass classification | Planned |
| 09 | Neural networks and nonlinear boundaries | Planned |
| 10 | Backpropagation and training | Planned |
| 11 | Unsupervised learning | Planned |
| 12 | Reinforcement learning | Planned |
| 13 | Exam synthesis and review | Planned |

The roadmap can be adjusted when the official Autumn 2026 teaching sequence is final.

## Run locally

Python 3.11 is recommended.

### `venv`

```bash
python -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

### Conda

```bash
conda env create -f environment.yml
conda activate in3050-in4050-f2026
jupyter lab
```

## Teaching principle

Every notebook should follow the same rhythm:

1. Present one concrete question.
2. Ask students to predict the outcome.
3. Build the simplest useful model.
4. Change one parameter.
5. Deliberately expose a failure case.
6. Name the concept that explains the result.
7. Transfer it to an exam-style question.

See [TEACHING.md](TEACHING.md) for the 105-minute session template and preparation checklist.

## Course and copyright note

This is supplementary group-teaching material, not an official course repository. Official UiO announcements, curriculum and deadlines take precedence. Do not commit copyrighted lecture slides, solution manuals, student submissions, personal data, API keys or credentials.

## License

Original code and prose are released under the MIT License. Third-party material retains its original ownership.
