#pingbong in progress

import pygame

pygame.init()
pygame.font.init()

screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))

myfont =  pygame.font.SysFont('Helvetica', 50)

FPS = 60
ROUND_DELAY = 1 

class Player:
	def __init__(self, pos_x, mode):
		self.mode = mode
		self.pos_x = pos_x
		self.height = 60
		self.pos_y = screen_height//2 - self.height // 2
		self.color = (0,255,0)
		self.rect = None
		self.score = 0

	def draw(self):
		self.rect = pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, 13,self.height))

	def movement(self, keys):
		if keys[pygame.K_q]:
			pygame.quit()
		elif self.mode == 1:
			if keys[pygame.K_w] and self.pos_y > 0:
				self.pos_y -= 10
			if keys[pygame.K_s] and self.pos_y < screen_height - self.height:
				self.pos_y += 10
		elif self.mode == 2:
			if keys[pygame.K_UP] and self.pos_y > 0:
				self.pos_y -= 10
			if keys[pygame.K_DOWN] and self.pos_y < screen_height - self.height:
				self.pos_y += 10
		else:
			pass

class Ball:
	def __init__(self):
		self.size = 15
		self.color = (0,0,160)
		self.pos_x, self.pos_y = screen_width//2, screen_height//2
		self.speed = 5
		self.direction = "L"
		self.rect = None

	def draw(self):
		self.rect = pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)

	def movement(self):
		if self.direction == "R":
			self.pos_x += self.speed
		if self.direction == "L":

	def check_collision(self, p1, p2):
		if p1.rect.colliderect(self.rect):
			self.direction = "R"
		elif p2.rect.colliderect(self.rect):
			self.direction = "L"

	def check_win(self, p1, p2):
		if self.pos_x < 0 - self.size:
			p2.score += 1
			main()
		if self.pos_x > screen_width + self.size:
			p1.score += 1
			main()

def middle():
	pygame.draw.rect(screen, (255,0,0), (screen_width//2 - 2.5, 0, 5, screen_height))

def draw_points(p1,p2):
	p1_points = myfont.render(str(p1.score), 1, ((255,255,255)))
	p2_points = myfont.render(str(p2.score), 1, ((255,255,255)))
	screen.blit(p1_points, (20,20))
	screen.blit(p2_points, (547,20))

p1 = Player(0,1)
p2 = Player(screen_width-13, 2)
def main():
	clock = pygame.time.Clock()

	ball = Ball()
	run = True
	while run:
		clock.tick(FPS)
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
		
		screen.fill((0,0,0))
		middle()
		ball.draw()
		ball.movement()
		p1.draw()
		p2.draw()
		draw_points(p1,p2)
		p1.movement(keys)
		p2.movement(keys)
		ball.check_collision(p1,p2)
		ball.check_win(p1,p2)
		pygame.display.flip()
	
main()
