import math
import random

from brain_games.base_game import run_game

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    

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
    

def generate_question_and_answer():
    random_num = generate_random_num()
    question = f"Question: {random_num}\n"
    answer = "yes" if is_predicate(random_num) else "no"

    return question, answer


def run():
    run_game(DESCRIPTION, generate_question_and_answer)
