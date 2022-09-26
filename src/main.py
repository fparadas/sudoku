from sudoku import SudokuSolver
valid_sudoku = [
    5, -1, -1, 6, 7, -1, 9, -1, -1,
    -1, 4, -1, 8, -1, -1, -1, -1, -1,
    8, -1, -1, 5, -1, -1, 6, 1, 3,
    -1, 6, 2, 4, -1, -1, -1, 7, -1,
    1, -1, -1, -1, -1, 3, -1, 2, -1,
    3, 7, 4, 9, -1, 8, -1, -1, -1,
    -1, 9, 6, 1, -1, 7, 8, -1, 2,
    2, 1, 8, -1, -1, 6, -1, 4, 5,
    -1, 5,-1, -1, 8, -1, -1, 9, -1
    ]

if __name__ == "__main__":
    # starts with a valid solution to show that the solver works (heheheh)

    solver = SudokuSolver(valid_sudoku)
    print(solver.get_game(valid_sudoku))
    k = input("Press any key to see the solutions (if they exist): ")
    solutions = solver.get_solutions(solver.color())
    print(solutions)

    k = input("Press y to generate a new game: ")

    if k == 'y':
        
        while True:
            solver = SudokuSolver()
            game = solver.create_game(inplace=True)
            print(solver.get_game(game))
            k = input("Press any key to see the solutions (if they exist): ")
            solutions = solver.get_solutions(solver.color())
            print(solutions)
            k = input("Press y to generate a new game: ")

            if k != 'y':
                break
