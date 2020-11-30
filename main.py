import pygame
from game import Game
from son import Son
pygame.init()

#le titre du jeu
pygame.display.set_caption('SpaceShip')

#longeur, largeur et fps
width = 600
height = 600
fps = 30

#ecran
screen = pygame.display.set_mode((width, height))

#image arriere plan
background = pygame.image.load('fonts/background.jpg')
background_rect = background.get_rect()

space_ship = pygame.image.load('fonts/spaceship (1).png').convert_alpha()
space_ship = pygame.transform.scale(space_ship, (200, 320))
space_ship_rect = space_ship.get_rect()
space_ship_rect.x = 200
space_ship_rect.y = 70

play_btn = pygame.image.load('fonts/play.png')
play_btn = pygame.transform.scale(play_btn, (64, 110))
play_btn_rect = play_btn.get_rect()
play_btn_rect.x = 270
play_btn_rect.y = 350

running = True

#clock pour la mises a jour du jeu
clock = pygame.time.Clock()

#appel au jeu
game = Game()


#ajouter les sons arriere plan
pygame.mixer.music.load('sound/music.mp3')
pygame.mixer.music.set_volume(.3)
pygame.mixer.music.play()
while running:
    delta_ms = clock.tick(fps)
    delta_s = delta_ms/1000.0

    screen.blit(background, background_rect)

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(space_ship, space_ship_rect)
        screen.blit(play_btn, play_btn_rect)

    pygame.display.flip()

    for evt in pygame.event.get():

        if evt.type == pygame.QUIT:
            running = False

        if evt.type == pygame.MOUSEBUTTONDOWN:
            if play_btn_rect.collidepoint(evt.pos):
                game.start_game()

        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_ESCAPE:
                running = False
            if evt.key == pygame.K_RIGHT:
                game.player.move_right()
            if evt.key == pygame.K_LEFT:
                game.player.move_left()
            if evt.key == pygame.K_UP:
                game.player.move_up()
            if evt.key == pygame.K_DOWN:
                game.player.move_down()
            if evt.key == pygame.K_SPACE:
                game.player.lancer_bullet()
                Son()


pygame.quit()