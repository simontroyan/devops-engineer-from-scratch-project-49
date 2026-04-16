import random

from ..base_game import run_game

DESCRIPTION = "What is the result of the expression?"


def generate_expression() -> str:
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    
    random_expression = f"{a} {operator} {b}"
    
    return random_expression
    

def generate_question_and_answer():
    random_expression = generate_expression()
    question = f"Question: {random_expression}\n"
    answer = str(eval(random_expression))
    
    return question, answer


def run():
    run_game(DESCRIPTION, generate_question_and_answer)
