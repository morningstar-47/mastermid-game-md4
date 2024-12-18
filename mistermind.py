import random


COMBINAISON_LENGTH = 4
ATTEMPTS_MAX = 10
COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']


def generate_code(length_key=COMBINAISON_LENGTH):
    return [random.choice(COLORS) for _ in range(length_key)]


def get_player_guess():
    while True:
        guess = input(
            "Entrez votre combinaison (ex: R G B Y) : ").upper().split()

        if len(guess) != COMBINAISON_LENGTH:
            print(f"Veuillez entrer exactement {COMBINAISON_LENGTH} couleurs.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Couleur invalide : {
                      color}. Veuillez utiliser seulement {', '.join(COLORS)}.")
                break
        else:
            return guess


def checking_guess(guess, combinaison):
    correct_position = 0

    for i in range(len(guess)):
        if guess[i] == combinaison[i]:
            correct_position += 1

    correct_color = 0
    for color in set(guess):
        correct_color += min(guess.count(color), combinaison.count(color))

    correct_color -= correct_position

    return correct_position, correct_color


def mastermind_terminal():
    code = generate_code()
    attempts = 0

    print("Bienvenue à Mastermind MD4 Hetic!")
    print(f"Essayez de deviner la combinaison de {
          COMBINAISON_LENGTH} couleurs.")
    print(f"Couleurs possibles : {', '.join(COLORS)}.")
    print(f"Vous avez {ATTEMPTS_MAX} essais au total.")

    while attempts < ATTEMPTS_MAX:
        print(f"Essai {attempts + 1} sur {ATTEMPTS_MAX}.")
        guess = get_player_guess()

        correct_position, correct_color = checking_guess(guess, code)
        print(f"Couleurs bien placées : {correct_position}")
        print(f"Couleurs correctes mais mal placées : {correct_color}")

        if correct_position == COMBINAISON_LENGTH:
            print("Félicitations! Vous avez deviné la combinaison!")
            return

        attempts += 1
        print(f"Il vous reste {ATTEMPTS_MAX - attempts} essai(s).")

    print(f"Désolé, vous avez utilisé tous vos essais.")
    print(f"La combinaison correcte était : {' '.join(code)}")


if __name__ == "__main__":
    mastermind_terminal()
