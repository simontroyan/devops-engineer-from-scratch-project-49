import random

from ..base_game import run_game

DESCRIPTION = "What is the result of the expression?"
MAX_NUMBER = 100
OPERATORS = ['+', '-', '*']


def calculate(a, operator, b):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    return a * b


def generate_question_and_answer():
    operator = random.choice(OPERATORS)
    a = random.randint(0, MAX_NUMBER)
    b = random.randint(0, MAX_NUMBER)
    question = f"Question: {a} {operator} {b}\n"
    answer = str(calculate(a, operator, b))
    
    return question, answer


def run():
    run_game(DESCRIPTION, generate_question_and_answer)
