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
