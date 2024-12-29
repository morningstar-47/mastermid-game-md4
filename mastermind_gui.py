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


def display_text(screen, text, x, y, color=(0, 0, 0)):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


def draw_circle(screen, x, y, color):
    pygame.draw.circle(screen, COLORS[color], (x, y), CIRCLE_RADIUS)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), CIRCLE_RADIUS, 2)


def draw_feedback_pegs(screen, black_pegs, white_pegs, row):
    start_x = MARGIN_X + SPACING_X * CODE_LENGTH + 50
    start_y = MARGIN_Y + row * SPACING_Y

    for index in range(black_pegs):
        x = start_x + (index * 20)
        pygame.draw.circle(screen, (0, 0, 0), (x, start_y), 8)

    for index in range(white_pegs):
        x = start_x + ((index + black_pegs) * 20)
        pygame.draw.circle(screen, (128, 128, 128), (x, start_y), 8)


if __name__ == '__main__':
    secret_code = generate_secret_code()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mastermind')

    current_attempt = 0
    guesses = []
    current_guess = []
    game_over = False
    won = False

    color_buttons = []
    for index, color in enumerate(COLORS.keys()):
        x = MARGIN_X + index * 80
        y = HEIGHT - 100
        color_buttons.append((pygame.Rect(
            x - CIRCLE_RADIUS, y - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2), color))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                for button, color in color_buttons:
                    if button.collidepoint(mouse_pos) and len(current_guess) < CODE_LENGTH:
                        current_guess.append(color)

                        if len(current_guess) == CODE_LENGTH:
                            black_pegs, white_pegs = evaluate_guess(
                                secret_code, current_guess)
                            guesses.append(
                                (current_guess.copy(), (black_pegs, white_pegs)))

                            if black_pegs == CODE_LENGTH:
                                game_over = True
                                won = True
                            elif current_attempt >= MAX_ATTEMPTS - 1:
                                game_over = True

                            current_guess = []
                            current_attempt += 1

     # Draw game board
        screen.fill((200, 200, 200))

        # Draw previous guesses
        for row, (guess, feedback) in enumerate(guesses):
            for col, color in enumerate(guess):
                x = MARGIN_X + col * SPACING_X
                y = MARGIN_Y + row * SPACING_Y
                draw_circle(screen, x, y, color)
            draw_feedback_pegs(screen, feedback[0], feedback[1], row)

        # Draw current incomplete guess
        for col, color in enumerate(current_guess):
            x = MARGIN_X + col * SPACING_X
            y = MARGIN_Y + current_attempt * SPACING_Y
            draw_circle(screen, x, y, color)

        # Draw color selection buttons
        for button, color in color_buttons:
            pygame.draw.circle(
                screen, COLORS[color], button.center, CIRCLE_RADIUS)
            pygame.draw.circle(screen, (0, 0, 0),
                               button.center, CIRCLE_RADIUS, 2)

        # Display game over message
        if game_over:
            if won:
                display_text(screen, "You Won!", WIDTH//2 - 50, HEIGHT//2)
            else:
                display_text(screen, "Game Over!", WIDTH//2 - 50, HEIGHT//2)
                display_text(screen, f"Secret code was: {' '.join(secret_code)}",
                             WIDTH//2 - 150, HEIGHT//2 + 40)

        pygame.display.flip()

    guess = ['Blue', 'Red', 'Green', 'Yellow']
    result = evaluate_guess(secret_code, guess)
    print('le code secret est : ', secret_code)
    print(result)
