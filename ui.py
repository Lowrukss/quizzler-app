from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TEXT_STYLE = "(Arial, 20, italic)"
STARING_SCORE = 0


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Press any button for first question",
                                                     fill="black",
                                                     font=("Arial", 10, "italic"))

        self.score = Label(text=f"Score: {STARING_SCORE}")
        self.score.grid(column=1, row=0)
        self.score.config(bg=THEME_COLOR, fg="white")

        self.true_image = PhotoImage(file="./images/true.png")
        self.true = Button(image=self.true_image, highlightthickness=0, command=self.correct_answer)
        self.true.grid(column=0, row=2, padx=20, pady=20)

        self.wrong_image = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=self.wrong_image, highlightthickness=0, command=self.false_answer)
        self.wrong.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have finnished the Quiz")
            self.true.config(state="disabled")
            self.wrong.config(state="disabled")

    def correct_answer(self):
        global STARING_SCORE
        if self.quiz.check_answer() == "True":
            STARING_SCORE += 1
            self.score.config(text=f"Score {STARING_SCORE}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def false_answer(self):
        global STARING_SCORE
        if self.quiz.check_answer() == "False":
            STARING_SCORE += 1
            self.score.config(text=f"Score {STARING_SCORE}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
