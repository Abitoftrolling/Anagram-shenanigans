

import sys
import pygame
from pygame.locals import *
 
def update(dt):
  """
  Update game. Called once per frame.
  dt is the amount of time passed since last frame.
  If you want to have constant apparent movement no matter your framerate,
  what you can do is something like
  
  x += v * dt
  
  and this will scale your velocity based on time. Extend as necessary."""
  
  
  for event in pygame.event.get():
    
    if event.type == QUIT:
      pygame.quit() 
      sys.exit() #
      
def draw(screen):
  """
  Draw things to the window. Called once per frame.
  """
  screen.fill((0, 0, 0)) 
  

  pygame.display.flip()
 
def runPyGame():
  
  pygame.init()
  
 
  fps = 60.0
  fpsClock = pygame.time.Clock()
  
 
  width, height = 640, 480
  screen = pygame.display.set_mode((width, height))
  
 
  
  dt = 1/fps 
  while True: 
    update(dt) 
    draw(screen)
    
    dt = fpsClock.tick(fps)