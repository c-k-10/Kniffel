import pygame
pygame.init()

# Fenster
WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dropdown Beispiel")

font = pygame.font.SysFont(None, 32)

# Dropdown-Daten
options = ["1 Spieler", "2 Spieler", "3 Spieler", "4 Spieler"]
selected_option = "Spieler auswählen"
dropdown_open = False

# Positionen
button_rect = pygame.Rect(50, 50, 200, 40)
option_height = 40


running = True
while running:
    window.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Hauptbutton geklickt → Dropdown öffnen/schließen
            if button_rect.collidepoint(mouse_pos):
                dropdown_open = not dropdown_open

            # Wenn Dropdown offen ist → Optionen prüfen
            if dropdown_open:
                for i, option in enumerate(options):
                    rect = pygame.Rect(button_rect.x, button_rect.y + (i+1)*option_height, button_rect.width, option_height)
                    if rect.collidepoint(mouse_pos):
                        selected_option = option
                        dropdown_open = False


    # Hauptbutton zeichnen
    pygame.draw.rect(window, (200, 200, 200), button_rect)
    text = font.render(selected_option, True, (0, 0, 0))
    window.blit(text, (button_rect.x + 10, button_rect.y + 8))

    # Dropdown-Optionen zeichnen
    if dropdown_open:
        for i, option in enumerate(options):
            rect = pygame.Rect(button_rect.x, button_rect.y + (i+1)*option_height, button_rect.width, option_height)

            # Hover-Effekt
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(window, (180, 180, 180), rect)
            else:
                pygame.draw.rect(window, (220, 220, 220), rect)

            text = font.render(option, True, (0, 0, 0))
            window.blit(text, (rect.x + 10, rect.y + 8))

    pygame.display.update()

pygame.quit()
