import random


COMBINAISON_LENGTH = 4
ATTEMPTS_MAX = 10
COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']


def generate_code(length_key=COMBINAISON_LENGTH):
    return [random.choice(COLORS) for _ in range(length_key)]
