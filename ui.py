#ui.py
import pygame

BEIGE = (245, 240, 230)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (50, 50, 255)
RED = (255, 180, 180)

def draw_interface(screen, font, letters, input, time_left, score, level, flash_invalid = False):
   screen.fill(BEIGE)
   screen_width, screen_height = screen.get_size()

   title_text = font.render("ANAGRAMS", True, BLACK)
   title_rect = title_text.get_rect(center=(screen_width // 2, 40))
   screen.blit(title_text, title_rect)

   box_size = 70
   spacing = 20
   total_width = len(letters) * (box_size + spacing) - spacing
   start_x = (screen_width - total_width) // 2
   y_pos = screen_height // 2 - box_size // 2

   for i, letter in enumerate(letters):
        x = start_x + i * (box_size + spacing)
        pygame.draw.rect(screen, GRAY, (x, y_pos, box_size, box_size), border_radius=5)
        letter_surf = font.render(letter.upper(), True, BLACK)
        letter_rect = letter_surf.get_rect(center=(x + box_size // 2, y_pos + box_size // 2))
        screen.blit(letter_surf, letter_rect)

   input_box_width = 600
   input_box_height = 70
   input_x = (screen_width - input_box_width) // 2
   input_y = screen_height - input_box_height - 30
   
   input_color = RED if flash_invalid else WHITE
   pygame.draw.rect(screen, input_color, (input_x, input_y, input_box_width, input_box_height), border_radius=5)

   input_text = font.render(input.upper(), True, BLACK)
   screen.blit(input_text, (input_x + 15, input_y + 20))

   info_font = pygame.font.SysFont("couriernew", 28)
   timer_color = RED if time_left <= 5 else BLACK
  
   timer_text = info_font.render(f"Time: {time_left}s", True, timer_color)
   score_text = info_font.render(f"Score: {score}", True, BLACK)
   level_text = info_font.render(f"Level: {level}", True, BLACK)
   
   screen.blit(timer_text, (screen_width - 180, 20))
   screen.blit(score_text, (screen_width - 180, 55))
   screen.blit(level_text, (screen_width - 180, 90))


def draw_start_screen(screen, font):
    screen.fill((245, 240, 230))
    title = font.render("ANAGRAMS", True, (0, 0, 0))
    title_rect = title.get_rect(center=(screen.get_width()//2, 150))
    screen.blit(title, title_rect)

    prompt = font.render("Press any key to start", True, (50, 50, 50))
    prompt_rect = prompt.get_rect(center=(screen.get_width()//2, 300))
    screen.blit(prompt, prompt_rect)

def draw_game_over_screen(screen, font, score):
    screen.fill((245, 240, 230))
    game_over = font.render("Game Over!", True, (180, 0, 0))
    game_over_rect = game_over.get_rect(center=(screen.get_width()//2, 150))
    screen.blit(game_over, game_over_rect)

    score_text = font.render(f"Your Score: {score}", True, (0, 0, 0))
    score_rect = score_text.get_rect(center=(screen.get_width()//2, 220))
    screen.blit(score_text, score_rect)

    restart = font.render("Press any key to restart", True, (50, 50, 50))
    restart_rect = restart.get_rect(center=(screen.get_width()//2, 300))
    screen.blit(restart, restart_rect)
        
    

   




