from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question_dict in question_data:
    question_bank.append(Question(question_dict['question'], question_dict['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Congratulations!!! You have completed the quiz\nYour final score is: {quiz.score}/{quiz.question_number}")
