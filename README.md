# Sudoku-Solver
# Sudoku Solver Using Constraint Propagation

A Python-based Sudoku Solver that uses **Constraint Propagation** to reduce possible values for empty cells and solve the puzzle efficiently. The solver applies **Naked Singles** and **Hidden Singles** before using **Backtracking** when necessary.

---

## 📌 Project Overview

Sudoku is a logic-based number-placement puzzle consisting of a **9 × 9 grid** divided into nine **3 × 3 subgrids**.

The objective is to fill every empty cell with a number from **1 to 9** while satisfying these constraints:

* Each row must contain numbers 1–9 without repetition.
* Each column must contain numbers 1–9 without repetition.
* Each 3 × 3 box must contain numbers 1–9 without repetition.

This project implements a Sudoku solver using **Constraint Propagation**, an important technique used in Artificial Intelligence and Constraint Satisfaction Problems (CSPs).

The program first eliminates impossible values from empty cells and repeatedly applies logical deductions. If constraint propagation cannot completely solve the puzzle, the program uses backtracking to find the remaining solution.

---

## 🎯 Objectives

The main objectives of this project are:

1. To develop a Sudoku solver using Python.
2. To understand the concept of **Constraint Satisfaction Problems (CSPs)**.
3. To implement constraint propagation for solving Sudoku.
4. To generate possible candidate values for empty cells.
5. To implement **Naked Single** detection.
6. To implement **Hidden Single** detection.
7. To reduce the Sudoku search space before backtracking.
8. To demonstrate how Artificial Intelligence techniques can solve logic puzzles.
9. To provide a simple and understandable implementation suitable for academic mini-projects.

---

## 🧠 Concepts Used

### 1. Constraint Satisfaction Problem

Sudoku can be modeled as a Constraint Satisfaction Problem.

Each empty Sudoku cell is treated as a **variable**.

The possible values of that cell form its **domain**.

The Sudoku rules act as **constraints**.

For example:

```text
Variable: X[1][3]

Domain:
{1, 2, 4, 6, 7, 8, 9}

Constraints:
- Cannot duplicate a number in the row
- Cannot duplicate a number in the column
- Cannot duplicate a number in the 3×3 box
```

---

## 🔍 Constraint Propagation

Constraint propagation removes values from a cell's domain whenever those values violate Sudoku constraints.

For every empty cell, the program checks:

```text
Row constraints
       +
Column constraints
       +
3 × 3 Box constraints
       ↓
Possible Candidate Values
```

For example, if an empty cell has:

```text
Candidates = {2, 5, 7}
```

and the constraints eliminate `2` and `7`, then:

```text
Candidates = {5}
```

Therefore:

```text
Cell = 5
```

This is called a **Naked Single**.

---

## 🔢 Naked Singles

A Naked Single occurs when an empty cell has only one possible candidate.

Example:

```text
Cell Candidates = {7}
```

Therefore:

```text
Cell = 7
```

The program automatically fills such cells.

---

## 🔎 Hidden Singles

A Hidden Single occurs when a particular number can appear in only one empty cell within a row, column, or 3 × 3 box.

For example:

```text
Row:

5 3 . | . 7 . | . . .
```

Suppose the number `4` can legally appear in only one of the empty cells in that row.

Then:

```text
That cell = 4
```

even if the cell has other candidates.

---

## 🔄 Algorithm

The overall algorithm is:

### Step 1: Read the Sudoku

The Sudoku puzzle is represented as a 9 × 9 Python list.

```text
0 = Empty Cell
1–9 = Given Number
```

---

### Step 2: Find Empty Cells

The program scans the board and identifies cells containing `0`.

---

### Step 3: Generate Candidates

For every empty cell:

```text
Candidates = {1,2,3,4,5,6,7,8,9}
```

The program removes numbers already present in:

* The same row
* The same column
* The same 3 × 3 box

---

### Step 4: Apply Naked Singles

If a cell has only one candidate:

```text
Candidates = {X}
```

the program assigns:

```text
Cell = X
```

---

### Step 5: Apply Hidden Singles

The program checks:

* Every row
* Every column
* Every 3 × 3 box

If a number has only one possible location, that number is placed there.

---

### Step 6: Repeat Constraint Propagation

The program continues applying:

```text
Naked Singles
       ↓
Hidden Singles
       ↓
Update Candidates
       ↓
Naked Singles
       ↓
Hidden Singles
```

until no further progress can be made.

---

### Step 7: Backtracking

If some cells remain empty, the solver selects a candidate and temporarily assigns it.

If the assignment produces a contradiction, it is undone and another candidate is tried.

