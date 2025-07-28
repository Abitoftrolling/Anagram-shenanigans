# main-file.py
import pygame
from classes.glbsettings import *
from classes.game import Game
from classes.ui import draw_interface
from classes.timer import Timer

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Anagram Game")
font = pygame.font.SysFont(None, FONT_SIZE)
clock = pygame.time.Clock()

game = Game("planet")  # Hardcoded for now; you can pull from word-bank
timer = Timer()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                game.backspace()
            elif event.key == pygame.K_RETURN:
                game.reset_input()
            elif event.unicode.isalpha():
                game.add_letter(event.unicode.lower())
        elif event.unicode.isalpha():
            success, invalid_letter = game.add_letter(event.unicode.lower())
            if invalid_letter:
                invalid_flash = True
            invalid_flash_timer = INVALID_FLASH_DURATION


    time_left = timer.get_time_left()
    draw_interface(screen, font, game.letter_pool, game.current_input, time_left)

    pygame.display.flip()
    clock.tick(90)


pygame.quit()
