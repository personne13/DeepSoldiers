import pygame
from player import *
from utils import *

def controlPlayer(player):
    keystate = pygame.key.get_pressed()
    direction = Vector2(0, 0)
    if keystate[pygame.K_LEFT]:
        direction.x += -1
    if keystate[pygame.K_RIGHT]:
        direction.x += 1
    if keystate[pygame.K_UP]:
        direction.y += -1
    if keystate[pygame.K_DOWN]:
        direction.y += 1

    direction.normalize()

    player.changeDirection(direction)

def main():
    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shmup!")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    # Game loop
    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        controlPlayer(player)

        # Update
        all_sprites.update()

        # Draw / render
        screen.fill(BLACK)
        all_sprites.draw(screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

main()
