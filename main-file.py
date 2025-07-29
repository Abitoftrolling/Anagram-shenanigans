# main-file.py
import pygame
from projFiles.anagram_solver import find_anagrams
from projFiles.letter_system import load_words, get_letters
from projFiles.point_system import PointSystem
from projFiles.levels import LevelSystem
#from classes.glbsettings import *
#from classes.game import Game
#from classes.ui import draw_interface
#from classes.timer import Timer

pygame.init()
pygame.mixer.music.load("projFiles/Don't Tap The Glass.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Anagram Game")
font = pygame.font.SysFont(None, FONT_SIZE)
clock = pygame.time.Clock()

game = Game("planet")  # Hardcoded for now; you can pull from word-bank
timer = Timer()
words = load_words()
curr_letters, curr_word = get_letters(random.choice(words))
point_system = PointSystem()
level_system = LevelSystem

def draw_screen(): #edit later
    screen.fill((245, 240, 230))    #beigeish



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                #game.backspace()
                input_text = 

            elif event.key == pygame.K_RETURN:
                #game.reset_input()
                valid_anagrams = find_anagrams(curr_word, words)

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
