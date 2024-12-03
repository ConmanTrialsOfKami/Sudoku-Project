import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.sudoku = SudokuGenerator(9, self.difficulty_to_cells())
        self.sudoku.fill_values()
        self.board = self.sudoku.get_board()
        self.cells = [[Cell(self.board[row][col], row, col, screen) for col in range(9)] for row in range(9)]

    def difficulty_to_cells(self):
        return {"easy": 30, "medium": 40, "hard": 50}[self.difficulty]

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()
        self.draw_grid()

    def draw_grid(self):
        for i in range(10):
            line_width = 4 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 60), (540, i * 60), line_width)
            pygame.draw.line(self.screen, (0, 0, 0), (i * 60, 0), (i * 60, 540), line_width)
