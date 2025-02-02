from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print("Your final score was:", quiz.score, '/', len(quiz.question_list) )
