import random

from ..base_game import run_game

DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_random_numbers() -> list[str]:
    randomNums: list = []
    for _ in range(2):
        randomNums.append(int(random.randint(1, 100)))
    return randomNums


def calculate_gcd(rand_nums: list[str]) -> int:
    a = int(rand_nums[0])
    b = int(rand_nums[1])
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
    return gcd


def generate_question_and_answer():
    numbers = ' '.join(
        [str(i) for i in generate_random_numbers()]
        )
    question = f"Question: {numbers}\n"
    answer = str(calculate_gcd(numbers.split(" ")))
    
    return question, answer


def run():
    run_game(DESCRIPTION, generate_question_and_answer)
