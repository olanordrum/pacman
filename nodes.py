import pygame
import numpy as np
from vector import Vector2
from constants import *


class Node(object):
    def __init__(self,x,y):
        self.position = Vector2(x, y)
        self.neighbors = {UP:None, RIGHT:None, LEFT:None, RIGHT:None,}
        
        
    def render(self, screen):
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                line_start = self.position.asTuple()
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                pygame.draw.circle(screen, RED, self.position.asInt(), 12)
                

class NodeGroup(object):
    def __init__(self, level):
        self.level = level
        self.nodesLUT = {}
        self.nodeSymbols = ['+']
        self.pathSymbols = ['.']
        data = self.readMazeFile(level)
        self.crecreateNodeTable(data)
        self.connectHorizontally(data)
        self.connectVertically(data)
        
        
   
        
    def render(self, screen):
        #for node in self.nodeList:
        for node in self.nodesLUT.values():
            node.render(screen)
            
            
    def readMazeFile(self,textfile):
        return np.loadtxt(textfile, dtype='<U1')

   # Runs through a 2d - array[[rows][cols]]
    def crecreateNodeTable(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):       #shape[0] -> number of rows in grid
            for col in list(range(data.shape[1])):   #shape[1] -> number of cols in grid
                if data[row][col] in self.nodeSymbols:
                    x,y = self.constructKey(col+xoffset,row+yoffset)
                    self.nodesLUT[(x,y)] = Node(x,y)
                    
    def constructKey(self,x,y):
        return x * TILEWIDTH, y * TILEHEIGHT
    
    
    def connectHorizontally(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):
            key = None
            for col in list(range(data.shape[1])):
                if data[row][col] in self.nodeSymbols:
                    if key is None:
                        key = self.constructKey(col+xoffset, row+yoffset)
                        
                    else:
                        otherkey = self.constructKey(col+xoffset, row+yoffset)
                        self.nodesLUT[key].neighbors[RIGHT]= self.nodesLUT[otherkey]
                        self.nodesLUT[otherkey].neighbors[LEFT] = self.nodesLUT[key]
                        key = otherkey
                elif data[row][col] not in self.pathSymbols:
                    key = None
            
            
    def connectVertically(self, data, xoffset=0, yoffset=0):
        dataT = data.transpose()
        for col in list(range(dataT.shape[0])):
            key = None
            for row in list(range(dataT.shape[1])):
                if dataT[col][row] in self.nodeSymbols:
                    if key is None:
                        key = self.constructKey(col+xoffset, row+yoffset)
                    else:
                        otherkey = self.constructKey(col+xoffset, row+yoffset)
                        self.nodesLUT[key].neighbors[DOWN] = self.nodesLUT[otherkey]
                        self.nodesLUT[otherkey].neighbors[UP] = self.nodesLUT[key]
                        key = otherkey
                elif dataT[col][row] not in self.pathSymbols:
                    key = None
            
            
    def getNodeFromPixels(self, xpixel, ypixel):
        if(xpixel, ypixel) in self.nodesLUT.keys():
            return self.nodesLUT[(xpixel, ypixel)]
        return None
    
    def getNodeFromTiles(self, col, row):
        x, y = self.constructKey(col, row)
        if (x, y) in self.nodesLUT.keys():
            return self.nodesLUT[(x, y)]
        return None
    
    
    def getStartTemoNode(self):
        nodes = list(self.nodesLUT.values())
        return nodes[0]
    
    
