import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x555")
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        self.title_label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.frame, text="", font=("Arial", 20), width=6, height=3,
                          command=lambda idx=i: self.click(idx))
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)
        
        self.status_label = tk.Label(root, text=f"Current Player: {self.current_player}", 
                                     font=("Arial", 14))
        self.status_label.pack(pady=10)
        
        self.reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12),
                                  command=self.reset_game)
        self.reset_btn.pack(pady=5)
    
    def click(self, index):
        if self.board[index] == "" and not self.game_over:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.game_over = True
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Current Player: {self.current_player}")
    
    def check_winner(self):
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]              
        ]
        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        for btn in self.buttons:
            btn.config(text="")
        self.status_label.config(text=f"Current Player: {self.current_player}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
