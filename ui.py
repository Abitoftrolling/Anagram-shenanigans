#ui.py
import pygame

BEIGE = (245, 240, 230)
DARK_BROWN = (60, 45, 35)
SOFT_GRAY = (210, 200, 190)
CREAM = (255, 250, 240)
RED = (255, 180, 180)
WHITE = (255, 255, 255)


def load_fonts():
   title_font = pygame.font.Font("Bungee-Regular.ttf", 64)
   main_font = pygame.font.Font("Bungee-Regular.ttf", 48)
   info_font = pygame.font.Font("Bungee-Regular.ttf", 36)
   return title_font, main_font, info_font


def draw_interface(screen, title_font, main_font, info_font, letters, input, time_left, score, level_system, flash_invalid = False, curr_word=None):
   screen.fill(BEIGE)
   screen_width, screen_height = screen.get_size()


   title_font = pygame.font.Font("Bungee-Regular.ttf", 64)
   title_text = title_font.render("ANAGRAMAS", True, DARK_BROWN)
   title_rect = title_text.get_rect(center=(screen_width // 2, 40))
   screen.blit(title_text, title_rect)

   if curr_word:
        small_font = pygame.font.Font("Bungee-Regular.ttf", 16)
        label_surf = small_font.render("Current Word:", True, DARK_BROWN)
        word_surf = small_font.render(curr_word.upper(), True, DARK_BROWN)

        label_pos = (20, 20)
        word_pos = (20, 42)

        screen.blit(label_surf, label_pos)
        screen.blit(word_surf, word_pos)


   box_size = 70
   spacing = 20
   total_width = len(letters) * (box_size + spacing) - spacing
   start_x = (screen_width - total_width) // 2
   y_pos = screen_height // 2 - box_size // 2


   for i, letter in enumerate(letters):
        x = start_x + i * (box_size + spacing)
        pygame.draw.rect(screen, SOFT_GRAY, (x, y_pos, box_size, box_size), border_radius=5)
        pygame.draw.rect(screen, DARK_BROWN, (x, y_pos, box_size, box_size), border_radius=5)
        letter_surf = main_font.render(letter.upper(), True, WHITE)
        letter_rect = letter_surf.get_rect(center=(x + box_size // 2, y_pos + box_size // 2))
        screen.blit(letter_surf, letter_rect)


   input_box_width = 600
   input_box_height = 70
   input_x = (screen_width - input_box_width) // 2
   input_y = screen_height - input_box_height - 30
 
   input_color = RED if flash_invalid else CREAM
   pygame.draw.rect(screen, input_color, (input_x, input_y, input_box_width, input_box_height), border_radius=5)
   pygame.draw.rect(screen, DARK_BROWN, (input_x, input_y, input_box_width, input_box_height), 2, border_radius=5)
   input_text = main_font.render(input.upper(), True, DARK_BROWN)
   input_rect = pygame.Rect(input_x, input_y, input_box_width, input_box_height)
   input_text_rect = input_text.get_rect(center=input_rect.center)
   screen.blit(input_text, input_text_rect)



   info_font = pygame.font.Font("Bungee-Regular.ttf", 16)
   timer_color = RED if time_left <= 5 else DARK_BROWN
   timer_text = info_font.render(f"Time: {time_left}s", True, timer_color)
   score_text = info_font.render(f"Score: {score}", True, DARK_BROWN)
   level_text = info_font.render(f"Level: {level_system.get_level()}", True, DARK_BROWN)
   score_target_text = info_font.render(f"Target: {level_system.get_score_target()}", True, DARK_BROWN)
   
   screen.blit(timer_text, timer_text.get_rect(topright=(screen_width - 20, 20)))
   screen.blit(score_text, score_text.get_rect(topright=(screen_width - 20, 50)))
   screen.blit(level_text, level_text.get_rect(topright=(screen_width - 20, 80)))
   screen.blit(score_target_text, score_target_text.get_rect(topright=(screen_width - 20, 110)))


def draw_start_screen(screen):
    screen.fill(BEIGE)
    title_font = pygame.font.Font("Bungee-Regular.ttf", 64)
    main_font = pygame.font.Font("Bungee-Regular.ttf", 36)


    title = title_font.render("ANAGRAMAS", True, DARK_BROWN)
    title_rect = title.get_rect(center=(screen.get_width()//2, 150))
    screen.blit(title, title_rect)


    prompt = main_font.render("Press any key to start", True, DARK_BROWN)
    prompt_rect = prompt.get_rect(center=(screen.get_width()//2, 300))
    screen.blit(prompt, prompt_rect)


def draw_game_over_screen(screen,score,level):
    screen.fill(BEIGE)
    title_font = pygame.font.Font("Bungee-Regular.ttf", 64)
    main_font = pygame.font.Font("Bungee-Regular.ttf", 36)


    game_over = title_font.render("Game Over!", True, RED)
    game_over_rect = game_over.get_rect(center=(screen.get_width()//2, 150))
    screen.blit(game_over, game_over_rect)


    score_text = main_font.render(f"Your Score: {score}", True, DARK_BROWN)
    score_rect = score_text.get_rect(center=(screen.get_width()//2, 220))
    screen.blit(score_text, score_rect)

    level_text = main_font.render(f"Level Reached: {level}", True, DARK_BROWN)
    level_text_rect = level_text.get_rect(center=(screen.get_width()//2, 255))
    screen.blit(level_text, level_text_rect)

    restart = main_font.render("Press any key to restart", True, DARK_BROWN)
    restart_rect = restart.get_rect(center=(screen.get_width()//2, 300))
    screen.blit(restart, restart_rect)
      
