```python
"""
Sudoku Solver using Constraint Propagation

Steps:
1. Create candidate sets for empty cells.
2. Remove candidates already present in the same row, column, and 3x3 box.
3. Fill cells having only one candidate.
4. Apply hidden-single constraint propagation.
5. Repeat until no more progress is possible.
6. Use backtracking if constraint propagation alone cannot solve it.

Run:
    python sudoku_constraint_propagation.py
"""


# ---------------------------------------------------------
# Display Sudoku
# ---------------------------------------------------------

def print_board(board):
    print("\n+-------+-------+-------+")

    for r in range(9):
        print("|", end=" ")

        for c in range(9):
            value = board[r][c]

            if value == 0:
                print(".", end=" ")
            else:
                print(value, end=" ")

            if c % 3 == 2:
                print("|", end=" ")
        
        print()

        if r % 3 == 2:
            print("+-------+-------+-------+")


# ---------------------------------------------------------
# Find empty cells
# ---------------------------------------------------------

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c

    return None


# ---------------------------------------------------------
# Check whether a number is valid
# ---------------------------------------------------------

def is_valid(board, row, col, number):

    # Check row
    for c in range(9):
        if board[row][c] == number:
            return False

    # Check column
    for r in range(9):
        if board[r][col] == number:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == number:
                return False

    return True


# ---------------------------------------------------------
# Get candidates for a cell
# ---------------------------------------------------------

def get_candidates(board, row, col):

    candidates = set()

    for number in range(1, 10):
        if is_valid(board, row, col, number):
            candidates.add(number)

    return candidates


# ---------------------------------------------------------
# Create candidate table
# ---------------------------------------------------------

def create_candidates(board):

    candidates = {}

    for r in range(9):
        for c in range(9):

            if board[r][c] == 0:
                possible = get_candidates(board, r, c)

                # Empty candidate set means contradiction
                if len(possible) == 0:
                    return None

                candidates[(r, c)] = possible

    return candidates


# ---------------------------------------------------------
# Constraint Propagation - Naked Singles
# ---------------------------------------------------------

def apply_naked_singles(board):

    changed = False

    candidates = create_candidates(board)

    if candidates is None:
        return False, True

    for (r, c), possible in candidates.items():

        if len(possible) == 1:

            value = next(iter(possible))

            board[r][c] = value

            print(
                f"Naked Single: Row {r + 1}, "
                f"Column {c + 1} = {value}"
            )

            changed = True

    return changed, False


# ---------------------------------------------------------
# Constraint Propagation - Hidden Singles
# ---------------------------------------------------------

def apply_hidden_singles(board):

    candidates = create_candidates(board)

    if candidates is None:
        return False, True

    changed = False

    # ---------------------------------------------
    # Check rows
    # ---------------------------------------------

    for r in range(9):

        for number in range(1, 10):

            locations = []

            for c in range(9):

                if board[r][c] == 0:
                    if number in candidates[(r, c)]:
                        locations.append((r, c))

            if len(locations) == 1:

                row, col = locations[0]

                board[row][col] = number

                print(
                    f"Hidden Single in Row {r + 1}: "
                    f"Column {col + 1} = {number}"
                )

                changed = True

                return changed, False

    # ---------------------------------------------
    # Check columns
    # ---------------------------------------------

    for c in range(9):

        for number in range(1, 10):

            locations = []

            for r in range(9):

                if board[r][c] == 0:
                    if number in candidates[(r, c)]:
                        locations.append((r, c))

            if len(locations) == 1:

                row, col = locations[0]

                board[row][col] = number

                print(
                    f"Hidden Single in Column {c + 1}: "
                    f"Row {row + 1} = {number}"
                )

                changed = True

                return changed, False

    # ---------------------------------------------
    # Check 3x3 boxes
    # ---------------------------------------------

    for box_row in range(0, 9, 3):

        for box_col in range(0, 9, 3):

            for number in range(1, 10):

                locations = []

                for r in range(box_row, box_row + 3):

                    for c in range(box_col, box_col + 3):

                        if board[r][c] == 0:
                            if number in candidates[(r, c)]:
                                locations.append((r, c))

                if len(locations) == 1:

                    row, col = locations[0]

                    board[row][col] = number

                    print(
                        f"Hidden Single in Box "
                        f"({box_row // 3 + 1}, "
                        f"{box_col // 3 + 1}): "
                        f"Row {row + 1}, "
                        f"Column {col + 1} = {number}"
                    )

                    changed = True

                    return changed, False

    return changed, False


# ---------------------------------------------------------
# Constraint Propagation
# ---------------------------------------------------------

def constraint_propagation(board):

    print("\nStarting Constraint Propagation...")

    while True:

        changed, contradiction = apply_naked_singles(board)

        if contradiction:
            return False

        if changed:
            continue

        changed, contradiction = apply_hidden_singles(board)

        if contradiction:
            return False

        if not changed:
            break

    return True


# ---------------------------------------------------------
# Backtracking Solver
# ---------------------------------------------------------

def solve(board):

    # First apply constraint propagation
    if not constraint_propagation(board):
        return False

    # Check whether puzzle is solved
    empty = find_empty(board)

    if empty is None:
        return True

    row, col = empty

    candidates = get_candidates(board, row, col)

    # Try candidates one by one
    for number in sorted(candidates):

        board[row][col] = number

        print(
            f"Backtracking: Trying "
            f"{number} at Row {row + 1}, "
            f"Column {col + 1}"
        )

        if solve(board):
            return True

        # Undo choice
        board[row][col] = 0

    return False


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------

def main():

    # 0 represents an empty cell

    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],

        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],

        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("===================================")
    print(" Sudoku Constraint Propagation")
    print("===================================")

    print("\nInitial Sudoku:")
    print_board(board)

    if solve(board):

        print("\nSudoku Solved Successfully!")

        print_board(board)

    else:

        print("\nNo solution exists for this Sudoku.")


# ---------------------------------------------------------
# Run program
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
```
