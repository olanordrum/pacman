import pygame
from vector import Vector2
from entity import Entity
from pygame.locals import *
from constants import *


class Pacman(Entity):
    def __init__(self, node):
        Entity.__init__(self, node )
        self.name = PACMAN
        self.color = YELLOW
        
        
        #dt -> time since last update
    def update(self,dt):
        self.position += self.directions[self.direction] * self.speed * dt
        direction = self.getValidKey()
        
        
        if self.overshotTarget():
            self.node = self.target
            self.target = self.getNewTarget(direction)
            
            if self.target is not self.node:
                self.direction = direction
            else:
                self.target = self.getNewTarget(self.direction)
                
            if self.target is self.node:
                self.direction = STOP
            self.setPosition()
            
        else:
            if self.oppositeDirection(direction):
                self.reverseDirection()
        

    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        return STOP
    
    
    # Draw pacman
    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen,self.color,p,self.radius)