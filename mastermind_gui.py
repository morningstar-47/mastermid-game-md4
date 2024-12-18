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


def display_text(screen, text, x, y, color=(0, 0, 0)):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


def draw_board(screen, secret_code, attempt_history, current_selection, current_row):
    screen.fill((240, 240, 240))

    for i, color in enumerate(COLORS.keys()):
        center = (MARGIN_X + i * SPACING_X, HEIGHT - 100)
        pygame.draw.circle(screen, COLORS[color], center, CIRCLE_RADIUS)
        pygame.draw.circle(screen, (0, 0, 0), center, CIRCLE_RADIUS, 2)

    for row in range(MAX_ATTEMPTS):
        for col in range(CODE_LENGTH):
            center = (MARGIN_X + col * SPACING_X, MARGIN_Y + row * SPACING_Y)
            pygame.draw.circle(screen, (200, 200, 200),
                               center, CIRCLE_RADIUS, 1)

    for row, attempt in enumerate(attempt_history):
        for col, color in enumerate(attempt):
            center = (MARGIN_X + col * SPACING_X, MARGIN_Y + row * SPACING_Y)
            pygame.draw.circle(screen, COLORS[color], center, CIRCLE_RADIUS)

        feedback = evaluate_guess(secret_code, attempt)
        draw_feedback(screen, row, feedback)

    for col, color in enumerate(current_selection):
        if color:
            center = (MARGIN_X + col * SPACING_X,
                      MARGIN_Y + current_row * SPACING_Y)
            pygame.draw.circle(screen, COLORS[color], center, CIRCLE_RADIUS)

    display_text(screen, "Guess the secret code!", 10, 10)
    display_text(screen, f"Attempts left: {
                 MAX_ATTEMPTS - current_row}", WIDTH - 250, 10)

    pygame.display.flip()


def draw_feedback(screen, row, feedback):
    black_pegs, white_pegs = feedback
    start_x = WIDTH - 120
    start_y = MARGIN_Y + row * SPACING_Y

    for i in range(black_pegs):
        center = (start_x + (i % 2) * 30, start_y + (i // 2) * 20)
        pygame.draw.circle(screen, (0, 0, 0), center, 10)

    for i in range(white_pegs):
        center = (start_x + (i % 2) * 30, start_y + (i // 2) * 20)
        pygame.draw.circle(screen, (255, 255, 255), center, 10, 2)


def handle_selection(position, current_selection):
    for i, color in enumerate(COLORS.keys()):
        color_center = pygame.math.Vector2(
            MARGIN_X + i * SPACING_X, HEIGHT - 100)

        if pygame.math.Vector2(position).distance_to(color_center) < CIRCLE_RADIUS:
            for j in range(CODE_LENGTH):
                if current_selection[j] is None:
                    current_selection[j] = color
                    break

    return current_selection


def reset_selection():
    return [None] * CODE_LENGTH


def play_mastermind():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mastermind")

    secret_code = generate_secret_code()
    attempt_history = []
    current_selection = reset_selection()
    current_row = 0
    game_over = False

    while True:
        draw_board(screen, secret_code, attempt_history,
                   current_selection, current_row)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_over:
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                current_selection = handle_selection(
                    event.pos, current_selection)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and None not in current_selection:
                    black_pegs, white_pegs = evaluate_guess(
                        secret_code, current_selection)
                    attempt_history.append(current_selection.copy())

                    if black_pegs == CODE_LENGTH:
                        display_text(screen, "Congratulations, you won!",
                                     WIDTH // 2 - 150, HEIGHT // 2)
                        game_over = True

                    current_selection = reset_selection()
                    current_row += 1

                    if current_row == MAX_ATTEMPTS:
                        loss_message = f"Game Over! The code was: {
                            ' '.join(secret_code)}"
                        display_text(screen, loss_message,
                                     WIDTH // 2 - 150, HEIGHT // 2)
                        game_over = True


if __name__ == "__main__":
    play_mastermind()
