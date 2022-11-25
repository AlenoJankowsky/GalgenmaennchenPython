from HangmanStages import stages
from Words import word_list
from random import choice


def print_hangman_stage(stage):
    print(stages[stage])


def get_random_word_from_list() -> str:
    return choice(word_list).upper()


def get_word_indices(random_word, user_guess):
    indices = []
    for index, letter in enumerate(random_word):
        if letter == user_guess:
            indices.append(index)

    return indices


def fill_letters_in_word(word_completion, random_word, user_guess):
    word_completion_as_list = list(word_completion)
    indices = get_word_indices(random_word, user_guess)
    for index in indices:
        word_completion_as_list[index] = user_guess

    word_completion = "".join(word_completion_as_list)

    return word_completion


def fill_guess_in_used_guess_list(used_guess_list, user_guess):
    if user_guess not in used_guess_list:
        used_guess_list.append(user_guess)

    return used_guess_list


def guess_has_number(user_guess):
    return any(char.isdigit() for char in user_guess)


def play_again():
    while True:
        try:
            play_again_value = input(
                "Möchtest du nochmal spielen? Gib Y/N ein. Y für ja, N für nein: "
            )
            if play_again_value == "Y":
                return True
            elif play_again_value == "N":
                return False
            else:
                raise ValueError

        except ValueError:
            print("Bitte gib nur Y oder nur N ein. ", end="")
            continue


def play(random_word):
    while True:
        user_name = input("Bitte geben Sie Ihren Namen ein: ")
        print(f"Hallo {user_name}, du bist gerade dabei Hangman zu spielen. Viel Spaß!")
        print(random_word)
        hidden_letter_symbol = "_"
        used_guess_list = []
        remaining_tries = 6
        word_was_guessed = False
        word_completion = hidden_letter_symbol * len(random_word)
        print_hangman_stage(remaining_tries)
        print(word_completion)
        while not word_was_guessed and remaining_tries > 0:
            user_guess = input(
                "Bitte geben Sie einen Buchstaben oder Wort ein: "
            ).upper()
            print_hangman_stage(remaining_tries)

            if guess_has_number(user_guess):
                print("Bitte geben Sie nur Buchstaben oder ein Wort ein.")
                continue

            if user_guess in used_guess_list:
                print(f"Du hast '{user_guess}' schon mal versucht.")
                print(word_completion)
                continue

            if user_guess not in random_word and user_guess:
                print(
                    f"Der Buchstabe oder das Wort '{user_guess}' ist nicht im Ratewort enthalten"
                )
                remaining_tries -= 1
            else:
                print(
                    f"Der Buchstabe oder das Wort '{user_guess}' ist im Ratewort enthalten"
                )
                for letter in user_guess:
                    word_completion = fill_letters_in_word(
                        word_completion, random_word, letter
                    )

                word_was_guessed = hidden_letter_symbol not in word_completion
            print(word_completion)
            fill_guess_in_used_guess_list(used_guess_list, user_guess)

        if word_was_guessed:
            print("Herzlichen Glückwünsch, Sie haben gewonnen :).")
        else:
            print("Schade, leider verloren")

        if play_again():
            random_word = get_random_word_from_list()
            continue
        else:
            break


def main_game():
    play(get_random_word_from_list())


if __name__ == "__main__":
    main_game()
