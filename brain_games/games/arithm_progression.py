import random

from brain_games.base_game import run_game

DESCRIPTION = "What number is missing in the progression?"
    

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


def hideRandomEl(progression_arr: list) -> tuple[str, str]:
    randomEl = random.randint(0, len(progression_arr) - 1)  
    correct_answer: str = progression_arr[randomEl]
    # hide element
    progression_arr[randomEl] = ".."
    
    return (correct_answer, " ".join(progression_arr))
    

def generate_question_and_answer():
    progression = generateProgression()
    answer, question = hideRandomEl(progression)
    question = f"Question: {question}\n"
    
    return question, str(answer)


def run():
    run_game(DESCRIPTION, generate_question_and_answer)
