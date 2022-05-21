import pgzrun
import time
import random


def fire_laser():
    laser.topright = spaceship.topright
    laser.x += -5
    sounds.missile.set_volume(.05)
    sounds.missile.play()


def show_asteroid():
    asteroid.topright = (random.randint(0, WIDTH), 0)


def show_space_station():
    space_station.topright = -600, 500
    #space_station.topright = (random.randint(0, WIDTH) + 50, -50)


def move_asteroid():
    global level
    if asteroid.y < HEIGHT+100:
        asteroid.y += 2 + level
    else:
        asteroid.topright = (random.randint(0, WIDTH), 0)


def move_space_station():
    if space_station.y < HEIGHT+100:
        space_station.y += .1
    else:
        show_space_station()

def move_laser():
    if laser.y > -5:
        laser.y -= 10
        firing = False


def check_collisions():
    global score
    
    for alien in aliens:
        if laser.distance_to(alien) < 30:
            
            explosion.center = alien.topright
            alien.x = 1200
            explosion.draw()
            animate(explosion, duration=6, pos=(explosion.x, explosion.y))
            sounds.explosion_3.set_volume(.05)
            sounds.explosion_3.play()
            alien.x = random.randint(30, 350)
            alien.y = 20
            score += 10
        else:
            if alien.x < WIDTH:
                alien.draw()
        if alien.distance_to(spaceship) < 60:
            explosion.center = spaceship.center
            spaceship.x = WIDTH + 100
            explosion.draw()
            animate(explosion, duration=6, pos=(explosion.x, explosion.y))
            sounds.explosion_3.set_volume(.05)
            sounds.explosion_3.play()

    if laser.distance_to(asteroid) < 19:
        explosion.center = asteroid.topright
        asteroid.x = 1200
        explosion.draw()
        animate(explosion, duration=6, pos=(explosion.x, explosion.y))
        sounds.explosion_3.set_volume(.05)
        sounds.explosion_3.play()
        # ghost.x = random.randint(30, 350)
        # ghost.y = 20
        score += 5
        
    if spaceship.distance_to(asteroid) < 150:
        explosion.center = spaceship.center
        explosion.draw()
        animate(explosion, duration=146, pos=(explosion.x, explosion.y))
        sounds.explosion_3.set_volume(.05)
        sounds.explosion_3.play()
        spaceship.x = WIDTH + 100
        score = score - 50
        if score < 0:
            score = 0
    else:
        if spaceship.x < WIDTH:
            spaceship.draw()


def check_level():
    global level
    global level_show_counter
    global aliens

    if level == 1 and score > 100:
        sounds.level_up.play()
        level = 2
        level_show_counter = level_show_counter + 1
        screen.draw.text("Level UP! " + str(level), pos=(level_show_counter * .1 + 50, 500), fontsize=80)

        screen.draw.text("Level UP! " + str(level), pos=(level_show_counter * .1 + 50, 500), fontsize=80)
        screen.draw.text("Level UP! " + str(level), pos=(level_show_counter * .1 + 50, 500), fontsize=80)
        alien = Actor('alien_spaceship2')
        alien.topright = 200, 10
        aliens.append(alien)
    if level_show_counter >=2000:
            level_show_counter = 1


    if level == 2 and score > 200:
        sounds.level_up.play()
        level = 3
        level_show_counter = level_show_counter + 1
        screen.draw.text("Level UP! " + str(level), pos=(level_show_counter * .1 + 50, 500), fontsize=80)
        screen.draw.text("Level UP! " + str(level), pos=(level_show_counter * .1 + 50, 500), fontsize=80)
        screen.draw.text("Level UP! " + str(level), pos=(level_show_counter * .1 + 50, 500), fontsize=80)
        alien = Actor('alien_spaceship2')
        alien.topright = 200, 10
        aliens.append(alien)
    if level_show_counter >=2000:
            level_show_counter = 1

    if level == 3 and score > 300:
        sounds.level_up.play()
        level = 4
        level_show_counter = level_show_counter + 1
        screen.draw.text("Level UP! " + str(level), pos=(level_show_counter*.1+50, 500), fontsize=80)
        screen.draw.text("Level UP! " + str(level), pos=(level_show_counter * .1 + 50, 500), fontsize=80)
        screen.draw.text("Level UP! " + str(level), pos=(level_show_counter * .1 + 50, 500), fontsize=80)
        alien = Actor('alien_spaceship2')
        alien.topright = 200, 10
        aliens.append(alien)
        if level_show_counter >=2000:
            level_show_counter = 1


def update():
    global score
    global level
    global level_show_counter
    a = 1
    moverand()
    move_laser()
    move_asteroid()
    move_space_station()
    asteroid.angle -= 1
    check_collisions()
    check_level()
    for alien in aliens:
        if alien.y > HEIGHT:
            alien.y = 10
        if alien.x < 0 or alien.x > WIDTH +100:
            alien.x = random.randint(0, WIDTH)
            alien.y = 0
    
    if keyboard.left:
        spaceship.left -= 7
    if keyboard.right:
        spaceship.left += 7

    if keyboard.a:
        ghost.left -= 4
    if keyboard.s:
        ghost.right += 4
    if keyboard.space:
        if laser.y < 0:
            firing = True
            fire_laser()
            #clock.schedule(fire_laser, 0.1)
    screen.draw.text("Score " + str(score), pos=(800, 10))
    screen.draw.text("Level " + str(level), pos=(800, 40))


def create_aliens():
    num_aliens = 1
    for alien_num in range(0, num_aliens):
        alien = Actor('alien_spaceship2')
        alien.topright = 200, 10
        aliens.append(alien)
    # alien = Actor('alien_spaceship2')
    # alien.topright = 200, 10
    # ghost2 = Actor('alien_spaceship2')
    # ghost2.topright = 200, 10
    # ghost3 = Actor('alien_spaceship2')
    # ghost3.topright = 200, 10
    # ghost4 = Actor('ufo')
    # ghost4.topright = 200, 10


def moverand():
    import random
    for ghost in aliens:
        ghost.left += random.randint(-7, 7)
        ghost.y += random.randint(-1, 3)


def on_mouse_move(rel, buttons):
    x, y = rel

    if x < 0:
        spaceship.left -= 4

    if x > 0:
        spaceship.left += 4


def draw():
    screen.clear()
    screen.blit("stars", (0, 0))
    space_station.draw()
    laser.draw()
    spaceship.draw()
    asteroid.draw()
    update()

import pygame
#background = pygame.image.load("./images/stars.jpeg")
#blit("background",(0,0))
WIDTH = 1000
HEIGHT = 800
firing = False
level_show_counter = 0
aliens = []

spaceship = Actor('spaceship_small')
spaceship.topright = WIDTH / 2, HEIGHT - 130

# ghost = Actor('alien_spaceship2')
# ghost.topright = 200, 10
# ghost2 = Actor('alien_spaceship2')
# ghost2.topright = 200, 10
# ghost3 = Actor('alien_spaceship2')
# ghost3.topright = 200, 10
# ghost4 = Actor('ufo')
# ghost4.topright = 200, 10
#
#
# aliens.append(ghost)
# aliens.append(ghost2)
# aliens.append(ghost3)
# aliens.append(ghost4)
asteroid = Actor('asteroid')
asteroid.topright = 1500, 0

laser = Actor('shot')
explosion = Actor('explosion')

space_station = Actor('space_station')

score = 0
level = 1
create_aliens()

time.sleep(20)

music.play('futuristic-timelapse-11951')
music.set_volume(.1)

pgzrun.go()


