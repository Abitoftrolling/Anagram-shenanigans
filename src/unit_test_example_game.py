# Importing necessary Pygame module
import pygame
import sys

# Initialize Pygame
pygame.init()

# Setting up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Unit Testing Vocabulary Example')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Filling the screen with a color
    screen.fill((135, 206, 250))  # Light blue background
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
