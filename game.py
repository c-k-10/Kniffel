import pygame
import scorecard

class Game:
    def __init__(self, players:list, cup, window):
        self.players = players
        self.cup = cup
        self.window = window

    def game_won():
        pass

    def play_turn():
        pass

    def choose_player_count(self, window, font):
        one_btn   = pygame.Rect(500, 250, 300, 60)
        two_btn   = pygame.Rect(500, 330, 300, 60)
        three_btn = pygame.Rect(500, 410, 300, 60)
        four_btn  = pygame.Rect(500, 490, 300, 60)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if one_btn.collidepoint(event.pos): return 1
                    if two_btn.collidepoint(event.pos): return 2
                    if three_btn.collidepoint(event.pos): return 3
                    if four_btn.collidepoint(event.pos): return 4

            window.fill((20,20,20))

            title = font.render("Wie viele Spieler?", True, (255,255,255))
            window.blit(title, (500, 150))

            pygame.draw.rect(window, "white", one_btn)
            pygame.draw.rect(window, "white", two_btn)
            pygame.draw.rect(window, "white", three_btn)
            pygame.draw.rect(window, "white", four_btn)

            window.blit(font.render("1 Spieler", True, (0,0,0)), (one_btn.x+40, one_btn.y+10))
            window.blit(font.render("2 Spieler", True, (0,0,0)), (two_btn.x+40, two_btn.y+10))
            window.blit(font.render("3 Spieler", True, (0,0,0)), (three_btn.x+40, three_btn.y+10))
            window.blit(font.render("4 Spieler", True, (0,0,0)), (four_btn.x+40, four_btn.y+10))

            pygame.display.update()
        
    def get_player_name(self, window, font, number):
        name = ""
        input_box = pygame.Rect(450, 350, 400, 60)

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

            window.fill((20,20,20))

            title = font.render(f"Name für Spieler {number} eingeben:", True, (255,255,255))
            window.blit(title, (450, 250))

            pygame.draw.rect(window, "white", input_box, 2)
            name_surface = font.render(name, True, (255,255,255))
            window.blit(name_surface, (input_box.x + 10, input_box.y + 10))

            pygame.display.update()

        

    def create_scoreboard(self):
        return [
        scorecard.Scorecard("Einser", 0, 20, False,0,False),
        scorecard.Scorecard("Zweier", 0, 80, False,0,False),
        scorecard.Scorecard("Dreier", 0, 140, False,0,False),
        scorecard.Scorecard("Vierer", 0, 200, False,0,False),
        scorecard.Scorecard("Fünfer", 0, 260, False,0,False),
        scorecard.Scorecard("Sechser", 0, 320, False,0,False),
        scorecard.Scorecard("Dreierpasch", 0, 380, False,0,False),
        scorecard.Scorecard("Viererpasch", 0, 440, False,0,False),
        scorecard.Scorecard("Full House", 0, 500, False,0,False),
        scorecard.Scorecard("Kleine Straße", 0, 560, False,0,False),
        scorecard.Scorecard("Große Straße", 0, 620, False,0,False),
        scorecard.Scorecard("Kniffel", 0, 680, False,0,False),
        scorecard.Scorecard("Chance", 0, 740, False,0,False),
        ]