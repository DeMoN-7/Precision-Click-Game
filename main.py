import tkinter as tk
import random

class ClickTheTargetGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click the Target")
        self.root.geometry("600x400")

        self.score = 0
        self.time_left = 30
        self.target_radius = 30

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(self.root, text=f"Time Left: {self.time_left}", font=("Helvetica", 14))
        self.timer_label.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=600, height=300, bg="white")
        self.canvas.pack()

        self.start_game()

    def start_game(self):
        self.update_timer()
        self.create_target()

    def create_target(self):
        x = random.randint(self.target_radius, 600 - self.target_radius)
        y = random.randint(self.target_radius, 300 - self.target_radius)
        self.target = self.canvas.create_oval(
            x - self.target_radius, y - self.target_radius,
            x + self.target_radius, y + self.target_radius,
            fill="red", outline="black", width=2
        )
        self.canvas.tag_bind(self.target, "<Button-1>", self.target_clicked)
        self.root.after(3000, self.remove_target)

    def remove_target(self):
        self.canvas.delete(self.target)
        self.create_target()

    def target_clicked(self, event):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.canvas.delete(self.target)
        self.create_target()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time Left: {self.time_left}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.canvas.delete("all")
        self.timer_label.config(text="Game Over")
        self.score_label.config(text=f"Final Score: {self.score}")

root = tk.Tk()
game = ClickTheTargetGame(root)
root.mainloop()
