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


def generate_secret_code(length_key=CODE_LENGTH):
    return [random.choice(list(COLORS.keys())) for _ in range(length_key)]


def evaluate_guess(secret_code, guess):
    secret_copy = secret_code.copy()
    guess_copy = guess.copy()

    black_pegs = sum(s == g for s, g in zip(secret_copy, guess_copy))

    secret_copy = [c for c, t in zip(secret_copy, guess_copy) if c != t]
    guess_copy = [t for c, t in zip(secret_code, guess_copy) if c != t]

    white_pegs = 0
    for color in guess_copy:
        if color in secret_copy:
            white_pegs += 1
            secret_copy.remove(color)

    return black_pegs, white_pegs
