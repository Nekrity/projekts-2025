import pygame

class SpriteSheet_Player():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, width, height, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), (5, 16, width, height))
		image.set_colorkey(colour)

		return image
class SpriteSheet_Buttons():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, width, height, colour,num):
		if num>1:
			defect=111+(num-1)*101
		else:
			defect=9+num*102
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), (8, (defect), width, height))
		image.set_colorkey(colour)

		return image
class SpriteSheet_Asgore():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, start_width, start_height, width, height, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), (start_width, start_height, width, height))
		image = pygame.transform.scale(image, (width * 2, height * 2))
		image.set_colorkey(colour)

		return image
class SpriteSheet_Textbubble():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, width, height, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), (21, 18, width, height))
		image.set_colorkey(colour)

		return image
#110 102
#360 286

#cape width 360 height 227
