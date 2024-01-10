from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    countdown(int(0.5 * 60))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0 or count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f'{count_minute}:{count_seconds}')
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.config(padx=10, pady=10)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
start_button.config(padx=5, pady=5)
start_button.grid(column=0, row=2)

check_label = Label(text="✅︎", bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_label.config(padx=5, pady=5)
check_label.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
reset_button.config(padx=5, pady=5)
reset_button.grid(column=2, row=2)

window.mainloop()
