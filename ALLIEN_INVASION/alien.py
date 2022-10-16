from turtle import screensize
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um único aligena da frota"""
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        #Inicia cada novo alienigena na parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienigena em sua posição atual"""
        self.screen.blit(self.image,self.rect)

