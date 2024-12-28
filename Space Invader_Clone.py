import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Load assets
player_img = pygame.image.load("player.png")  # Replace with your own player image
alien_img = pygame.image.load("alien.png")  # Replace with your own alien image
bullet_img = pygame.image.load("bullet.png")  # Replace with your own bullet image

# Scale images
player_img = pygame.transform.scale(player_img, (50, 50))
alien_img = pygame.transform.scale(alien_img, (50, 50))
bullet_img = pygame.transform.scale(bullet_img, (10, 30))

# Game variables
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 70
player_speed = 5

aliens = [{"x": random.randint(0, WIDTH - 50), "y": random.randint(-100, -40), "speed": random.randint(2, 4)} for _ in range(10)]
bullets = []
bullet_speed = 100

score = 0
font = pygame.font.Font(None, 36)

# Game loop variables
running = True
game_over = False

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    # Shooting bullets
    if keys[pygame.K_SPACE]:
        if len(bullets) < 3:  # Limit the number of bullets on screen
            bullets.append({"x": player_x + 20, "y": player_y})

    # Update bullets
    for bullet in bullets[:]:
        bullet["y"] -= bullet_speed
        if bullet["y"] < 0:
            bullets.remove(bullet)

    # Update aliens
    for alien in aliens[:]:
        alien["y"] += alien["speed"]
        if alien["y"] > HEIGHT:
            game_over = True
        for bullet in bullets[:]:
            if bullet["x"] in range(alien["x"], alien["x"] + 50) and bullet["y"] in range(alien["y"], alien["y"] + 50):
                bullets.remove(bullet)
                aliens.remove(alien)
                score += 10

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw aliens
    for alien in aliens:
        screen.blit(alien_img, (alien["x"], alien["y"]))

    # Draw bullets
    for bullet in bullets:
        screen.blit(bullet_img, (bullet["x"], bullet["y"]))

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Game over check
    if game_over:
        game_over_text = font.render("GAME OVER ", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
