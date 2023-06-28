import pygame

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (234, 212, 252)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND_COLOR)

pygame.display.set_caption("Simple Game")
pygame.display.flip()

square_width = 50
square_height = 50
square_x = 100
square_y = 300

SQUARE_COLOR = (255, 0, 0)
SQUARE_VELOCITY = 5

jump_height = 100
jump_count = 0
is_jumping = False

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if not is_jumping:
            is_jumping = True
            jump_count = 10

    if is_jumping:
        if jump_count >= -10:
            square_y -= jump_count * abs(jump_count) * 0.5
            jump_count -= 1
        else:
            is_jumping = False

    if keys[pygame.K_a]:
        square_x -= SQUARE_VELOCITY

    if keys[pygame.K_d]:
        square_x += SQUARE_VELOCITY

    if (square_y < 600 - square_height) and not is_jumping:
        square_y += 5

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, SQUARE_COLOR, (square_x, square_y, square_width, square_height))
    pygame.display.update()
