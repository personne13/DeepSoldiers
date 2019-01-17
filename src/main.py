import pygame
from bullet import *
from player import *
from utils import *
import numpy as np

def controlPlayer(player, input):#input is an array containing all possible inputs
    direction = Vector2(0, 0)
    if input[Input.GOLEFT]:
        direction.x += -1
    if input[Input.GORIGHT]:
        direction.x += 1
    if input[Input.GODOWN]:
        direction.y += -1
    if input[Input.GOUP]:
        direction.y += 1

    if input[Input.SHOOTUP]:
        player.actionType = ActionType.SHOOT;
        player.shootDirection = Vector2(0, -1).normalize()
    if input[Input.SHOOTLEFT]:
        player.actionType = ActionType.SHOOT;
        player.shootDirection = Vector2(-1, 0).normalize()
    if input[Input.SHOOTDOWN]:
        player.actionType = ActionType.SHOOT;
        player.shootDirection = Vector2(0, 1).normalize()
    if input[Input.SHOOTRIGHT]:
        player.actionType = ActionType.SHOOT;
        player.shootDirection = Vector2(1, 0).normalize()

    direction.normalize()

    player.changeDirection(direction)

def getInputPlayers(player1, player2):
    input1 = np.zeros(Input.nbInputs, bool)
    input2 = np.zeros(Input.nbInputs, bool)

    keystate = pygame.key.get_pressed()
    input1[Input.GOLEFT] = keystate[pygame.K_LEFT]
    input1[Input.GORIGHT] = keystate[pygame.K_RIGHT]
    input1[Input.GODOWN] = keystate[pygame.K_DOWN]
    input1[Input.GOUP] = keystate[pygame.K_UP]
    input1[Input.SHOOTUP] = keystate[pygame.K_KP8]
    input1[Input.SHOOTLEFT] = keystate[pygame.K_KP4]
    input1[Input.SHOOTDOWN] = keystate[pygame.K_KP5]
    input1[Input.SHOOTRIGHT] = keystate[pygame.K_KP6]

    input2[Input.GOLEFT] = keystate[pygame.K_q]
    input2[Input.GORIGHT] = keystate[pygame.K_d]
    input2[Input.GODOWN] = keystate[pygame.K_z]
    input2[Input.GOUP] = keystate[pygame.K_s]
    input2[Input.SHOOTUP] = keystate[pygame.K_y]
    input2[Input.SHOOTLEFT] = keystate[pygame.K_g]
    input2[Input.SHOOTDOWN] = keystate[pygame.K_h]
    input2[Input.SHOOTRIGHT] = keystate[pygame.K_j]

    return input1, input2


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



        input1, input2 = getInputPlayers(player1, player2)

        controlPlayer(player1, input1)
        controlPlayer(player2, input2)

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
