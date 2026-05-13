import pygame

class Dropdown:
    def __init__(self, x, y, w, h, font, main_color, hover_color, options):
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.main_color = main_color
        self.hover_color = hover_color
        self.options = options  # [("Babyblau", (174,239,255)), ...]
        self.open = False
        self.selected = options[0]  # erstes Element

    def draw(self, win):
        # Hauptfeld
        pygame.draw.rect(win, self.main_color, self.rect)
        text = self.font.render(self.selected[0], True, (0,0,0))
        win.blit(text, (self.rect.x + 10, self.rect.y + 8))

        # Wenn offen → Optionen anzeigen
        if self.open:
            for i, option in enumerate(self.options):
                opt_rect = pygame.Rect(
                    self.rect.x,
                    self.rect.y + (i+1)*self.rect.height,
                    self.rect.width,
                    self.rect.height
                )

                # Hover
                color = self.hover_color if opt_rect.collidepoint(pygame.mouse.get_pos()) else self.main_color
                pygame.draw.rect(win, color, opt_rect)

                text = self.font.render(option[0], True, (0,0,0))
                win.blit(text, (opt_rect.x + 10, opt_rect.y + 8))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Klick auf Hauptfeld
            if self.rect.collidepoint(event.pos):
                self.open = not self.open
                return None

            # Klick auf Optionen
            if self.open:
                for i, option in enumerate(self.options):
                    opt_rect = pygame.Rect(
                        self.rect.x,
                        self.rect.y + (i+1)*self.rect.height,
                        self.rect.width,
                        self.rect.height
                    )

                    if opt_rect.collidepoint(event.pos):
                        self.selected = option
                        self.open = False
                        return option  # ("Babyblau", (174,239,255))

        return None
