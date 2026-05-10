import pygame

class Scorecard:
    def __init__(self, name, value, y, possible:bool,possible_value:int, locked, game):
        self.name = name
        self.value = value
        self.rect = pygame.Rect(game.width - (game.width / 100 * 25), y, 300, 50)
        self.possible = possible
        self.possible_value = possible_value
        self.locked = locked

    def draw(self, win, font):
        if self.possible == True:
            pygame.draw.rect(win, (40, 40, 40), self.rect)
            pygame.draw.rect(win, (0, 0, 255), self.rect, width=4)
            #Name schreiben 
            name_text = font.render(self.name, True, (255, 255, 255))
            #Value schreiben
            val_text = font.render(str(self.possible_value), True, (255, 255, 255))

            win.blit(name_text, (self.rect.x + 10, self.rect.y + 8))
            win.blit(val_text, (self.rect.right - 40, self.rect.y + 8))
        elif self.locked == True:
            #Rechteck zeichnen
            pygame.draw.rect(win, (40, 40, 40), self.rect)
            #Name schreiben 
            name_text = font.render(self.name, True, (0, 0, 0))
            #Value schreiben
            val_text = font.render(str(self.value), True, (0, 0, 0))

            win.blit(name_text, (self.rect.x + 10, self.rect.y + 8))
            win.blit(val_text, (self.rect.right - 40, self.rect.y + 8))
        else:
        #Rechteck zeichnen
            pygame.draw.rect(win, (40, 40, 40), self.rect)
            #Name schreiben 
            name_text = font.render(self.name, True, (255, 255, 255))
            #Value schreiben
            val_text = font.render(str(self.value), True, (255, 255, 255))

            win.blit(name_text, (self.rect.x + 10, self.rect.y + 8))
            win.blit(val_text, (self.rect.right - 40, self.rect.y + 8))


    def possible_score(self, counts, values, total):

        # Wenn die Zeile schon eingetragen wurde → nichts berechnen
        if self.locked:
            self.possible = False
            self.possible_value = 0
            return

        name = self.name

        # Einser–Sechser
        if name in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]:
            number = ["Einser","Zweier","Dreier","Vierer","Fünfer","Sechser"].index(name) + 1
            value = counts[number] * number
            self.possible_value = value
            self.possible = value > 0
            return

        # Dreierpasch
        if name == "Dreierpasch":
            self.possible = max(counts) >= 3
            self.possible_value = total if self.possible else 0
            return

        # Viererpasch
        if name == "Viererpasch":
            self.possible = max(counts) >= 4
            self.possible_value = total if self.possible else 0
            return

        # Full House
        if name == "Full House":
            self.possible = (3 in counts and 2 in counts)
            self.possible_value = 25 if self.possible else 0
            return

        # Kleine Straße
        if name == "Kleine Straße":
            small = [{1,2,3,4},{2,3,4,5},{3,4,5,6}]
            self.possible = any(s.issubset(values) for s in small)
            self.possible_value = 30 if self.possible else 0
            return

        # Große Straße
        if name == "Große Straße":
            self.possible = set(values) in [{1,2,3,4,5},{2,3,4,5,6}]
            self.possible_value = 40 if self.possible else 0
            return

        # Kniffel
        if name == "Kniffel":
            self.possible = max(counts) == 5
            self.possible_value = 50 if self.possible else 0
            return

        # Chance
        if name == "Chance":
            self.possible = True
            self.possible_value = total
            return
