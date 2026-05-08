# === IMPORTS ====
import pygame
import cup
import dice
import game
import player
import scorecard

# === Fenster erstellen ===
pygame.init()
window = pygame.display.set_mode((1300,800))
pygame.display.set_caption("Kniffel")
font = pygame.font.SysFont("comicsansms", 28, bold=True)
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (1300, 800))
running = True

# === Button zum Würfeln ===
button = pygame.Rect(20,730,130,50)

# ---------------------------------------------------------
#   FUNKTION: Spieleranzahl auswählen
# ---------------------------------------------------------
def choose_player_count(window, font):
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

# ---------------------------------------------------------
#   FUNKTION: Namen eingeben
# ---------------------------------------------------------
def get_player_name(window, font, number):
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

# ---------------------------------------------------------
#   SCOREBOARD ERSTELLEN
# ---------------------------------------------------------
def create_scoreboard():
    return [
        scorecard.Scorecard("Einser", 0, 20, False, 0, False),
        scorecard.Scorecard("Zweier", 0, 80, False, 0, False),
        scorecard.Scorecard("Dreier", 0, 140, False, 0, False),
        scorecard.Scorecard("Vierer", 0, 200, False, 0, False),
        scorecard.Scorecard("Fünfer", 0, 260, False, 0, False),
        scorecard.Scorecard("Sechser", 0, 320, False, 0, False),
        scorecard.Scorecard("Dreierpasch", 0, 380, False, 0, False),
        scorecard.Scorecard("Viererpasch", 0, 440, False, 0, False),
        scorecard.Scorecard("Full House", 0, 500, False, 0, False),
        scorecard.Scorecard("Kleine Straße", 0, 560, False, 0, False),
        scorecard.Scorecard("Große Straße", 0, 620, False, 0, False),
        scorecard.Scorecard("Kniffel", 0, 680, False, 0, False),
        scorecard.Scorecard("Chance", 0, 740, False, 0, False),
    ]

# ---------------------------------------------------------
#   STARTMENÜ AUSFÜHREN
# ---------------------------------------------------------
player_count = choose_player_count(window, font)

players_list = []
for i in range(player_count):
    name = get_player_name(window, font, i+1)
    players_list.append(player.Player(create_scoreboard(), name, False, "easy", False))

# ---------------------------------------------------------
#   WÜRFEL ERSTELLEN
# ---------------------------------------------------------
dices = [
    dice.Dice(1, False, 20, {"x": 10, "y": 10}, "white",  20, 20),
    dice.Dice(2, False, 20, {"x": 10, "y": 10}, "white", 120, 20),
    dice.Dice(3, False, 20, {"x": 10, "y": 10}, "white", 220, 20),
    dice.Dice(4, False, 20, {"x": 10, "y": 10}, "white", 320, 20),
    dice.Dice(5, False, 20, {"x": 10, "y": 10}, "white", 420, 20),
]

cup = cup.Cup(dices)
game = game.Game(players_list, cup, window)

# ⭐ Spieler, der dran ist
current_player = 0

# ⭐ Würfe pro Runde
rolls_left = 3

# ---------------------------------------------------------
#   MAIN-SCHLEIFE
# ---------------------------------------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        # Würfeln
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                if rolls_left > 0:
                    for d in dices:
                        d.roll_dice()
                    rolls_left -= 1
                else:
                    print("Keine Würfe mehr übrig!")

        # Würfel fixieren
        if event.type == pygame.MOUSEBUTTONDOWN:
            for d in dices:
                if d.rect.collidepoint(event.pos):
                    d.fixed = not d.fixed

        # ⭐ Scoreboard anklicken
        if event.type == pygame.MOUSEBUTTONDOWN:
            for row in players_list[current_player].scorecard:
                if row.rect.collidepoint(event.pos):
                    if row.possible and not row.locked:

                        # Wert setzen
                        row.score = row.possible_value
                        row.locked = True

                        # ⭐ Prüfen ob Spieler fertig ist
                        if all(r.locked for r in players_list[current_player].scorecard):
                            total = sum(r.score for r in players_list[current_player].scorecard)
                            print(f"{players_list[current_player].name} ist fertig! Gesamtpunkte: {total}")

                        # Spielerwechsel
                        current_player = (current_player + 1) % len(players_list)

                        # Würfe zurücksetzen
                        rolls_left = 3

                        # Würfel freigeben
                        for d in dices:
                            d.fixed = False

                        break

    window.blit(background, (0,0))

    # ⭐ Spielername anzeigen
    player_text = font.render(f"Spieler: {players_list[current_player].name}", True, (255,255,255))
    window.blit(player_text, (20, 120))

    # ⭐ Würfe anzeigen
    roll_text = font.render(f"Würfe übrig: {rolls_left}", True, (255,255,0))
    window.blit(roll_text, (20, 160))

    # Würfel zeichnen
    for d in dices:
        d.draw(window,font)

    # Scoreboard zeichnen + mögliche Punkte berechnen
    counts, values, total = cup.counts()
    for row in players_list[current_player].scorecard:
        row.possible_score(counts, values, total)
        row.draw(window, font)

    # Würfeln-Button
    pygame.draw.rect(window, "white", button)
    text = font.render("Würfeln", True, (0, 0, 0))
    text_rect = text.get_rect(center=button.center)
    window.blit(text, text_rect)

    pygame.display.update()

pygame.quit()
