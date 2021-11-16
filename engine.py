import pygame

class Game:
    def __init__(self, title, width, height, start, update):
        self.screen = pygame.display.set_mode((width, height), 0, 32)
        self.title = title
        self.width = width
        self.height = height
        self.start = start
        self.update = update

        self.start()
        self.update()
    

