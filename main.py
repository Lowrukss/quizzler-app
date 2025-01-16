from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface, App

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quizbrain = QuizBrain(question_bank)
#quiz_ui = QuizInterface(quiz)
quiz_ui = App(quizbrain)
quiz_ui.mainloop()



