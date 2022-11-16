import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings,screen,ship,bullets):
    """Responde a eventos de acionamento de teclas e mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """Responde a pressionamento de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:                       # USANDO A TECLA q PARA SAIR DO JOGO
        sys.exit()
        
def check_keyup_events(event,ship):
    """Responde a soltura de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullets(ai_settings,screen,ship,bullets):
    """Dispara um projétil se o limite ainda não foi alcançado"""
    #Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza as posições dos projéteis
    bullets.update()
    # Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(ai_settings,alien_width):
    """Determina o numero de alienigenas que cabe em uma linha"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width + 1))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number):
    # Cria um alienígena e o posiciona na linha 
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens):
    """Cria uma frota completa de alienígenas."""
    # Cria um alienígena e calcula o número de alienígenas em uma linha
    # O espaçamento entre os alienígenas é igual à largura de um alienígena
    alien = Alien(ai_settings,screen)                                   # CRIA ALIENIGENA PARA O CALCULO (NAO ADICIONAR AO GRUPO)
    #alien_width = alien.rect.width                                      # OBTEMOS A LARGURA DO ALIENIGENA
    #available_space_x = ai_settings.screen_width - 2 * alien_width      # CALCULO DO ESPAÇO HORIZONTAL DISPONIVEL 
    #number_aliens_x = int(available_space_x / (2 * alien_width))        # NRO DE ALIENIGENA QUE CABEM NO RESTANTE DO ESPAÇO 
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width) 
    # Cria a primeira linha de alienígenas
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings,screen,aliens,alien_number)
        # Cria um alienígena e o posiciona na linha
        #alien = Alien(ai_settings,screen)
        #alien.x = alien_width + 2 * alien_width * alien_number
        #alien.rect.x = alien.x
        #aliens.add(alien)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    # Redesenha a tela a cada passagem pelo laço     
    screen.fill(ai_settings.bg_color)
    # Redesenha todos os projéteis atrás da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Adiciona a imagem da nave na tela com blit
    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)
    # Deixa a tela mais recente visivel
    pygame.display.flip()