---

### Step 8: Solution

When there are no empty cells remaining, the Sudoku is solved.

---

# 📊 Flowchart

```text
                 ┌──────────────────┐
                 │      START       │
                 └────────┬─────────┘
                          │
                          ▼
                ┌────────────────────┐
                │  Read Sudoku Grid  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │   Find Empty Cell  │
                └─────────┬──────────┘
                          │
                          ▼
              ┌──────────────────────────┐
              │ Generate Candidate Values│
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │     Naked Single?        │
              └────────────┬─────────────┘
                           │
                    ┌──────┴──────┐
                   YES            NO
                    │              │
                    ▼              ▼
            ┌──────────────┐  ┌──────────────────┐
            │ Fill the Cell│  │  Hidden Single?  │
            └───────┬──────┘  └────────┬─────────┘
                    │                  │
                    │            ┌─────┴─────┐
                    │           YES          NO
                    │            │             │
                    │            ▼             ▼
                    │      ┌────────────┐  ┌──────────────┐
                    │      │ Fill Cell  │  │ More Empty   │
                    │      └──────┬─────┘  │ Cells?       │
                    │             │        └──────┬───────┘
                    │             │               │
                    └─────────────┴───────┐  ┌────┴────┐
                                          │ YES       NO
                                          │   │        │
                                          ▼   │        ▼
                              ┌──────────────┐│  ┌────────────┐
                              │ Repeat       ││  │   SOLVED   │
                              │ Propagation  ││  └────────────┘
                              └──────┬───────┘│
                                     │        │
                                     └────────┘
                                          │
                                          ▼
                                ┌─────────────────┐
                                │   Backtracking  │
                                └────────┬────────┘
                                         │
                                         ▼
                                ┌─────────────────┐
                                │ Valid Candidate?│
                                └───────┬─────────┘
                                        │
                                  ┌─────┴─────┐
                                 YES          NO
                                  │            │
                                  ▼            ▼
                           ┌────────────┐  ┌──────────┐
                           │ Continue   │  │ Try Next │
                           │ Solving    │  │ Candidate│
                           └──────┬─────┘  └────┬─────┘
                                  │              │
                                  └──────────────┘
```

---

# 🛠️ Requirements

## Software Requirements

* Python 3.x
* Git
* GitHub account
* Any Python-compatible IDE or text editor

### Recommended IDEs

* Visual Studio Code
* PyCharm
* IDLE
* Jupyter Notebook

---

## Hardware Requirements

The project has very low hardware requirements.

| Component        | Requirement             |
| ---------------- | ----------------------- |
| Processor        | Any modern processor    |
| RAM              | 2 GB or more            |
| Storage          | Less than 100 MB        |
| Operating System | Windows / Linux / macOS |

---

# 📁 Project Structure

```text
sudoku-constraint-propagation/
│
├── sudoku_constraint_propagation.py
│
├── README.md
│
└── screenshots/
    ├── initial_sudoku.png
    ├── solving_steps.png
    └── solved_sudoku.png
```

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/sudoku-constraint-propagation.git
```

---

## 2. Open the Project Folder

```bash
cd sudoku-constraint-propagation
```

---

## 3. Run the Python Program

```bash
python sudoku_constraint_propagation.py
```

If your system uses `python3`:

```bash
python3 sudoku_constraint_propagation.py
```

---

# 🧪 Sample Input

The program contains the following Sudoku puzzle:

```text
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```

`.` represents an empty cell.

---

# 💻 Sample Output

```text
===================================
 Sudoku Constraint Propagation
===================================

Initial Sudoku:

+-------+-------+-------+
| 5 3 . | . 7 . | . . . |
| 6 . . | 1 9 5 | . . . |
| . 9 8 | . . . | . 6 . |
+-------+-------+-------+
| 8 . . | . 6 . | . . 3 |
| 4 . . | 8 . 3 | . . 1 |
| 7 . . | . 2 . | . . 6 |
+-------+-------+-------+
| . 6 . | . . . | 2 8 . |
| . . . | 4 1 9 | . . 5 |
| . . . | . 8 . | . 7 9 |
+-------+-------+-------+

Starting Constraint Propagation...

Naked Single: Row 5, Column 5 = 5
Hidden Single in Row 5: Column 2 = 2
...

Sudoku Solved Successfully!

