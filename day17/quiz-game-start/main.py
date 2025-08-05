from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    qn_obj = Question(question['text'], question['answer'])
    question_bank.append(question)

print("===> hello")
print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    print(f"question number {quiz.qn_number}")
    quiz.next_question()

print("You have completed the Quiz")
print(f"your final score is  {quiz.score}")
