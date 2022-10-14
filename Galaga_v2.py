#import libraries
import pgzrun
import pygame as pg
import random

#screen dimensions
WIDTH = 1100
HEIGHT = 850

#definining colors for our game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#create ship
ship = Actor('ship.png')
#specify initial position of ship
ship.x = WIDTH // 2
ship.y = HEIGHT - 100
ship.dead = False
ship.countdown = 120

#define a list for bullets
bullets = []

#define a list for enemies - making enemies
#defining enemy behavior
enemies = []
enemies_2 = []

for x in range (2):
	enemies.append(Actor('fireball.png'))
	enemies[-1].x = random.randint(40, WIDTH-40)
	enemies[-1].y = random.randint(-550, -50)

for x in range (1):
	enemies.append(Actor('pacman.png'))
	enemies[-1].x = random.randint(40, WIDTH-40)
	enemies[-1].y = random.randint(-550, -50)

for x in range (2):
	enemies_2.append(Actor('bug.png'))
	enemies_2[-1].x = random.randint(40, WIDTH-40)
	enemies_2[-1].y = random.randint(-550, -50)

for x in range (1):
	enemies_2.append(Actor('blue.png'))
	enemies_2[-1].x = random.randint(40, WIDTH-40)
	enemies_2[-1].y = random.randint(-550, -50)


#updating game score
score = 0 

def drawScore():
	screen.draw.text(str(score), (50, 30), fontsize=120)

#configuring key controls and object movements
def on_key_down(key):
	if ship.dead== False:
		if key == keys.SPACE:
			bullets.append(Actor('bullet.png'))
			bullets[-1].x = ship.x 
			bullets[-1].y = ship.y - 75

def update():
	global score
	#ship left/right movement and speed
	if ship.dead == False:
		if keyboard.left: 
			ship.x -= 15
		elif keyboard.right:
			ship.x += 15
		#once enemies are defeated then fly off the screen
		elif len(enemies) == 0 and len(enemies_2) == 0:
			ship.y -= 10 

	for bullet in bullets:
		if bullet.y < -20:
			bullets.remove(bullet)
		else:
			bullet.y -= 15         

	#enemy 1
	for enemy in enemies:
		enemy.y += 15
		if enemy.y > HEIGHT + 60:
			enemy.y = -100
			enemy.x = random.randint(40, WIDTH - 40)
		#bullet collision with enemy
		for bullet in bullets:
			if enemy.colliderect(bullet):
				score += 50
				bullets.remove(bullet)
				enemies.remove(enemy)
		#enemy collision with ship
		if enemy.colliderect(ship):
				ship.dead = True
		#time for ship to respawn after collision 
		if ship.dead:
			ship.countdown -= 1
		if ship.countdown == 0:
			ship.dead = False
			ship.countdown = 90

	#enemy 2 - bug moving slower
	for enemy in enemies_2:
		enemy.y += 10
		if enemy.y > HEIGHT + 60:
			enemy.y = -100
			enemy.x = random.randint(40, WIDTH - 40)
		#bullet collision with enemy
		for bullet in bullets:
			if enemy.colliderect(bullet):
				score += 50
				bullets.remove(bullet)
				enemies_2.remove(enemy)
		#enemy collision with ship
		if enemy.colliderect(ship):
				ship.dead = True
		#time for ship to respawn after collision 
		if ship.dead:
			ship.countdown -= 1
		if ship.countdown == 0:
			ship.dead = False
			ship.countdown = 90

#background color and drawing objects on the screen
def draw():
	screen.clear()
	screen.fill(BLACK)

	for bullet in bullets:
		bullet.draw()
	for enemy in enemies:
		enemy.draw()
	for enemy in enemies_2:
		enemy.draw()
	if ship.dead == False:
		ship.draw()
	drawScore()


#run the game
pgzrun.go() 