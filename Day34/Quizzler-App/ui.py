from tkinter import *
from quiz_brain import  QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250, highlightthickness=0)
        self.quiz_text = self.canvas.create_text(
            150, 125,
            text="Quiz here",
            font=("Arial", 20, "italic"),
            fill="black",
            width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=self.false_image,
            command=self.false_check,
            bg=THEME_COLOR,
            highlightthickness=0)
        self.false_button.grid(row=2, column=0)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=self.true_image,
            command=self.true_check,
            bg=THEME_COLOR,
            highlightthickness=0)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.quiz_text, text=q_text)
        self.canvas.config(bg="white")

    def true_check(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_check(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
