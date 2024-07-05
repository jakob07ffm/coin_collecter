import pygame
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collect the Coins")

clock = pygame.time.Clock()
FPS = 30

player_size = 50
player_pos = [screen_width // 2, screen_height // 2]
player_speed = 10

coin_size = 30
coin_pos = [random.randint(0, screen_width - coin_size), random.randint(0, screen_height - coin_size)]

game_time = 30  
start_ticks = pygame.time.get_ticks()

def detect_collision(player_pos, coin_pos):
    p_x, p_y = player_pos
    c_x, c_y = coin_pos

    if (c_x >= p_x and c_x < (p_x + player_size)) or (p_x >= c_x and p_x < (c_x + coin_size)):
        if (c_y >= p_y and c_y < (p_y + player_size)) or (p_y >= c_y and p_y < (c_y + coin_size)):
            return True
    return False

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < screen_height - player_size:
        player_pos[1] += player_speed

    screen.fill(BLACK)

    if detect_collision(player_pos, coin_pos):
        score += 1
        coin_pos = [random.randint(0, screen_width - coin_size), random.randint(0, screen_height - coin_size)]

    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, GOLD, (coin_pos[0], coin_pos[1], coin_size, coin_size))

    font = pygame.font.SysFont("monospace", 35)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    timer_text = font.render(f"Time: {game_time - seconds}", True, WHITE)
    screen.blit(timer_text, (10, 50))

    if game_time - seconds <= 0:
        game_over = True

    pygame.display.flip()
    clock.tick(FPS)

font = pygame.font.SysFont("monospace", 75)
game_over_text = font.render("Game Over", True, RED)
screen.blit(game_over_text, (screen_width / 2 - 200, screen_height / 2 - 50))
pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()
sys.exit()
