import pygame
from bullet import *
from player import *
from utils import *

def controlPlayers(player1, player2):
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


    if keystate[pygame.K_p]:
        player1.actionType = ActionType.SHOOT;
        player1.shootDirection = Vector2(2, 6).normalize()

    direction.normalize()

    player1.changeDirection(direction)

    direction = Vector2(0, 0)
    if keystate[pygame.K_q]:
        direction.x += -1
    if keystate[pygame.K_d]:
        direction.x += 1
    if keystate[pygame.K_z]:
        direction.y += -1
    if keystate[pygame.K_s]:
        direction.y += 1

    direction.normalize()

    player2.changeDirection(direction)

    if keystate[pygame.K_t]:
        player2.actionType = ActionType.SHOOT;
        player2.shootDirection = Vector2(2, 6).normalize()

def handleActions(player, all_sprites):
    if(player.actionType == ActionType.SHOOT):
        if(player.shoot()):
            newBullet = Bullet(Vector2(player.rect.centerx, player.rect.centery), player.shootDirection)
            all_sprites.add(newBullet)

        player.actionType = ActionType.NONE

def main():
    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DeepSoldiers!")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    player1 = Player(Vector2(10, 10))
    player2 = Player(Vector2(100, 100))

    all_sprites.add(player1)
    all_sprites.add(player2)


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



        controlPlayers(player1, player2)
        handleActions(player1, all_sprites)
        handleActions(player2, all_sprites)
        # handleCollisions(player1, player2, all_sprites)

        # # Update
        all_sprites.update()

        # Draw / render
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

main()
