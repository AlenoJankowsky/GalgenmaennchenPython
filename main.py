from HangmanStages import stages
from Words import word_list
from random import choice


def print_hangman_stage(stage):
    print(stages[stage])


def get_random_word_from_list() -> str:
    return choice(word_list).upper()


def play(random_word):
    remaining_tries = 6
    word_was_guessed = False
    while not word_was_guessed and remaining_tries > 0:
        user_guess = input("Bitte geben Sie einen Buchstaben oder Wort ein: ").upper()
        if user_guess not in random_word:
            print(
                f"Der Buchstabe oder das Wort {user_guess} ist nicht im Ratewort enthalten"
            )
            remaining_tries -= 1
        else:
            print(f"Der Buchstabe oder das Wort {user_guess} ist im Ratewort enthalten")


def main_game():
    play(get_random_word_from_list())


if __name__ == "__main__":
    main_game()
