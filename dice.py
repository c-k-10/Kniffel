#=== Imports ===
import pygame
import random

#=== Klasse Dice ===
class Dice: 
    def __init__(self, value:int, fixed:bool, size:int, position:dict, color:str, x:int, y:int):
        self._value = value #Augenzahl des Würfels
        self.fixed = fixed #Boolean ob der Würfel fixiert wurde oder nicht
        self.size = size
        self.position = position
        self.color = color #Farbe des Würfels
        self.x = x #x-Koordinate
        self.y = y #y-Koordinate
        self.rect = pygame.Rect(self.x, self.y, 80,80) #Rechteck mit den Werten erstellen

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, v):
        self._value = v


    def roll_dice(self):
        """Die Funktion startet den Würfel‑Animationsvorgang, 
        sofern der Würfel nicht fixiert ist, indem sie die Animation aktiviert 
        und die Anzahl der Animations‑Frames setzt."""

        if self.fixed: 
            #Falls der Würfel fixiert ist, soll keine Animation stattfinden 
            return

        self.animating = True #Animation aktivieren 
        self.animation_frames = 5 #Animation dauert 5 Frames

  

    def draw(self, window, font):
        """Die Funktion zeichnet den Würfel, führt bei Bedarf die Roll‑Animation aus,
        markiert fixierte Würfel mit einem blauen Rahmen
        und rendert anschließend die passenden Punkte entsprechend des aktuellen Würfelwerts."""

        # === Animation ===
        if getattr(self, "animating", False):
            self.value = random.randint(1, 6)

            # Kleine Wackelbewegung während der Animation
            offset_x = random.randint(-30, 30)
            offset_y = random.randint(-30, 30)
            temp_rect = self.rect.move(offset_x, offset_y)

            pygame.time.delay(60)
            self.animation_frames -= 1

            if self.animation_frames <= 0:
                self.animating = False
                self.value = random.randint(1, 6)
                temp_rect = self.rect  # wieder normale Position
        else:
            temp_rect = self.rect

        # === Würfel-Hintergrund ===
        pygame.draw.rect(window, self.color, temp_rect, border_radius=8)

        # Fixierter Würfel → blauer Rahmen
        if self.fixed:
            pygame.draw.rect(window, (150, 220, 240), temp_rect, width=4, border_radius=8)

        # === Punkte zeichnen ===
        cx = temp_rect.x + temp_rect.width // 2
        cy = temp_rect.y + temp_rect.height // 2
        r = 6 #Radius
        
        #Position der Punkte für die jeweilige Zahl
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

        #Ausgabe/Zeichnen der Punkte der Würfel
        for (px, py) in positions[self.value]:
            pygame.draw.circle(window, "black", (px, py), r)
