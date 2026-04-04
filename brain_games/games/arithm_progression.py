import random

from brain_games.base_game import BaseGame


class ArithmeticProgression(BaseGame):
    @property
    def description(self):
        return "What number is missing in the progression?"
    
    def __init__(self):
        super().__init__()
        self.correct_answer: int = 0
        self.arithm_progression: str = ""
        
    @staticmethod
    def generateProgression() -> list[str]:
        progression_arr: list[str] = []
        d = random.randint(1, 10)
        a1 = random.randint(1, 100)
        random_length = random.randint(5, 10)
        
        # add 1st random int to 0 index
        progression_arr.append(str(a1))

        for i in range(random_length - 1):
            next_num = int(progression_arr[i]) + d
            progression_arr.append(str(next_num))
        
        return progression_arr
    
    @staticmethod
    def hideRandomEl(progression_arr: list) -> tuple[str, str]:
        randomEl = random.randint(0, len(progression_arr) - 1)  
        correct_answer: str = progression_arr[randomEl]
        # hide element
        progression_arr[randomEl] = ".."
        
        return (correct_answer, " ".join(progression_arr))
        
    def generate_question(self) -> str:
        self.correct_answer, self.arithm_progression = self.hideRandomEl(
            self.generateProgression()
            )
        return f"Question: {self.arithm_progression}\n"
    
    def get_correct_answer(self) -> int:
        return str(self.correct_answer)