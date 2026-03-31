from .games_logic import (
    generate_random_num,
    get_user_answer,
    is_user_right,
    welcome_user,
)


def odd_game():
    name = welcome_user()
    try_count = 0

    print(
        'Answer "yes" if the number is even, otherwise answer "no".'
        )

    while try_count < 3:
        random_num = generate_random_num()
        user_answer = get_user_answer(random_num)

        if is_user_right(random_num, user_answer):
            try_count += 1
        else:
            break

    print(f"Congratulations, {name}!")
