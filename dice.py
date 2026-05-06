import pygame
import random

class Dice: 
    def __init__(self, value:int, fixed:bool, size:int, position:dict, color:str, x:int, y:int):
        self._value = value
        self.fixed = fixed
        self.size = size
        self.position = position
        self.color = color
        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, 80,80)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, v):
        self._value = v

    def roll_dice(self):
            if self.fixed == False:
                rand_num = random.randint(1,6)
                self.value = rand_num

    def show():
        pass

    def draw(self,win,font):
        if self.fixed == False:
            pygame.draw.rect(win,self.color,self.rect)
            text = font.render(str(self.value), True, "black")
            win.blit(text, (self.x + 30, self.y + 25))
        elif self.fixed == True:
            pygame.draw.rect(win,self.color,self.rect)
            pygame.draw.rect(win, (0, 0, 255), self.rect, width=4)
            text = font.render(str(self.value), True, "black")
            win.blit(text, (self.x + 30, self.y + 25))
  
