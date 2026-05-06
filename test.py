import pygame
pygame.init()

# Fenster
screen = pygame.display.set_mode((900, 750))
pygame.display.set_caption("Kniffel – Darstellung")

font = pygame.font.SysFont(None, 32)

# --- ScoreRow Klasse (nur Darstellung) ---
class ScoreRow:
    def __init__(self, name, value, y):
        self.name = name
        self.value = value
        self.rect = pygame.Rect(550, y, 300, 40)

    def draw(self, surface):
        pygame.draw.rect(surface, (40, 40, 40), self.rect)
        name_text = font.render(self.name, True, (255, 255, 255))
        val_text = font.render(str(self.value), True, (255, 255, 255))
        surface.blit(name_text, (self.rect.x + 10, self.rect.y + 8))
        surface.blit(val_text, (self.rect.right - 40, self.rect.y + 8))

# Spielzettel (nur Anzeige)
score_rows = [
    ScoreRow("Einser", 0, 50),
    ScoreRow("Zweier", 0, 100),
    ScoreRow("Dreier", 0, 150),
    ScoreRow("Vierer", 0, 200),
    ScoreRow("Fünfer", 0, 250),
    ScoreRow("Sechser", 0, 300),
    ScoreRow("Dreierpasch", 0, 380),
    ScoreRow("Viererpasch", 0, 430),
    ScoreRow("Full House", 0, 480),
    ScoreRow("Kleine Straße", 0, 530),
    ScoreRow("Große Straße", 0, 580),
    ScoreRow("Kniffel", 0, 630),
    ScoreRow("Chance", 0, 680),
]

# Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((25, 25, 25))

    # Spielzettel zeichnen
    for row in score_rows:
        row.draw(screen)

    pygame.display.update()

pygame.quit()