+-------+-------+-------+
| 5 3 4 | 6 7 8 | 9 1 2 |
| 6 7 2 | 1 9 5 | 3 4 8 |
| 1 9 8 | 3 4 2 | 5 6 7 |
+-------+-------+-------+
| 8 5 9 | 7 6 1 | 4 2 3 |
| 4 2 6 | 8 5 3 | 7 9 1 |
| 7 1 3 | 9 2 4 | 8 5 6 |
+-------+-------+-------+
| 9 6 1 | 5 3 7 | 2 8 4 |
| 2 8 7 | 4 1 9 | 6 3 5 |
| 3 4 5 | 2 8 6 | 1 7 9 |
+-------+-------+-------+
```

> Note: The exact sequence of displayed solving steps can vary depending on the implementation.

---

# 📸 Screenshots

Screenshots can be added to demonstrate the working of the project.

## Initial Sudoku

Add a screenshot showing the Sudoku before solving.

Save the image as:

```text
screenshots/initial_sudoku.png
```

Then add:

```markdown
![Initial Sudoku](screenshots/initial_sudoku.png)
```

---

## Constraint Propagation Steps

Add a screenshot showing the candidate elimination and solving steps.

Save the image as:

```text
screenshots/solving_steps.png
```

Then add:

```markdown
![Constraint Propagation Steps](screenshots/solving_steps.png)
```

---

## Final Sudoku

Add a screenshot showing the completed Sudoku.

Save the image as:

```text
screenshots/solved_sudoku.png
```

Then add:

```markdown
![Solved Sudoku](screenshots/solved_sudoku.png)
```

---

# 📈 Method Used

The solver combines two major techniques:

### Constraint Propagation

Used to logically reduce the possible values of empty cells.

```text
Sudoku
   ↓
Generate Candidates
   ↓
Remove Invalid Values
   ↓
Naked Singles
   ↓
Hidden Singles
   ↓
Repeat
```

### Backtracking

Used when logical constraint propagation cannot completely solve the puzzle.

```text
Choose Candidate
      ↓
Try Candidate
      ↓
Valid?
 ┌────┴────┐
YES        NO
 │          │
 ▼          ▼
Continue   Undo
            ↓
       Try Another
```

---

# ⏱️ Complexity

The worst-case time complexity of a Sudoku solver using backtracking can be exponential because it may need to explore many possible assignments.

Constraint propagation helps reduce the search space before backtracking.

Therefore, the practical solving process is:

```text
Constraint Propagation
          ↓
Reduced Search Space
          ↓
Backtracking
          ↓
Solution
```

---

# 🤖 Artificial Intelligence Perspective

This project demonstrates concepts from Artificial Intelligence, particularly:

* Constraint Satisfaction Problems
* Domain Reduction
* Constraint Propagation
* Search
* Backtracking
* Logical Inference

Sudoku is a good example of a CSP because each empty cell has a domain of possible values and the Sudoku rules define relationships between those variables.

---

# 🌟 Features

* ✅ 9 × 9 Sudoku support
* ✅ Candidate generation
* ✅ Row constraint checking
* ✅ Column constraint checking
* ✅ 3 × 3 box constraint checking
* ✅ Naked Single detection
* ✅ Hidden Single detection
* ✅ Constraint propagation
* ✅ Backtracking
* ✅ Console-based output
* ✅ Beginner-friendly Python implementation

---

# 🔮 Future Enhancements

The project can be extended with:

1. Graphical User Interface (GUI)
2. Sudoku puzzle input from the user
3. Difficulty-level selection
4. Step-by-step visualization
5. Candidate display inside cells
6. Sudoku puzzle generator
7. Multiple Sudoku sizes
8. Performance comparison between algorithms
9. Minimum Remaining Values (MRV) heuristic
10. Arc Consistency techniques
11. Web-based Sudoku solver
12. Interactive solving animation

---

# 📚 Applications

Constraint propagation techniques are useful beyond Sudoku.

They can be applied to:

* Scheduling
* Timetabling
* Resource allocation
* Planning
* Logic puzzles
* Configuration problems
* Route planning
* Assignment problems
* Artificial Intelligence search problems

---

# 🎓 Educational Value

This project is suitable for:

* AI Mini Projects
* Python Mini Projects
* Constraint Satisfaction Problem demonstrations
* Artificial Intelligence laboratory work
* Academic project demonstrations
* Beginner AI projects

---

# 👨‍💻 Author

**Your Name**

GitHub:

```text
https://github.com/YOUR_USERNAME
```

---

# 📄 License

This project is open-source and available for educational purposes.

You can modify and improve the code according to your requirements.

---

# ⭐ Acknowledgment

This project was developed to demonstrate how **Constraint Propagation and Backtracking** can be used to solve Sudoku as a Constraint Satisfaction Problem.

If you find this project useful, consider giving the repository a ⭐ on GitHub.
