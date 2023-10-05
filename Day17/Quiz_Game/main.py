from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question_dict in question_data:
    question_bank.append(Question(question_dict['text'], question_dict['answer']))

quiz = QuizBrain(question_bank)
quiz.next_question()
