from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface(Toplevel):
    def __init__(self, parent, quiz_process: QuizBrain):
        self.quiz = quiz_process
        super().__init__(parent)
        self.title("Quizzler")
        self.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(self, width=300, height=250, bg="white", highlightthickness=0)
        self.text_question = self.canvas.create_text(150, 125, width=280, text="Hello",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, columnspan=2, pady=20)

        self.score_label = Label(self, text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, pady=20)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(self, image=self.true_image, highlightthickness=0, bg=THEME_COLOR,
                                  command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(self, image=self.false_image, highlightthickness=0, bg=THEME_COLOR,
                                   command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_question, text=q_text)
        else:
            self.canvas.itemconfig(self.text_question, text="You have reached the end of the quiz Thank You!!!")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.after(1000, self.get_next_question)

