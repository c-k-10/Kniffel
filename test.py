import pygame
import sys

pygame.init()

# --- Fullscreen starten ---
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = window.get_size()

# --- Basisauflösung für Skalierung ---
BASE_WIDTH = 1920
BASE_HEIGHT = 1080

scale_x = width / BASE_WIDTH
scale_y = height / BASE_HEIGHT
scale = min(scale_x, scale_y)

# --- Farben ---
WHITE = (255, 255, 255)
BLUE = (100, 180, 255)
GREEN = (50, 150, 50)

# --- Dynamische Schrift ---
font_size = int(50 * scale)
font = pygame.font.Font(None, font_size)

# --- Beispiel-Text ---
text = font.render("Hallo Chrissi! Dynamische Skalierung aktiv!", True, WHITE)
text_rect = text.get_rect(center=(width // 2, int(100 * scale_y)))

# --- Kreis (z.B. für Würfelbereich) ---
circle_radius = int(250 * scale)
circle_center = (width // 2, height // 2)

# --- Beispiel-Würfel (einfaches Quadrat) ---
dice_size = int(120 * scale)
dice_x = int(800 * scale_x)
dice_y = int(500 * scale_y)
dice_rect = pygame.Rect(dice_x, dice_y, dice_size, dice_size)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    window.fill((30, 30, 30))

    # Kreis zeichnen
    pygame.draw.circle(window, GREEN, circle_center, circle_radius)

    # Würfel zeichnen
    pygame.draw.rect(window, BLUE, dice_rect, border_radius=10)

    # Text zeichnen
    window.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)
