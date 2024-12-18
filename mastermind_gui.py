import pygame
import random
import sys

COLORS = {
    'Red': (255, 0, 0),
    'Blue': (0, 0, 255),
    'Green': (0, 255, 0),
    'Yellow': (255, 255, 0),
    'White': (255, 255, 255),
    'Purple': (128, 0, 128)
}

# Game settings
CODE_LENGTH = 4
MAX_ATTEMPTS = 10

# Game window configuration
WIDTH, HEIGHT = 800, 600
CIRCLE_RADIUS = 40
MARGIN_X = 100
MARGIN_Y = 50
SPACING_X = 100
SPACING_Y = 90

pygame.init()
font = pygame.font.Font(None, 36)


def generate_secret_code(length=CODE_LENGTH):
    secret_code = []
    for _ in range(length):
        color = random.choice(list(COLORS.keys()))
        secret_code.append(color)
    return secret_code


def evaluate_guess(secret_code, guess):
    secret_copy = secret_code.copy()
    guess_copy = guess.copy()

    black_pegs = 0
    for key in range(len(secret_copy)):
        if secret_copy[key] == guess_copy[key]:
            black_pegs += 1
            secret_copy[key] = None
            guess_copy[key] = None

    white_pegs = 0
    for color in guess_copy:
        if color is not None and color in secret_copy:
            white_pegs += 1
            secret_copy[secret_copy.index(color)] = None

    return black_pegs, white_pegs


if __name__ == '__main__':
    secret_code = generate_secret_code()

    guess = ['Blue', 'Red', 'Green', 'Yellow']
    result = evaluate_guess(secret_code, guess)
    print('le code secret est : ', secret_code)
    print(result)
