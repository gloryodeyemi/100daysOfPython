from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo


def quiz_game():
    print(logo)  # display the quiz game art

    difficulty_level = input("Choose the quiz difficulty level (Easy/Medium/Hard): ").lower()
    question_bank = []  # list to store all the Question objects
    q_data = []  # empty list to store question data

    correct_input = False  # set initial value of input

    # keep asking for input if input is invalid
    while not correct_input:
        if difficulty_level == 'easy':
            q_data = question_data[0]
            correct_input = True
        elif difficulty_level == 'medium':
            q_data = question_data[1]
            correct_input = True
        elif difficulty_level == 'hard':
            q_data = question_data[2]
            correct_input = True
        else:
            difficulty_level = input("Invalid input! Enter easy/medium/hard: ")
            correct_input = False

    # loop through the question data and initialize a Question object then add it to the question bank
    for question_dict in q_data:
        question_bank.append(Question(question_dict['question'], question_dict['correct_answer']))

    quiz = QuizBrain(question_bank, difficulty_level.capitalize())  # initialize a QuizBrain object
    quiz.questions()  # show the number of questions in the chosen difficulty level

    # keep generating questions until function returns false
    while quiz.still_has_questions():
        quiz.next_question()

    print(f"Congratulations!!! You have completed the quiz.\nYour final score is: {quiz.score}/{quiz.question_number}\n")

    play_again = input("Do you want to play again? (yes or no): ")
    if play_again.lower() == "yes":
        quiz_game()


quiz_game()
