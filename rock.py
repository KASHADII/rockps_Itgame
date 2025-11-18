import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("350x450")

hscore = 0
cscore = 0

# Labels
score_label = tk.Label(root, text=f"Your Score: {hscore}   Computer Score: {cscore}", font=("Arial", 14))
score_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=20)

choice_label = tk.Label(root, text="", font=("Arial", 12))
choice_label.pack(pady=10)

# Game Logic
def play(user_choice):
    global hscore, cscore

    computer_choice = random.randint(1, 3)

    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    choice_label.config(text=f"You: {choices[user_choice]}   |   Computer: {choices[computer_choice]}")

    # Checking winner
    if (user_choice == 1 and computer_choice == 3) or \
       (user_choice == 2 and computer_choice == 1) or \
       (user_choice == 3 and computer_choice == 2):
        hscore += 1
        result_label.config(text="You won the round!", fg="green")

    elif user_choice == computer_choice:
        result_label.config(text="It's a draw!", fg="blue")

    else:
        cscore += 1
        result_label.config(text="Computer won the round!", fg="red")

    score_label.config(text=f"Your Score: {hscore}   Computer Score: {cscore}")

    # Check for winner
    if hscore == 5:
        result_label.config(text="🎉 YOU WON THE GAME 🎉", fg="green")
        disable_buttons()

    elif cscore == 5:
        result_label.config(text="💀 COMPUTER WON THE GAME 💀", fg="red")
        disable_buttons()


def disable_buttons():
    rock_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")

# Buttons
rock_btn = tk.Button(root, text="Rock", font=("Arial", 14), width=12, command=lambda: play(1))
paper_btn = tk.Button(root, text="Paper", font=("Arial", 14), width=12, command=lambda: play(2))
scissors_btn = tk.Button(root, text="Scissors", font=("Arial", 14), width=12, command=lambda: play(3))

rock_btn.pack(pady=10)
paper_btn.pack(pady=10)
scissors_btn.pack(pady=10)

root.mainloop()
