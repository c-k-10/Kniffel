# === IMPORTS ====
import pygame
import game
# === GAME ===           
def main(game):     
    game = game.Game()
    game.main_game()
    pygame.quit()   

if __name__ == "__main__":
    main(game)