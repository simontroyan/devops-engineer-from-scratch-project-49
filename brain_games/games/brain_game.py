import math
import random

from brain_games.base_game import BaseGame


class BrainGame(BaseGame):
    @property
    def description(self):
        return 'Answer "yes" if given number is prime. Otherwise answer "no"'
    
    def __init__(self):
        super().__init__()
        self.correct_answer: bool = False
        self.random_num: int = 0
        
    @staticmethod
    def generate_random_num() -> int:
        return random.randint(0, 10000)
    
    @staticmethod
    def is_predicate(num: int) -> bool:
        if num <= 1:
            return False
        
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
            elif num % 1 == 0 and num % num == 0:
                return True
        return False
        
    def generate_question(self):
        self.random_num = self.generate_random_num()
        return f"Question: {self.random_num}\n"
    
    def get_correct_answer(self):
        return "yes" if self.is_predicate(self.random_num) else "no"