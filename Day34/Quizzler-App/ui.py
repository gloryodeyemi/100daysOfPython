from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250, highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, text="Quiz here", font=("Arial", 20, "italic"), fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, bg=THEME_COLOR, highlightthickness=0)
        self.right_button.grid(row=2, column=0)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, bg=THEME_COLOR, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()
