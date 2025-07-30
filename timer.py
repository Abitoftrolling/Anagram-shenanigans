# timer.py
import pygame
from glbsettings import TIMER_DURATION

class Timer:
    def __init__(self):
        self.start_ticks = pygame.time.get_ticks()

    def get_time_left(self):
        seconds_passed = (pygame.time.get_ticks() - self.start_ticks) // 1000
        return max(0, TIMER_DURATION - seconds_passed)

    def is_time_up(self):
        return self.get_time_left() == 0
    
    def add_time(self, seconds):
        self.start_ticks -= seconds * 1000
