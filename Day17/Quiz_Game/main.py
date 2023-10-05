from data import question_data
from question_model import Question

question_bank = []
for question_dict in question_data:
    # print(question_dict['text'])
    question_bank.append(Question(question_dict['text'], question_dict['answer']))

print(len(question_bank))
print(question_bank[8].text)
