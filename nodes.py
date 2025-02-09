import pygame
from vector import Vector2
from constants import *


class Node(object):
    def __init__(self,x,y):
        self.position = Vector2(x, y)
        self.neighbours = {UP:None,RIGHT:None,LEFT:None,RIGHT:None,}
        
        
    def render(self, screen):
        for n in self.neighbours.keys():
            if self.neighbours[n] is not None:
                line_start = self.position.asTuple()
                line_end = self.neighbours[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                pygame.draw.circle(screen, RED, self.position.asInt(), line_end, 12)
