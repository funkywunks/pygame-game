import pygame
import math
import time

def wall_collision():
    if circle_surface_coordinates[0] < 0:
        circle_surface_coordinates[0] = 0

    if circle_surface_coordinates[0] > SCREEN_WIDTH - 30:
        circle_surface_coordinates[0] = SCREEN_WIDTH - 30

    if circle_surface_coordinates[1] < 0:
        circle_surface_coordinates[1] = 0

    if circle_surface_coordinates[1] > SCREEN_HEIGHT - 30:
        circle_surface_coordinates[1] = SCREEN_HEIGHT - 30


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
bg_surface.fill('Black')


running = True

circle_surface = pygame.Surface((30, 30))
circle_surface_coordinates = [(SCREEN_WIDTH / 2) - 15, (SCREEN_HEIGHT / 2) - 15]
player_direction_degrees = 90

previous_time = time.time()
while running:
    delta_time = previous_time - time.time()
    previous_time = time.time()

    if not running:
        pygame.quit()
        break

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        circle_surface_coordinates[0] += 150 * delta_time * math.cos(math.radians(player_direction_degrees))
        circle_surface_coordinates[1] += 150 * delta_time * math.sin(math.radians(player_direction_degrees))

        wall_collision()

    if keys[pygame.K_LEFT]:
        player_direction_degrees += 360 * delta_time

    if keys[pygame.K_RIGHT]:
        player_direction_degrees -= 360 * delta_time

    screen.blit(bg_surface, (0, 0))
    screen.blit(circle_surface, circle_surface_coordinates)
    pygame.draw.circle(circle_surface, 'White', (15, 15), 15, 1)
    pygame.display.update()

print('bye :D')
