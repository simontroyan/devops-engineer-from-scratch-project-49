import prompt

from .interfaces import IGame


class BaseGame(IGame):
    def __init__(self):
        self.user_name = ""
        self.try_count = 0

    def welcome_user(self) -> str:
        print("Welcome to the Brain Games!")
        self.user_name = prompt.string("May I have your name? ")
        print(f"Hello, {self.user_name}!")
        return self.user_name

    def get_user_answer(self, question: str) -> str:
        self.user_answer = str.lower(prompt.string(question))
        print(f"Your answer: {self.user_answer}")
        return self.user_answer

    def check_correct_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct!")
            return True
        else:
            print(
                f'"{user_answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".'
            )
            return False

    def run(self):
        self.welcome_user()
        print(self.description)

        while self.try_count < 3:
            question = self.generate_question()
            user_answer = self.get_user_answer(question)
            correct_answer = self.get_correct_answer()

            if self.check_correct_answer(user_answer, correct_answer):
                self.try_count += 1
            else:
                break
