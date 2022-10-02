class Settings():
    """Uma classe para armazenar todas as configurações da invasão alienigena."""
    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        # Configuração da espeçonave
        self.ship_speed_factor = 1.5
        # Configurações dos projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
