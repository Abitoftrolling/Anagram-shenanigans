# main-file.py
import pygame
from projFiles.letter_system import load_words, get_letters, get_valid_anagrams
from ui import draw_interface
from projFiles.point_system import PointSystem
from projFiles.levels import LevelSystem
from timer import Timer
from glbsettings import INVALID_FLASH_DURATION, FONT_SIZE

pygame.init()
pygame.mixer.music.load("projFiles/Don't Tap The Glass.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Anagram Game")
font = pygame.font.SysFont(None, FONT_SIZE)
clock = pygame.time.Clock()

words = load_words()
curr_word, valid_anagrams = get_valid_anagrams(words, min_anagrams=10)
curr_letters, _ = get_letters(curr_word)

timer = Timer()
point_system = PointSystem()
level_system = LevelSystem()

current_input = ""
invalid_flash = False
invalid_flash_timer = 0

game_state = "start"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                current_input = current_input[:-1]

            elif event.key == pygame.K_RETURN:
                if current_input in valid_anagrams:
                    points, added = point_system.add_word(current_input)
                    if added:
                        current_input = ""
                        if level_system.should_level_up(point_system.get_score()):
                            level_system.level_up()
                            timer.start_ticks = pygame.time.get_ticks()
                            #reset new level
                            point_system = PointSystem()
                            curr_word, valid_anagrams = get_valid_anagrams(words, min_anagrams=10)
                            curr_letters, _ = get_letters(curr_word)

                else:
                    invalid_flash = True
                    invalid_flash_timer = INVALID_FLASH_DURATION
                    current_input = ""

            elif event.unicode.isalpha():
                if current_input.count(event.unicode.lower()) < curr_letters.count(event.unicode.lower()):
                    current_input += event.unicode.lower()
                else:
                    invalid_flash = True
                    invalid_flash_timer = INVALID_FLASH_DURATION

    if invalid_flash:
        invalid_flash_timer -= 1
        if invalid_flash_timer <= 0:
            invalid_flash = False

    time_left = timer.get_time_left()
    
    draw_interface(screen, font, curr_letters, current_input, time_left, point_system.get_score(), level_system.get_level(), flash_invalid=invalid_flash)

    pygame.display.flip()
    clock.tick(90)


pygame.quit()