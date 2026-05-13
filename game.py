#=== Imports ===
import pygame
import scorecard
import cup
import dice
import player
import math
#=== Klasse Game ===
class Game:
    def __init__(self):
        #Pygame Initalisierung
        pygame.init()
        pygame.display.set_caption("Kniffel")
        self.window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.running = True
        self.width = self.window.get_width()
        self.height = self.window.get_height()

        #Basisauflösung für Skalierung
        BASE_WIDTH = 1920
        BASE_HEIGHT = 1080

        scale_x = self.width / BASE_WIDTH
        scale_y = self.height / BASE_HEIGHT
        self.scale = min(scale_x, scale_y) 

        #Button
        self.button = pygame.Rect(self.width * 0.20 - 65, self.height * 0.67 ,130,50)

        #Schriftarten        
        self.font_size = int(32 * self.scale)
        self.font = pygame.font.SysFont("calibri", self.font_size, bold=True)
        self.head_font = pygame.font.SysFont("calibri", self.font_size + 15, bold=True)
       
        #Kreis
        self.circle_radius = int(250 + (self.height / 100 * 1))
        self.current_player = 0
        self.rolls_left = 2
        self.dices = []
        self.player_list = []
        self.dice_cup = cup.Cup(self.dices)

    def create_scoreboard(self):
        """Die Funktion erzeugt eine vollständige Liste aller Scoreboard‑Einträge für Kniffel, 
        wobei jeder Eintrag mit Namen, Startwerten und seiner festen Bildschirmposition initialisiert wird."""
        return [
        scorecard.Scorecard("Einser", 0, 60, False,0,False, self),
        scorecard.Scorecard("Zweier", 0, 120, False,0,False, self),
        scorecard.Scorecard("Dreier", 0, 180, False,0,False, self),
        scorecard.Scorecard("Vierer", 0, 240, False,0,False, self),
        scorecard.Scorecard("Fünfer", 0, 300, False,0,False, self),
        scorecard.Scorecard("Sechser", 0, 360, False,0,False, self),
        scorecard.Scorecard("Dreierpasch", 0, 420, False,0,False, self),
        scorecard.Scorecard("Viererpasch", 0, 480, False,0,False, self),
        scorecard.Scorecard("Full House", 0, 540, False,0,False, self),
        scorecard.Scorecard("Kleine Straße", 0, 600, False,0,False, self),
        scorecard.Scorecard("Große Straße", 0, 660, False,0,False, self),
        scorecard.Scorecard("Kniffel", 0, 720, False,0,False, self),
        scorecard.Scorecard("Chance", 0, 780, False,0,False, self),
        ]
    
    def create_dices(self):
        """Diese Funktion erzeugt fünf Würfel und positioniert sie kreisförmig um das Zentrum."""
        center_x = self.width * 0.20 
        center_y = self.height * 0.35
        radius = 130      
        offset = 40

        # 5 gleichmäßig verteilte Winkel (360° / 5 = 72°)
        angles = [90, 162, 234, 306, 18]  

        for i, angle in enumerate(angles):
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * radius - offset
            y = center_y + math.sin(rad) * radius - offset
            self.dices.append(
                dice.Dice(i+1, False, 20, {"x": 10, "y": 10}, (255,255,255), int(x), int(y))
            )

    def create_player_list(self):
        """Diese Funktion erstellt die Spielerliste, indem zuerst die Spieleranzahl abgefragt 
        und anschließend für jeden Spieler ein Name eingeholt und ein Player‑Objekt erzeugt wird."""
        player_number = self.choose_player_count(self.window, self.font, self.head_font)

        for i in range(player_number):
            name = self.get_player_name(self.window, self.font, i+1)
            self.player_list.append(player.Player(self.create_scoreboard(), name, False, "easy", False, 0))
    
    def main_game(self):
        self.create_dices()
        self.create_player_list()
       
        for i in range(len(self.dices)):
            self.dices[i].roll_dice()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                #Bei Escape wird die Fester auf geschlossen
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                    self.running = False

                #Button Würfeln bedrückt
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.collidepoint(event.pos):
                        if self.rolls_left > 0:
                            self.rolls_left = self.rolls_left - 1
                            for i in range(len(self.dices)):
                                self.dices[i].roll_dice()
                                self.dices[i].roll_dice()
                                
                #Auf einen Würfel gedrückt um ihn zu fixieren
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for dice in self.dices:
                        if dice.rect.collidepoint(event.pos):
                            if dice.fixed == True:
                                dice.fixed = False
                            else:
                                dice.fixed = True
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for row in self.player_list[self.current_player].scorecard:
                        if row.rect.collidepoint(event.pos):
                            if row.locked == False:
                                row.value = row.possible_value
                                row.locked = True

                                if all(r.locked for r in self.player_list[self.current_player].scorecard) == True:
                                    self.player_list[self.current_player].sum_score()
                                    
                                    
                                if all(all(row.locked for row in p.scorecard) for p in self.player_list):
                                    self.won(self.window, self.font, self.player_list)

                                self.current_player = (self.current_player + 1) % len(self.player_list)
                                self.rolls_left = 2

                                for d in self.dices:
                                    d.fixed = False

                                for i in range(len(self.dices)):
                                    self.dices[i].roll_dice()
                                

            #Hintergrundfarbe
            self.draw_vertical_gradient((18, 22, 28), (23, 27, 33))

            #Würfelfeld zeichnen
            pygame.draw.circle(self.window, (40, 120, 95), (self.width * 0.20, self.height * 0.35), self.circle_radius)
            pygame.draw.circle(self.window, (78, 52, 39), (self.width * 0.20, self.height * 0.35), self.circle_radius, 20)

            #Spielernamen ausgeben
            player_text = self.font.render(f"Spieler: {self.player_list[self.current_player].name}", True, (255,255,255))
            self.window.blit(player_text, (550, 120))

            #Übrige Würfe anzeigen
            roll_text = self.font.render(f"Würfe übrig: {self.rolls_left}", True, (174, 239, 255))
            self.window.blit(roll_text, (550, 160))

            #Würfel zeichnen
            for i in range(len(self.dices)):
                self.dices[i].draw(self.window,self.font)

            start_y = self.height * 0.10
            spacing = 57 + self.scale

            for index, row in enumerate(self.player_list[self.current_player].scorecard):
                counts, values, total = self.dice_cup.counts()
                row.possible_score(counts, values, total)

                y = start_y + index * spacing
                row.draw(self.window, self.font, y)


            #Button für würfeln
            pygame.draw.rect(self.window, "white", self.button)

            text = self.font.render("Würfeln", True, (0, 0, 0))
            text_rect = text.get_rect(center=self.button.center)
            self.window.blit(text, text_rect)
        
            pygame.display.update()

    def choose_player_count(self, window, font, head_font):
        """Die Funktion zeigt ein Auswahlmenü an, 
        in dem der Spieler per Mausklick die gewünschte Spieleranzahl wählen kann, 
        und gibt diese anschließend zurück."""

        start_y = self.height * 0.25
        spacing = self.height * 0.07

        one_btn   = pygame.Rect(self.width * 0.20, start_y + spacing * 0, 300, self.font_size + 25)
        two_btn   = pygame.Rect(self.width * 0.20, start_y + spacing * 1, 300, self.font_size + 25)
        three_btn = pygame.Rect(self.width * 0.20, start_y + spacing * 2, 300, self.font_size + 25)
        four_btn  = pygame.Rect(self.width * 0.20, start_y + spacing * 3, 300, self.font_size + 25)

        game_info = (
        "Kniffel - Spielinfo\n\n"
        "Kniffel wird mit 5 Würfeln gespielt.\n"
        "Du hast pro Runde 3 Würfe und kannst \nnach jedem Wurf Würfel festhalten.\n"
        "Danach musst du eine Kategorie wählen.\n\n"
        "Oberer Teil:\n"
        "- Einser bis Sechser\n"
        "- Bonus ab 63 Punkten: +35 Punkte\n\n"
        "Unterer Teil:\n"
        "- Dreierpasch\n- Viererpasch\n- Full House (25 Punkte)\n"
        "- Kleine Straße (30 Punkte)\n"
        "- Große Straße (40 Punkte)\n"
        "- Kniffel (50 Punkte)\n"
        "- Chance\n\n"
        "Gewinner ist, wer die meisten Punkte hat."
        )

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if one_btn.collidepoint(event.pos): return 1
                    if two_btn.collidepoint(event.pos): return 2
                    if three_btn.collidepoint(event.pos): return 3
                    if four_btn.collidepoint(event.pos): return 4

            #Hintergrundfarbe
            self.draw_vertical_gradient((18, 22, 28), (23, 27, 33))


            #Aufgabe der Spiel Infos
            lines = game_info.split("\n")
            line_height = font.get_height() + 5
            for i, line in enumerate(lines):
                rendered = font.render(line, True, (230,230,230))
                window.blit(rendered, (self.width * 0.60, (self.height * 0.15) + i * line_height))

            #Ausgabe der Überschrift
            h_font = head_font.render("Willkommen bei Kniffel!", True, (174, 239, 255))
            window.blit(h_font, (self.width * 0.15,self.height * 0.10))

            #Ausgabe "Wie viele Spieler?"
            title = font.render("Wie viele Spieler?", True, (230,230,230))
            window.blit(title, (self.width * 0.20, self.height * 0.19))

            #Buttons anzeigen
            pygame.draw.rect(window, "white", one_btn)
            pygame.draw.rect(window, "white", two_btn)
            pygame.draw.rect(window, "white", three_btn)
            pygame.draw.rect(window, "white", four_btn)

            #Beschriftung der Button anzeigen
            window.blit(font.render("1 Spieler", True, (0,0,0)), (one_btn.x+40, one_btn.y+10))
            window.blit(font.render("2 Spieler", True, (0,0,0)), (two_btn.x+40, two_btn.y+10))
            window.blit(font.render("3 Spieler", True, (0,0,0)), (three_btn.x+40, three_btn.y+10))
            window.blit(font.render("4 Spieler", True, (0,0,0)), (four_btn.x+40, four_btn.y+10))

            pygame.display.update()
        
    def get_player_name(self, window, font, number):
        """Die Funktion zeigt ein Eingabefeld an, in das der Spieler seinen Namen eintippen kann, 
        verarbeitet Tastatureingaben und gibt den eingegebenen Namen zurück, 
        sobald Enter gedrückt wird."""
        name = ""
        input_box = pygame.Rect((self.width // 2) - 200, self.height // 2, 450, 60)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and name != "":
                        return name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 12:
                            name += event.unicode

            self.draw_vertical_gradient((18, 22, 28), (23, 27, 33))

            h_font = self.head_font.render("Spielernamen eingeben:", True, (174, 239, 255))
            window.blit(h_font, (self.width * 0.15, self.height * 0.20))

            title = font.render(f"Name für Spieler {number} eingeben:", True, (255,255,255))
            window.blit(title, ((self.width // 2) - 200, (self.height // 2) - self.font_size * 2))

            pygame.draw.rect(window, "white", input_box, 2)
            name_surface = font.render(name, True, (255,255,255))
            window.blit(name_surface, (input_box.x + 10, input_box.y + 10))

            text = font.render("Mit Enter weiter...", True, (255,255,255))
            window.blit(text, ((self.width // 2) - 200, (self.height // 2) + self.font_size * 4))

            pygame.display.update()

    def won(self, win, font, player_list):
        """Die Funktion zeigt den Endbildschirm an, listet alle Spieler mit ihren finalen Punktzahlen auf, 
        ermittelt den Spieler mit der höchsten Punktzahl und blendet ihn als Gewinner ein."""
        max_score = 0
        max_name = ""
       
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                    pygame.quit()
                    exit()

            self.draw_vertical_gradient((18, 22, 28), (23, 27, 33))

            h_font = self.head_font.render("Ergebnis:", True, (174, 239, 255))
            self.window.blit(h_font, (self.width * 0.15,self.height * 0.10))

            y = 250
            for player in player_list:
                title = font.render(f"{player.name}: {player.final_score}", True, (255,255,255))
                win.blit(title, (450, y))
                y += 50

            for player in player_list:
                if player.final_score > max_score:
                    max_score = player.final_score
                    max_name = player.name

            won_text = font.render(f"{max_name} hat mit {max_score} gewonnen!", True, (255,255,255))
            win.blit(won_text, (450, y + 50))
        
            pygame.display.update()

    def draw_vertical_gradient(self, top_color, bottom_color):
            width, height = self.window.get_size()
            for y in range(height):
                ratio = y / height
                r = int(top_color[0] * (1 - ratio) + bottom_color[0] * ratio)
                g = int(top_color[1] * (1 - ratio) + bottom_color[1] * ratio)
                b = int(top_color[2] * (1 - ratio) + bottom_color[2] * ratio)
                pygame.draw.line(self.window, (r, g, b), (0, y), (width, y))