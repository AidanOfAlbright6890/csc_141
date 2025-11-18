import pygame

from pygame.sprite import Sprite

class Rain(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, rs_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = rs_game.screen 
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('C:/Users/aidan/OneDrive/Documents/CSC 141/assignments/13_aliens/alien_Invasion 2.py/images/13_3_raindrops.py/images/Raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
       
    def update(self):
        """Move the alien right or left."""
        self.rect.x = self.x

        