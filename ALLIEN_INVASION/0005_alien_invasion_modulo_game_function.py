# UTILIZANDO CLASS settings 

# import sys                        # nao é necessario importar sys que é usado em game_functions.py
import pygame
from settings import Settings                          
from ship import Ship                                      
import game_functions as gf                                 # importando modulo game_function

def run_game():
    # Inicializa o jogo e cria um objeto para a tela 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))     
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave
    ship = Ship(screen)

    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        gf.check_events(ship)

        # chamando update_screen()
        gf.update_screen(ai_settings,screen,ship)

run_game()