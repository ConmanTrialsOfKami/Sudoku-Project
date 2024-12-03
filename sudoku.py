import pygame
import sys
from board import Board

def main():
    pygame.init()
    screen = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    
    board = Board(540, 540, screen, "easy")

    running = True
    while running:
        screen.fill((255, 255, 255))
        board.draw()
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
