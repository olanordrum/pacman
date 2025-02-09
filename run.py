import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman 
from nodes import Node
from nodes import NodeGroup


class GameColtroller(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE,0,32)
        self.background = None
        self.clock = pygame.time.Clock()
        
        
    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE)
        self.background.fill(BLACK)
        

        
    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)
        self.checkEvents()
        self.render()
        
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                
    def startGame(self):
        self.setBackground()
        self.nodes = NodeGroup()
        self.nodes.setupTestNodes()
        self.pacman = Pacman(self.nodes.nodeList[0])
    
    
    def render(self):
        self.screen.blit(self.background,(0, 0))
        self.nodes.render(self.screen)
        self.pacman.render(self.screen)
        pygame.display.update()
        
        


        
        

if __name__ == "__main__":
    game = GameColtroller()
    game.startGame()
    while True:
        game.update()     