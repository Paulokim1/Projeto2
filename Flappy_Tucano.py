#Blibiotecas importadas
import pygame
import random

#Iniciação do código
pygame.init()

#Especificações sobre a janela e o seu Título
WIDTH = 800
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Tucano')

#Inicia assets
TUCANO_WIDTH = 70
TUCANO_HEIGHT = 70
TRONCO_WIDTH = 100
TRONCO_HEIGHT = random.randint(0,300)
TRONCO_INVERTIDO_WIDTH = TRONCO_WIDTH
TRONCO_INVERTIDO_HEIGHT = 500-TRONCO_HEIGHT-120

TUCANO = pygame.image.load('tucano2.png').convert_alpha()
TUCANO = pygame.transform.scale(TUCANO, (TUCANO_WIDTH, TUCANO_HEIGHT))

FUNDO = pygame.image.load('wallpaper.jpg').convert()
FUNDO = pygame.transform.scale(FUNDO,(WIDTH,HEIGHT))

TRONCO = pygame.image.load('tronco.jpg').convert_alpha()
TRONCO = pygame.transform.scale(TRONCO,(TRONCO_WIDTH,TRONCO_HEIGHT))

TRONCO_INVERTIDO = pygame.transform.flip(TRONCO,True,True)

SPEED = 10

GRAVITY = 1 
#inicia sprites
class Tucano(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = TUCANO
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH/2
		self.rect.bottom = HEIGHT/2
		self.speed = SPEED*2

	def update(self):
		self.speed += GRAVITY
		self.rect.y += self.speed

<<<<<<< HEAD
class Tronco(pygame.sprite.Sprite):
 	def __init__(self):
 		pygame.sprite.Sprite.__init__(self)
 		self.image = TRONCO
 		self.rect = self.image.get_rect()
=======
	def pulo(self):
		self.speed = -SPEED*1.5
# class Tronco(pygame.sprite.Sprite):
# 	def __init__(self):
# 		pygame.sprite.Sprite.__init__(self)

# 	self.image = TRONCO 
# 	self.rect = self.image.get_rect()
>>>>>>> 26ecdc276dd59e311e611fc78c5b29fab5c0278b

class Tronco_invertido(pygame.sprite.Sprite):
	def __init__(self):
 		pygame.sprite.Sprite.__init__(self)
 		self.image = TRONCO_INVERTIDO
 		self.rect = self.image.get_rect()

sprite_group = pygame.sprite.Group()
player_tucano = Tucano()
sprite_tronco = Tronco()
sprite_tronco_invertido = Tronco_invertido()
sprite_group.add(player_tucano)
sprite_group.add(sprite_tronco)
sprite_group.add(sprite_tronco_invertido)
sprite_group.add()

clock = pygame.time.Clock()
FPS = 30
#Loop principal
GAME = True

while GAME:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GAME = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player_tucano.pulo()

	WINDOW.blit(FUNDO, (0,0))
	
	sprite_group.draw(WINDOW)
	sprite_group.update()

	pygame.display.update()

#Finalização do código
pygame.quit()