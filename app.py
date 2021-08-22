from tkinter import *
from tkinter import ttk, messagebox
from ui import QuizInterface
from quiz_brain import QuizBrain
from data import DataProcess
from question_model import Question

THEME_COLOR = "#375362"


class App(Tk):

    def __init__(self):
        self.quiz = None
        self.number_of_questions = 0
        self.difficulty_level = ""
        self.category = ""
        self.quiz_process = None
        self.quiz_data = None
        self.quiz_ = None

        super().__init__()
        self.title("Quizler")
        self.resizable(False, False)
        self.config(bg=THEME_COLOR, padx=20, pady=20)

        # Setting up labels
        self.number_of_questions_label = Label(self, text="Number of questions:", bg=THEME_COLOR)
        self.number_of_questions_label.grid(row=0, column=1, pady=10, padx=10)
        self.select_category_label = Label(self, text="Select Category:", bg=THEME_COLOR)
        self.select_category_label.grid(row=1, column=1, padx=10, pady=10)
        self.select_difficulty_label = Label(self, text="Select Difficulty:", bg=THEME_COLOR)
        self.select_difficulty_label.grid(row=2, column=1, padx=10, pady=10)
        # Setting up the entry
        self.number_of_questions_entry = Entry(self, width=35, bg="white", fg="black")
        self.number_of_questions_entry.insert(index=0, string="10")
        self.number_of_questions_entry.grid(row=0, column=2)
        # Setting up Category and difficult combo box
        n = StringVar()
        s = StringVar()
        self.select_category_combo_box = ttk.Combobox(self, width=34, textvariable=n)
        self.select_category_combo_box["values"] = (
            "General Knowledge",
            "Entertainment: Books",
            "Entertainment: Film",
            "Entertainment: Music",
            "Entertainment: Musicals & Theatres",
            "Entertainment: Television",
            "Entertainment: Video Games",
            "Entertainment: Board Games",
            "Science & Nature",
            "Science: Computers",
            "Science: Mathematics",
            "Mythology",
            "Sports",
            "Geography",
            "History",
            "Politics",
            "Art",
            "Celebrities",
            "Animals",
            "Vehicles",
            "Entertainment: Comics",
            "Science: Gadgets",
            "Entertainment: Japanese Anime & Manga",
            "Entertainment: Cartoon & Animations"
        )
        self.select_category_combo_box["state"] = "readonly"
        self.select_category_combo_box.grid(row=1, column=2)
        self.select_category_combo_box.current(1)

        self.select_difficulty_combo_box = ttk.Combobox(self, width=34, textvariable=s)
        self.select_difficulty_combo_box["values"] = ("Easy", "Medium", "Hard")
        self.select_difficulty_combo_box["state"] = "readonly"
        self.select_difficulty_combo_box.grid(row=2, column=2)
        self.select_difficulty_combo_box.current(1)
        # Generating button
        self.generate_button = Button(self, text="Start Quiz", command=self.open_quiz)
        self.generate_button.grid(row=3, column=0, pady=10)

    def open_quiz(self):
        self.quiz_ = self.save_file()
        if self.quiz_:
            window = QuizInterface(self, self.quiz_)
            window.grab_set()

    def save_file(self):
        # Getting the Values in the text box and combo box
        if len(self.number_of_questions_entry.get()) > 0 and len(self.select_difficulty_combo_box.get()) > 0 and len(
                self.select_category_combo_box.get()) > 0:

            # if the number of questions is a number
            try:
                self.number_of_questions = int(self.number_of_questions_entry.get())
            except ValueError:
                messagebox.showerror(title="error", message="Please number of questions should be a number")
            else:
                self.difficulty_level = self.select_difficulty_combo_box.get().lower()
                self.category = self.select_category_combo_box.get()

                self.quiz_process = DataProcess(amount=self.number_of_questions,
                                                difficulty=self.difficulty_level,
                                                category=self.category)

                self.quiz_data, self.response_code = self.quiz_process.loading_quiz()

                question_bank = []

                if self.response_code == 0:
                    for question in self.quiz_data:
                        question_text = question["question"]
                        question_answer = question["correct_answer"]
                        new_question = Question(question_text, question_answer)
                        question_bank.append(new_question)

                    self.quiz = QuizBrain(question_bank)

                    return self.quiz
                else:
                    messagebox.showerror(title="Error", message="No questions found in the Database"
                                                                "Please select again")
        else:
            messagebox.showerror(title="Error", message="Please fields should not be empty")


