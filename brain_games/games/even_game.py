import random

from ..base_game import run_game

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    num = random.randint(0, 100)
    question = f"Question: {num}\n"
    answer = "yes" if num % 2 == 0 else "no"
    return question, answer


def run():
    run_game(DESCRIPTION, generate_question_and_answer)
