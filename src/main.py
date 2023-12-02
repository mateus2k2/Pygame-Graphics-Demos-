import pygame

class GlobalVars:
    def __init__(self):
        self.lineColorR = 100
        self.lineColorG = 255
        self.lineColorB = 50
        self.lineThickness = 6
        self.targetFPS = 60
        self.slowMode = False
        
        self.corFundo = (228, 230, 246)
        self.disp_size = (1150, 800)
        
        self.corLoadingText = (104, 153, 180)
    
Cosmetics = GlobalVars()

pygame.init()
surface = pygame.display.set_mode(Cosmetics.disp_size)
pygame.display.set_caption('Grafica')
clock = pygame.time.Clock()

reconstruir = []
dataTela = None