import pygame

class Scorecard:
    def __init__(self, name, value, y, possible:bool,possible_value:int, locked, game):
        self.name = name
        self.value = value
        self.rect = pygame.Rect(game.width - (game.width / 100 * 25), y, 300 + game.font_size, game.font_size + game.font_size * 1.2)
        self.possible = possible
        self.possible_value = possible_value
        self.locked = locked

    def draw(self, win, font, y):
        self.rect.y = y
        if self.possible == True:
            pygame.draw.rect(win, (30, 36, 46), (self.rect))
            pygame.draw.rect(win, (174, 239, 255), (self.rect), width=4)
            #Name schreiben 
            name_text = font.render(self.name, True, (230, 230, 230))
            #Value schreiben
            val_text = font.render(str(self.possible_value), True, (230, 230, 230))

            # Name links
            name_text = font.render(self.name, True, (230, 230, 230))
            name_rect = name_text.get_rect(midleft=(self.rect.x + 10, self.rect.centery))
            win.blit(name_text, name_rect)

            # Wert rechts
            val_text = font.render(str(self.possible_value), True, (230, 230, 230))
            val_rect = val_text.get_rect(midright=(self.rect.right - 10, self.rect.centery))
            win.blit(val_text, val_rect)

        elif self.locked == True:
            #Rechteck zeichnen
            pygame.draw.rect(win, (55, 60, 70), (self.rect))
            #Name schreiben 
            name_text = font.render(self.name, True, (140, 140, 140))
            #Value schreiben
            val_text = font.render(str(self.value), True, (140, 140, 140))

            # Name links
            name_text = font.render(self.name, True, (140, 140, 140))
            name_rect = name_text.get_rect(midleft=(self.rect.x + 10, self.rect.centery))
            win.blit(name_text, name_rect)

            # Wert rechts
            val_text = font.render(str(self.value), True, (140, 140, 140))
            val_rect = val_text.get_rect(midright=(self.rect.right - 10, self.rect.centery))
            win.blit(val_text, val_rect)
        else:
        #Rechteck zeichnen
            pygame.draw.rect(win, (30, 36, 46), (self.rect))
            #Name schreiben 
            name_text = font.render(self.name, True, (230, 230, 230))
            #Value schreiben
            val_text = font.render(str(self.value), True, (230, 230, 230))

            # Name links
            name_text = font.render(self.name, True, (230, 230, 230))
            name_rect = name_text.get_rect(midleft=(self.rect.x + 10, self.rect.centery))
            win.blit(name_text, name_rect)

            # Wert rechts
            val_text = font.render(str(self.value), True, (230, 230, 230))
            val_rect = val_text.get_rect(midright=(self.rect.right - 10, self.rect.centery))
            win.blit(val_text, val_rect)

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
