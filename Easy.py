import pygame, random

# initialize pygame
pygame.init()

# Display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Fetch the fly")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
FLY_STARTING_VELOCITY = 5
FLY_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
fly_velocity = FLY_STARTING_VELOCITY

# Set colors
LIGHTBLUE = (81, 174, 232)
DARKBLUE = (5, 63, 99)

# Set fonts
font = pygame.font.Font('FONT.ttf', 32)

# Set texts
score_text = font.render("Score: " + str(score), True, DARKBLUE, LIGHTBLUE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Fetch the fly", True, DARKBLUE, LIGHTBLUE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, DARKBLUE, LIGHTBLUE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAMEOVER", True, DARKBLUE, LIGHTBLUE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any key to play again", True, DARKBLUE, LIGHTBLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)

# Set sound and music
fly_sound = pygame.mixer.Sound("fly_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
miss_sound.set_volume(.1)
pygame.mixer.music.load("ftf_background_music.wav")

# Set images
player_image = pygame.image.load("frog.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2

fly_image = pygame.image.load("fly.png")
fly_rect = fly_image.get_rect()
fly_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
fly_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

# Main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    # Check quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY

    # Move fly
    if fly_rect.x < 0:
        # Missed fly
        player_lives -= 1
        miss_sound.play()
        fly_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        fly_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        # Move fly
        fly_rect.x -= fly_velocity

    # Collisions
    if player_rect.colliderect(fly_rect):
        score += 1
        fly_sound.play()
        fly_velocity += FLY_ACCELERATION
        fly_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        fly_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

    # Update HUD
    score_text = font.render("Score: " + str(score), True, DARKBLUE, LIGHTBLUE)
    lives_text = font.render("Lives: " + str(player_lives), True, DARKBLUE, LIGHTBLUE)

    # Game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        # Pause
        pygame.mixer.music.stop()
        is_pause = True
        while is_pause:
            for event in pygame.event.get():
                # Play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT // 2
                    coin_velocity = FLY_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_pause = False
                # Quit
                if event.type == pygame.QUIT:
                    is_pause = False
                    running = False

    # Fill display
    display_surface.fill(LIGHTBLUE)

    # Blit to screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, DARKBLUE, (0, 64), (WINDOW_WIDTH, 64), 2)

    display_surface.blit(player_image, player_rect)
    display_surface.blit(fly_image, fly_rect)

    # Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
