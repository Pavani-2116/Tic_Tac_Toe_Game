import tkinter as tk
from tkinter import ttk, messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("Helvetica", 24), padding=10)
        self.style.map("TButton",
            background=[('active', '#e0f7fa')],
            foreground=[('pressed', '#000')],
        )
        self.style.configure("Winner.TButton", background="#a5d6a7")

        self.current_player = "X"
        self.board = [""] * 9
        self.game_mode = None  # 'pvp' or 'ai'

        self.create_mode_selection()

    def create_mode_selection(self):
        self.clear_window()
        label = ttk.Label(self.root, text="Choose Game Mode", font=("Helvetica", 18, "bold"))
        label.pack(pady=40)

        btn1 = ttk.Button(self.root, text="Player vs Player", command=lambda: self.start_game("pvp"))
        btn1.pack(pady=10)

        btn2 = ttk.Button(self.root, text="Player vs Computer", command=lambda: self.start_game("ai"))
        btn2.pack(pady=10)

        exit_btn = ttk.Button(self.root, text="Exit", command=self.root.quit)
        exit_btn.pack(pady=20)

    def start_game(self, mode):
        self.game_mode = mode
        self.clear_window()
        self.setup_game_board()

    def setup_game_board(self):
        self.label = ttk.Label(self.root, text="Player X's Turn", font=("Helvetica", 18, "bold"))
        self.label.pack(pady=20)

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.board = [""] * 9
        self.buttons = []
        for i in range(9):
            btn = ttk.Button(self.frame, text="", command=lambda i=i: self.on_click(i), width=5)
            btn.grid(row=i//3, column=i%3, padx=10, pady=10)
            self.buttons.append(btn)

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=20)

        self.reset_btn = ttk.Button(btn_frame, text="Reset Game", command=self.reset_game)
        self.reset_btn.pack(side="left", padx=10)

        self.exit_btn = ttk.Button(btn_frame, text="Exit", command=self.root.quit)
        self.exit_btn.pack(side="right", padx=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def on_click(self, i):
        if self.board[i] != "":
            return

        self.board[i] = self.current_player
        self.buttons[i].config(text=self.current_player)

        if self.check_winner():
            self.label.config(text=f"Player {self.current_player} wins!")
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.disable_all_buttons()
            return
        elif "" not in self.board:
            self.label.config(text="Draw!")
            messagebox.showinfo("Game Over", "It's a Draw!")
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.label.config(text=f"Player {self.current_player}'s Turn")

        if self.game_mode == "ai" and self.current_player == "O":
            self.root.after(500, self.computer_move)

    def computer_move(self):
        available = [i for i in range(9) if self.board[i] == ""]
        if not available:
            return
        move = random.choice(available)
        self.on_click(move)

    def check_winner(self):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] != "":
                for idx in (a, b, c):
                    self.buttons[idx].config(style="Winner.TButton")
                return True
        return False

    def disable_all_buttons(self):
        for btn in self.buttons:
            btn.state(["disabled"])

    def reset_game(self):
        for btn in self.buttons:
            btn.config(text="", style="TButton")
            btn.state(["!disabled"])
        self.board = [""] * 9
        self.current_player = "X"
        self.label.config(text="Player X's Turn")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()