from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
count = 0

# ----------------------------- DATA PROCESSING ----------------------------- #
try:
    words_data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    words_data = pd.read_csv('data/french_words.csv')

words_to_learn = words_data.to_dict(orient='records')
current_word = {}


# ----------------------------- NEXT CARD ----------------------------- #
def countdown(seconds=3):
    global timer, count
    canvas.itemconfig(timer_text, text=f"{seconds}")
    if seconds > 0:
        timer = window.after(1000, countdown, seconds - 1)
    count += 1
    if count > 3:
        flip_card()


def next_card():
    global current_word, timer, count
    count = 0
    window.after_cancel(timer)
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(language_text, text="French", fill='black')
    canvas.itemconfig(word_text, text=current_word['French'], fill='black')
    canvas.itemconfig(canvas_image, image=front_image)
    countdown()


# ----------------------------- FLIP ----------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language_text, text="English", fill='White')
    canvas.itemconfig(timer_text, text="")
    canvas.itemconfig(word_text, text=current_word['English'], fill='White')


# ----------------------------- BUTTONS ----------------------------- #
def right_button():
    global current_word
    words_to_learn.remove(current_word)
    words_df = pd.DataFrame(words_to_learn)
    words_df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ----------------------------- UI SETUP ----------------------------- #
# GUI window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=(FONT_NAME, 60, "bold"))
timer_text = canvas.create_text(700, 80, text="3", fill="black", font=(FONT_NAME, 80, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=right_button, bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
