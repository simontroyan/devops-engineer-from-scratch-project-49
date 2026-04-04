import random

from ..base_game import BaseGame


class EvenGame(BaseGame):
    @property
    def description(self) -> str:
        return 'Answer "yes" if the number is even, otherwise answer "no".'

    def __init__(self):
        super().__init__()
        self.random_number: int = 0

    @staticmethod
    def generate_random_num() -> int:
        return int(random.randint(0, 100))

    @staticmethod
    def is_even(number: int) -> bool:
        return number % 2 == 0

    def generate_question(self) -> str:
        self.random_number = self.generate_random_num()
        return f"Question: {self.random_number}\n"

    def get_correct_answer(self) -> str:
        return "yes" if self.is_even(self.random_number) else "no"
