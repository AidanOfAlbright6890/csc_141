import pygame
from pygame.sprite import Sprite

class Stars(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, si_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = si_game.screen 
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('C:/Users/aidan/OneDrive/Documents/CSC 141/assignments/13_aliens/alien_Invasion 2.py/images/13_01_stars.py/images/stars.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)