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

    if keystate[pygame.K_KP8]:
        player1.actionType = ActionType.SHOOT;
        player1.shootDirection = Vector2(0, -1).normalize()
    if keystate[pygame.K_KP4]:
        player1.actionType = ActionType.SHOOT;
        player1.shootDirection = Vector2(-1, 0).normalize()
    if keystate[pygame.K_KP5]:
        player1.actionType = ActionType.SHOOT;
        player1.shootDirection = Vector2(0, 1).normalize()
    if keystate[pygame.K_KP6]:
        player1.actionType = ActionType.SHOOT;
        player1.shootDirection = Vector2(1, 0).normalize()


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

    if keystate[pygame.K_y]:
        player2.actionType = ActionType.SHOOT;
        player2.shootDirection = Vector2(0, -1).normalize()
    if keystate[pygame.K_g]:
        player2.actionType = ActionType.SHOOT;
        player2.shootDirection = Vector2(-1, 0).normalize()
    if keystate[pygame.K_h]:
        player2.actionType = ActionType.SHOOT;
        player2.shootDirection = Vector2(0, 1).normalize()
    if keystate[pygame.K_j]:
        player2.actionType = ActionType.SHOOT;
        player2.shootDirection = Vector2(1, 0).normalize()

def handleActions(player, all_sprites):
    if(player.actionType == ActionType.SHOOT):
        if(player.shoot()):
            newBullet = Bullet(Vector2(player.rect.centerx, player.rect.centery), player.shootDirection, player)
            all_sprites.add(newBullet)

        player.actionType = ActionType.NONE


def handleCollisions(player, all_sprites):
    #for i in range(len(all_sprites.sprites())):
    #    (all_sprites.sprites()[i].direction)
    sprites = all_sprites.sprites()
    length = len(sprites)
    toRemove = []
    for j in range(length):
        bullet = sprites[j]
        if (bullet.tag == ObjectName.BULLET): #check if it's a bullet
            if (bullet.shooter != player):
                if bullet.is_collided_with(player):
                    player.reset()
                    player.score += 1
                    print(player.name)
                    print(player.score)
                    toRemove.append(bullet)


    for b in toRemove:
        b.kill()



    #if (len(all_sprites.sprites()) > 2) :
    #    for i in range(2):
    #        for j in range(2, len(all_sprites.sprites())):
    #            print(j)
    #            print(len(all_sprites.sprites()))
    #            bullet = all_sprites.sprites()[j]
    #            if bullet.is_collided_with(all_sprites.sprites()[i]):
    #                all_sprites.sprites()[i].kill





def main():
    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DeepSoldiers!")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    player1 = Player(Vector2(10, 10), "Franck")
    player2 = Player(Vector2(100, 100), "Thomas")

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
        #print (all_sprites)
        handleCollisions(player1, all_sprites)
        handleCollisions(player2, all_sprites)


        # # Update
        all_sprites.update()

        # Draw / render
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

main()
