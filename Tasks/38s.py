import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = 'X'
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[None] * 3 for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text='', width=10, height=3, command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.buttons[row][col]['text'] == '' and not self.check_winner():
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner():
                tk.messagebox.showinfo("Победа!", f"Игрок {self.current_player} выиграл!")
            elif all(self.buttons[r][c]['text'] != '' for r in range(3) for c in range(3)):
                tk.messagebox.showinfo("Ничья", "Игра закончилась вничью!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != '':
                return True
        for col in range(3):
            if self.buttons[0][col]['text'] == self.buttons[1][col]['text'] == self.buttons[2][col]['text'] != '':
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            return True
        return False

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
