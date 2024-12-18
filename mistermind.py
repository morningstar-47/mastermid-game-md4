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
