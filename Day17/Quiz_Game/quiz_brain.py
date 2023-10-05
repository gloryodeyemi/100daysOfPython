class QuizBrain:
    def __init__(self, q_list, q_difficulty):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.difficulty = q_difficulty

    def questions(self):
        """Display the total number of questions in the current level of difficulty."""
        print(f"\nThere are {len(self.question_list)} questions in the '{self.difficulty}' difficulty.\n")

    def still_has_questions(self):
        """Returns True/False after if the question number is lesser than the length of questions"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Display the current question and asks user for input
        Call the check answer function
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        :param user_answer: the answer the user entered.
        :param correct_answer: the correct answer to the question.
        :return: display correct/incorrect message and increment score if correct.
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!!!")
        else:
            print("Incorrect!!!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
