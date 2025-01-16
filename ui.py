import tkinter
from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TEXT_STYLE = "(Arial, 20, italic)"
STARTING_SCORE = 0


class App(tkinter.Tk):
    def __init__(self, quiz_brain):
        super().__init__()
        self.title("Quizzler Game")
        self.geometry("400x400")

        container = tkinter.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")

        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (StartWindow, QuizInterface, EndWindow):
            if f == QuizInterface:
                frame = f(container, self, quiz_brain)
            else:
                frame = f(container, self)

            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartWindow)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


class QuizInterface(tkinter.Frame):
    def __init__(self, parent, controller, quiz_brain: QuizBrain):
        super().__init__(parent)
        self.quiz = quiz_brain
        self.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(self, width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Press any button for the first question",
            fill="black", font=("Arial", 10, "italic")
        )

        self.score_label = Label(self, text=f"Score: {STARTING_SCORE}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.score_label.config(bg=THEME_COLOR, fg="white")

        self.true_button = Button(self, text="True", command=self.correct_answer)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        self.false_button = Button(self, text="False", command=self.false_answer)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have finished the Quiz! Your score is:"
                                                            f"{STARTING_SCORE}/{10}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct_answer(self):
        global STARTING_SCORE
        if self.quiz.check_answer() == "True":
            STARTING_SCORE += 1
            self.score_label.config(text=f"Score: {STARTING_SCORE}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.after(1000, self.get_next_question)

    def false_answer(self):
        global STARTING_SCORE
        if self.quiz.check_answer() == "False":
            STARTING_SCORE += 1
            self.score_label.config(text=f"Score: {STARTING_SCORE}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.after(1000, self.get_next_question)


class StartWindow(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)  # Add space at the top
        self.grid_rowconfigure(1, weight=1)  # Center the content vertically
        self.grid_rowconfigure(2, weight=1)  # Add space at the bottom
        self.grid_columnconfigure(0, weight=1)  # Center the content horizontally

        # Title label
        label = tkinter.Label(self, text="Welcome to Quizzler!", font=("Arial", 24))
        label.grid(row=0, column=0, padx=20, pady=20)

        # Start button
        start_button = ttk.Button(self, text="Start Quiz",
                                  command=lambda: controller.show_frame(QuizInterface))
        start_button.grid(row=1, column=0, padx=20, pady=20)


class EndWindow(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tkinter.Label(self, text="Thanks for playing!", font=("Arial", 18))
        label.grid(row=0, column=0, padx=20, pady=20)

        quit_button = ttk.Button(self, text="Quit", command=controller.quit)
        quit_button.grid(row=1, column=0, padx=20, pady=20)
