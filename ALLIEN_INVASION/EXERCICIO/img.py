from turtle import screensize
import pygame

class Img():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('call.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        
