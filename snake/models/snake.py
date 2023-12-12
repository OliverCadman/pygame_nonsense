
import pygame as pg

class Snake:
    
    def __init__(self):
        self.position = [100, 50]
        self.body = [
            [100,50],
            [90, 50],
            [80, 50],
            [70, 50],
            [60, 50]
        ]
        self.color = (255, 255, 255)
        self.width = 10
        self.height = 10
    
    def insert(self):
        return self.body.insert(0, list(self.position))
    
    def pop(self):
        return self.body.pop()

    def draw(self, screen):
        return [
            pg.draw.rect(screen, self.color, 
                         pg.Rect(pos[0], pos[1], 
                         self.width, self.height
                    )
                ) for pos in self.body
            ]
    