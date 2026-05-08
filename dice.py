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


    def roll_dice(self):
        if self.fixed:
            return

        self.animating = True
        self.animation_frames = 5

  

    def draw(self, window, font):
        # === Animation ===
        if getattr(self, "animating", False):
            import random
            self.value = random.randint(1, 6)

            # ⭐ Animation verlangsamen
            pygame.time.delay(60)   # 60 ms pro Frame → schön langsam

            self.animation_frames -= 1

            if self.animation_frames <= 0:
                self.animating = False
                self.value = random.randint(1, 6)

        # === Würfel-Hintergrund ===
        pygame.draw.rect(window, "white", self.rect, border_radius=8)

        # ⭐ Fixierter Würfel → blauer Rahmen
        if self.fixed:
            pygame.draw.rect(window, (0, 0, 255), self.rect, width=4, border_radius=8)

        # === Punkte zeichnen ===
        cx = self.rect.x + self.rect.width // 2
        cy = self.rect.y + self.rect.height // 2
        r = 6

        positions = {
            1: [(cx, cy)],
            2: [(cx - 20, cy - 20), (cx + 20, cy + 20)],
            3: [(cx - 20, cy - 20), (cx, cy), (cx + 20, cy + 20)],
            4: [(cx - 20, cy - 20), (cx + 20, cy - 20),
                (cx - 20, cy + 20), (cx + 20, cy + 20)],
            5: [(cx - 20, cy - 20), (cx + 20, cy - 20),
                (cx, cy),
                (cx - 20, cy + 20), (cx + 20, cy + 20)],
            6: [(cx - 20, cy - 20), (cx + 20, cy - 20),
                (cx - 20, cy),     (cx + 20, cy),
                (cx - 20, cy + 20), (cx + 20, cy + 20)],
        }

        for (px, py) in positions[self.value]:
            pygame.draw.circle(window, "black", (px, py), r)



