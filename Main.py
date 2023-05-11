import pygame

running = True

pygame.init()

# Display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Fetch the fly")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()
# Set colors
LIGHTBLUE = (81, 174, 232)
DARKBLUE = (5, 63, 99)

# Set fonts
font = pygame.font.Font('FONT.ttf', 32)

# insert stuff
font1 = pygame.font.Font('FONT.ttf', 124)
font2 = pygame.font.Font('FONT.ttf', 64)
font3 = pygame.font.Font('FONT.ttf', 24)

# Set texts
title_text = font1.render("Fetch the fly", True, DARKBLUE, LIGHTBLUE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 40

level_text = font2.render("Select level", True, DARKBLUE, LIGHTBLUE)
level_rect = title_text.get_rect()
level_rect.centerx = WINDOW_WIDTH // 2
level_rect.y = 200

levels_text = font3.render("Easy: Press 'e'    Medium: Press 'm'    Hard: Press 'h'", True, DARKBLUE, LIGHTBLUE)
levels_rect = title_text.get_rect()
levels_rect.centerx = WINDOW_WIDTH // 2
levels_rect.y = 300

frog_image = pygame.image.load("ForsideFrog.png")
frog_rect = frog_image.get_rect()
frog_rect.left = 750
frog_rect.centery = 280

while running:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            exec(open("Easy.py").read())
        elif keys[pygame.K_m]:
            exec(open("Medium.py").read())
        elif keys[pygame.K_h]:
            exec(open("Hard.py").read())

    display_surface.fill(LIGHTBLUE)

    display_surface.blit(title_text, title_rect)
    display_surface.blit(level_text, level_rect)
    display_surface.blit(levels_text, levels_rect)
    display_surface.blit(frog_image, frog_rect)