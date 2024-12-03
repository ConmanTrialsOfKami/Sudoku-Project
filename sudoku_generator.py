import math
import random
import pygame
import sys

# SudokuGenerator Class
class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))
    
    def get_board(self):
        return self.board
    
    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) if cell != 0 else '.' for cell in row))
    
    def valid_in_row(self, row, num):
        return num not in self.board[row]
    
    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]
    
    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + self.box_length):
            for j in range(col_start, col_start + self.box_length):
                if self.board[i][j] == num:
                    return False
        return True
    
    def is_valid(self, row, col, num):
        return (
            self.valid_in_row(row, num) and
            self.valid_in_col(col, num) and
            self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num)
        )
    
    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.row_length + 1))
        random.shuffle(nums)
        for i in range(self.box_length):
            for j in range(self.box_length):
                self.board[row_start + i][col_start + j] = nums.pop()
    
    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)
    
    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == row // self.box_length * self.box_length:
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
    
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
    
    def remove_cells(self):
        removed = 0
        while removed < self.removed_cells:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                removed += 1

# Cell Class
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = None

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        font = pygame.font.Font(None, 50)
        x = self.col * 60
        y = self.row * 60

        rect = pygame.Rect(x, y, 60, 60)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), rect, 3)

        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 15))
        elif self.sketched_value:
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (x + 5, y + 5))

# Board Class
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
