from tkinter import *
from quiz_brain import QuizBrain

FONT_SETTING = ("Arial", 20, "italic")
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score = Label(text=f"Score: {self.quiz.score}")
        self.score.config(bg=THEME_COLOR, fg="white", font=("Arial", 15, "normal"))
        self.score.grid(row=0, column=2)
        self.canvas = Canvas(height=250, width=300)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="x",
            width=280,
            font=FONT_SETTING,
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50)
        image1 = PhotoImage(file="./images/true.png")
        image2 = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=image1, width=100, height=97, highlightthickness=0,
                                  command=self.true)
        self.false_button = Button(image=image2, width=100, height=97, highlightthickness=0,
                                   command=self.false)
        self.true_button.grid(row=2, column=1)
        self.false_button.grid(row=2, column=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score["text"] = f"Score: {self.quiz.score}"
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def reset_bg(self):
        self.canvas.config(background="white")

    def true(self):
        self.feedback(self.quiz.check_answer(user_answer="true"))

    def false(self):
        self.feedback(self.quiz.check_answer(user_answer="false"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)
