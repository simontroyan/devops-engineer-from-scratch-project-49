import prompt


def run_game(description, generate_question_and_answer):
    print("Welcome to the Brain Games!")
    
    user_name = prompt.string("May I have your name? ")
    
    print(f"Hello, {user_name}!")
    # Description
    print(description)

    for _ in range(3):
        question, correct_answer = generate_question_and_answer()
        user_answer = prompt.string(question)
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f'"{user_answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".\n'
                f"Let's try again, {user_name}!"

            )
            return
    print(f"Congratulations, {user_name}!")