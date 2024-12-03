import pygame
import sys
from sudoku_generator import Board

def main():
    pygame.init()
    screen = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    
    # Initialize the Sudoku board
    difficulty = "easy"  # Change to "medium" or "hard" for different difficulties
    board = Board(540, 540, screen, difficulty)

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
