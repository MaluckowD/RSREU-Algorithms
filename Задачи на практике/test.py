import tkinter as tk
import random
from collections import deque

class FifteenPuzzle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()
        self.empty_row, self.empty_col = self.find_empty()
        self.moves = 0

    def generate_board(self):
        numbers = list(range(1, self.size * self.size)) + [0]
        random.shuffle(numbers)
        return [numbers[i:i + self.size] for i in range(0, self.size * self.size, self.size)]

    def find_empty(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    return row, col

    def move(self, direction):
        new_row, new_col = self.empty_row, self.empty_col

        if direction == "up" and self.empty_row > 0:
            new_row -= 1
        elif direction == "down" and self.empty_row < self.size - 1:
            new_row += 1
        elif direction == "left" and self.empty_col > 0:
            new_col -= 1
        elif direction == "right" and self.empty_col < self.size - 1:
            new_col += 1
        else:
            return False

        self.board[self.empty_row][self.empty_col] = self.board[new_row][new_col]
        self.board[new_row][new_col] = 0
        self.empty_row, self.empty_col = new_row, new_col
        self.moves += 1
        self.update_board_display()
        return True

    def is_solved(self):
        target = [[i + 1 + j * self.size for i in range(self.size)] for j in range(self.size)]
        target[-1][-1] = 0
        return self.board == target

    def get_possible_moves(self):
        moves = ["up", "down", "left", "right"]
        possible_moves = []
        for move in moves:
            if self.move(move):
                possible_moves.append(move)
                self.move(move)  # Отменяем ход
        return possible_moves

    def update_board_display(self):
        for i in range(self.size):
            for j in range(self.size):
                button = self.app.buttons[i][j]  # Доступ к buttons через app
                value = self.board[i][j]
                if value == 0:
                    button.config(text="")
                else:
                    button.config(text=value)

    def reset_moves(self):
        self.moves = 0
        self.app.update_moves_display()  # Доступ к update_moves_display через app

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("15-Puzzle")
        self.puzzle = FifteenPuzzle()
        self.create_widgets()

    def create_widgets(self):
        # Создаем поле 4x4 для игры
        self.buttons = []
        for i in range(self.puzzle.size):
            row = []
            for j in range(self.puzzle.size):
                button = tk.Button(self, text="", width=5, height=2, command=lambda row=i, col=j: self.handle_button_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        self.puzzle.app = self  # Передаем ссылку на App в FifteenPuzzle
        self.puzzle.update_board_display()

        # Панель с кнопками
        button_frame = tk.Frame(self)
        button_frame.grid(row=self.puzzle.size + 1, columnspan=self.puzzle.size)

        # Кнопка сброса
        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_puzzle)
        reset_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Кнопка старта
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_solving, state=tk.DISABLED)
        self.start_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Кнопки выбора алгоритма
        self.algorithm_var = tk.StringVar(self.start_button)
        self.algorithm_var.set("BFS")
        bfs_button = tk.Radiobutton(button_frame, text="BFS", variable=self.algorithm_var, value="BFS")
        bfs_button.pack(side=tk.LEFT, padx=5, pady=5)
        dfs_button = tk.Radiobutton(button_frame, text="DFS", variable=self.algorithm_var, value="DFS")
        dfs_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Подпись количества ходов
        self.moves_label = tk.Label(button_frame, text=f"Moves: {self.puzzle.moves}")
        self.moves_label.pack(side=tk.LEFT, padx=5, pady=5)

    def update_moves_display(self):
        self.moves_label.config(text=f"Moves: {self.puzzle.moves}")

    def handle_button_click(self, row, col):
        if self.puzzle.move((row, col)):
            self.update_moves_display()
            if self.puzzle.is_solved():
                self.start_button.config(state=tk.DISABLED)
                tk.messagebox.showinfo("Победа!", "Вы решили головоломку!")

    def reset_puzzle(self):
        self.puzzle = FifteenPuzzle()
        self.puzzle.app = self
        self.puzzle.update_board_display()
        self.puzzle.reset_moves()
        self.start_button.config(state=tk.NORMAL)

    def start_solving(self):
        self.start_button.config(state=tk.DISABLED)
        algorithm = self.algorithm_var.get()
        if algorithm == "BFS":
            solution, depth = bfs_solve(self.puzzle)
        else:
            solution, depth = dfs_solve(self.puzzle, max_depth=20)
        if solution:
            for move in solution:
                self.after(500, lambda move=move: self.puzzle.move(move))
            self.after(depth * 500 + 500, lambda: self.start_button.config(state=tk.NORMAL))
        else:
            self.start_button.config(state=tk.NORMAL)
            tk.messagebox.showinfo("Ошибка!", "Решения не найдено!")

def bfs_solve(puzzle):
    visited = set()
    queue = deque([(puzzle, [], 0)])  # (Состояние, Последовательность ходов, Глубина)

    while queue:
        state, moves, depth = queue.popleft()
        if state.is_solved():
            return moves, depth

        if str(state.board) not in visited:
            visited.add(str(state.board))
            for move in state.get_possible_moves():
                new_state = FifteenPuzzle(state.board[:])
                new_state.move(move)
                new_state.app = puzzle.app  # Передаем ссылку на App 
                queue.append((new_state, moves + [move], depth + 1))

    return None, None  # Решения не найдено

def dfs_solve(puzzle, moves=None, max_depth=100):
    moves = moves or []
    visited = set()
    visited.add(str(puzzle.board))
    depth = len(moves)

    if puzzle.is_solved():
        return moves, depth

    if depth < max_depth:
        for move in puzzle.get_possible_moves():
            new_state = FifteenPuzzle(puzzle.board[:])
            new_state.move(move)
            new_state.app = puzzle.app  # Передаем ссылку на App
            if str(new_state.board) not in visited:
                visited.add(str(new_state.board))
                result, result_depth = dfs_solve(new_state, moves + [move], max_depth)
                if result:
                    return result, result_depth

    return None, None  # Решения не найдено

if __name__ == "__main__":
    app = App()