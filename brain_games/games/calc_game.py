import random

from ..base_game import BaseGame


class CalcGame(BaseGame):
    @property
    def description(self) -> str:
        return "What is the result of the expression?"
    
    def __init__(self):
        super().__init__()
        self.random_expression: str = ""
        self.expression_res: int = 0
        self.a = 0
        self.b = 0
        
    @staticmethod
    def generate_expression() -> str:
        operators = ['+', '-', '*']
        operator = random.choice(operators)
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        
        random_expression = f"{a} {operator} {b}"
        
        return random_expression
        
    def generate_question(self) -> str:
        self.random_expression = self.generate_expression()
        return f"Question: {self.random_expression}\n"
    
    def get_correct_answer(self) -> int:
        return str(eval(self.random_expression))