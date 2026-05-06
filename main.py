import pygame
import cup
import dice
import game
import player
import scorecard

pygame.init()
window = pygame.display.set_mode((1300,800))
pygame.display.set_caption("Kniffel")
font = pygame.font.SysFont("comicsansms", 28, bold=True)
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (1300, 800))

button = pygame.Rect(20,730,130,50) 

running = True

players = []
dices = []

score_card = [
    scorecard.Scorecard("Einser", 0, 20),
    scorecard.Scorecard("Zweier", 0, 80),
    scorecard.Scorecard("Dreier", 0, 140),
    scorecard.Scorecard("Vierer", 0, 200),
    scorecard.Scorecard("Fünfer", 0, 260),
    scorecard.Scorecard("Sechser", 0, 320),
    scorecard.Scorecard("Dreierpasch", 0, 380),
    scorecard.Scorecard("Viererpasch", 0, 440),
    scorecard.Scorecard("Full House", 0, 500),
    scorecard.Scorecard("Kleine Straße", 0, 560),
    scorecard.Scorecard("Große Straße", 0, 620),
    scorecard.Scorecard("Kniffel", 0, 680),
    scorecard.Scorecard("Chance", 0, 740),
]



# scorecard = scorecard.Scorecard(score_card)

players.append(player.Player(scorecard, "Henry", False, "easy"))
players.append(player.Player(scorecard, "Henryson", False, "easy"))

dices.append(dice.Dice(1, False, 20, {"x": 10, "y": 10}, "white",  20, 20))
dices.append(dice.Dice(2, False, 20, {"x": 10, "y": 10}, "white", 120, 20))
dices.append(dice.Dice(3, False, 20, {"x": 10, "y": 10}, "white", 220, 20))
dices.append(dice.Dice(4, False, 20, {"x": 10, "y": 10}, "white", 320, 20))
dices.append(dice.Dice(5, False, 20, {"x": 10, "y": 10}, "white", 420, 20))

cup = cup.Cup(dices)
game = game.Game(players, cup, window)

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

    #Würfel zeichnen
    for i in range(len(dices)):
        dices[i].draw(window,font)

    for row in score_card:
        row.draw(window, font)

    #Button für würfeln
    pygame.draw.rect(window, "white", button)

    text = font.render("Würfeln", True, (0, 0, 0))
    text_rect = text.get_rect(center=button.center)
    window.blit(text, text_rect)
   
    pygame.display.update()

pygame.quit()   