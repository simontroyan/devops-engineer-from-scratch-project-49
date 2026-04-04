import random

from ..base_game import BaseGame


class GcdGame(BaseGame):
    @property
    def description(self) -> str:
        return "Find the greatest common divisor (GCD) of given numbers."
    
    def __init__(self):
        super().__init__()
        self.random_nums: str = ""
        self.greatest_divisor: int = 1
    
    @staticmethod
    def generate_random_numbers() -> list[str]:
        randomNums: list = []
        for _ in range(2):
            randomNums.append(int(random.randint(1, 100)))
        return randomNums
    
    @staticmethod
    def calculate_gcd(rand_nums: list[str]) -> int:
        a = int(rand_nums[0])
        b = int(rand_nums[1])
        gcd = 1
        for i in range(1, min(a, b) + 1):
            if (a % i == 0) and (b % i == 0):
                gcd = i
        print(f"a={a}, b={b}, gcd={gcd}")
        return gcd
        
    def generate_question(self):
        self.random_nums = ' '.join(
            [str(i) for i in self.generate_random_numbers()]
            )
        return f"Question: {self.random_nums}\n"
    
    def get_correct_answer(self):
        return str(self.calculate_gcd(self.random_nums.split(" ")))
        