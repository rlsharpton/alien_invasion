#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

#import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen)

    bg_color = (230,230,230)
    #Start main loop for the game.
    while True:

        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

run_game()