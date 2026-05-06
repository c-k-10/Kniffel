import pygame

class Scorecard:
    def __init__(self, name, value, y):
        self.name = name
        self.value = value
        self.rect = pygame.Rect(970, y, 300, 50)

    def has_bonus():
        pass

    def sum():
        pass

    def score_points_on_scorecard():
        pass

    def draw(self, win, font):
        #Rechteck zeichnen
        pygame.draw.rect(win, (40, 40, 40), self.rect)
        #Name schreiben 
        name_text = font.render(self.name, True, (255, 255, 255))
        #Value schreiben
        val_text = font.render(str(self.value), True, (255, 255, 255))

        win.blit(name_text, (self.rect.x + 10, self.rect.y + 8))
        win.blit(val_text, (self.rect.right - 40, self.rect.y + 8))