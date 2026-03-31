import random

import prompt


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def generate_random_num() -> int:
    return int(random.randint(0, 100))


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_user_answer(random_number: int) -> str:
    user_answer = str.lower(prompt.string(f"Question: {random_number}\n"))
    print(f"Your answer: {user_answer}")
    return user_answer


def is_user_right(random_number: int, answer: str) -> bool:
    correct_answer = "yes" if is_even(random_number) else "no"

    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(
        f'"{answer}" is wrong answer ;(. '
        f'Correct answer was "{correct_answer}".'
        )
        return False
