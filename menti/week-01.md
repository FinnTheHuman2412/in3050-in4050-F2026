# Week 1 Menti: From numbers to decisions

Target time: 15-20 minutes distributed across the 90-minute session.

## Screen 1 - Welcome

- Type: Content slide
- Title: `IN3050/IN4050 - From numbers to decisions`
- Subtitle: `Group session 1`
- Say: Today is about making the mathematical words in the course concrete.

## Screen 2 - Background check

- Type: Scale, 1-5
- Question: `How comfortable are you using Python and NumPy?`
- Labels: `1 = completely new`, `5 = comfortable`
- Purpose: Decide how slowly to explain the code cells.

## Screen 3 - Course language

- Type: Word cloud
- Question: `Which AI or machine-learning term currently feels most like a black box?`
- Purpose: Collect terms to revisit during later sessions.

## Screen 4 - Vector or matrix?

- Type: Multiple choice
- Question: `We measure speed and strength for 100 creatures. What is the usual shape of the dataset X?`
- Options:
  - `(2, 100)`
  - `(100, 2)` - correct
  - `(100,)`
  - `(2,)`
- Follow-up: What does one row represent? What does one column represent?

## Screen 5 - Dot product

- Type: Quiz
- Question: `For x = [2, 4], w = [1, -1] and b = 0, what is w^T x + b?`
- Options:
  - `-2` - correct
  - `2`
  - `6`
  - `8`
- Follow-up: Which feature pushes the score upward, and which pushes it downward?

## Screen 6 - Move or rotate?

- Type: Multiple choice
- Question: `If we change only b, what happens to the decision boundary?`
- Options:
  - `It moves without rotating` - correct
  - `It rotates around the origin`
  - `It becomes curved`
  - `Nothing changes`
- Run the notebook experiment after revealing responses.

## Screen 7 - Diagnose the limitation

- Type: Multiple choice
- Question: `Why can one perceptron not solve XOR?`
- Options:
  - `XOR has too few data points`
  - `The classes are not linearly separable` - correct
  - `The features must be normalized`
  - `The bias must be zero`
- Follow-up: Changing weights can move or rotate a line, but cannot bend it.

## Screen 8 - Exit ticket

- Type: Open ended
- Question: `Explain a decision boundary in one sentence.`
- Look for: a rule or set of points separating prediction regions; ideally mention `w^T x + b = 0`.

## Optional final scale

- Type: Scale, 1-5
- Question: `Could you now explain the role of w and b to another student?`
