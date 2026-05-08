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

# === Button zum Würfeln erstellen ===
button = pygame.Rect(20,730,130,50) 

player_list = []
dices = []

current_player = 0
rolls_left = 3

dices.append(dice.Dice(1, False, 20, {"x": 10, "y": 10}, "white",  20, 20))
dices.append(dice.Dice(2, False, 20, {"x": 10, "y": 10}, "white", 120, 20))
dices.append(dice.Dice(3, False, 20, {"x": 10, "y": 10}, "white", 220, 20))
dices.append(dice.Dice(4, False, 20, {"x": 10, "y": 10}, "white", 320, 20))
dices.append(dice.Dice(5, False, 20, {"x": 10, "y": 10}, "white", 420, 20))

cup = cup.Cup(dices)
game = game.Game(player_list, cup, window)

player_number = game.choose_player_count(window, font)

for i in range(player_number):
    name = game.get_player_name(window, font, i+1)
    player_list.append(player.Player(game.create_scoreboard(), name, False, "easy"))

# === MAIN SCHLEIFE ===
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Bei Escape wird die Fester auf geschlossen
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                 for i in range(len(dices)):
                    dices[i].roll_dice()

        if event.type == pygame.MOUSEBUTTONDOWN:
             for dice in dices:
                if dice.rect.collidepoint(event.pos):
                    if dice.fixed == True:
                        dice.fixed = False
                    else:
                        dice.fixed = True
                        

    #Hintergrundfarbe
    window.blit(background, (0,0))

    player_text = font.render(f"Spieler: {player_list[current_player].name}", True, (255,255,255))
    window.blit(player_text, (20, 120))

    #Würfel zeichnen
    for i in range(len(dices)):
        dices[i].draw(window,font)

    for row in player_list[current_player].scorecard:
        counts, values, total = cup.counts()
        row.possible_score(counts, values, total)
        row.draw(window, font)

    #Button für würfeln
    pygame.draw.rect(window, "white", button)

    text = font.render("Würfeln", True, (0, 0, 0))
    text_rect = text.get_rect(center=button.center)
    window.blit(text, text_rect)
   
    pygame.display.update()

pygame.quit()   