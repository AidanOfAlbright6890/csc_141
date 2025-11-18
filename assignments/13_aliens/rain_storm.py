import sys 

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from rain import Rain

class Rainstorm:
    """Overall class to manage game assets add behavior."""

    def __init__(self):
        """Initialize the game, and create game recources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rain Storm")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.rain = pygame.sprite.Group()
        
        self._create_storm()

        # Set the backround color.
        self.bg_color = (230, 230, 230)

    def _create_storm(self):
         """Create the storm of rain."""
         # Create an alien and keep adding aliens until there's no room left.
         # Spacing between aliens is one alien width and one alien height.
         rain = Rain(self)
         rain_width, rain_height = rain.rect.size

         current_x, current_y = rain_width, rain_height
         while current_y < (self.settings.screen_height - 3 * rain_height):
              while current_x < (self.settings.screen_width - 2 * rain_width):
                   self._create_rain(current_x, current_y)
                   current_x += 2 * rain_width
              # Finished a row; reset x value, and increment y value.
              current_x = rain_width
              current_y += 2 * rain_height
    def _create_rain(self, x_position, y_position):
         """Create an rain and place it in the fleet."""
         new_rain = Rain(self)
         new_rain.x = x_position
         new_rain.rect.x = x_position
         new_rain.rect.y = y_position
         self.rain.add(new_rain)
                    
                   

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_rain()
            self._update_screen()
            
            



            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                 if bullet.rect.bottom <= 0:
                      self.bullets.remove(bullet)
            print(len(self.bullets))
            self._update_screen()
            # Redraw the screen during each pass through the loop.
            # Watch for keyboard and mouse events.
    def _check_events(self):
            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)

    def _check_keydown_events(self, event):
         """Respond to keypresses."""
         if event.key == pygame.K_RIGHT:
              self.ship.moving_right = True
         elif event.key == pygame.K_LEFT:
              self.ship.moving_left = True
         elif event.key == pygame.K_q:
              sys.exit()
         elif event.key == pygame.K_SPACE:
              self._fire_bullet()

    def _check_keyup_events(self, event):
         """Respond to key releases"""
         if event.key == pygame.K_RIGHT:
              self.ship.moving_right = False
         elif event.key == pygame.K_LEFT:
              self.ship.moving_left = False

    def _fire_bullet(self):
         """Create a new bullet and add it to the bullets group."""
         new_bullet = Bullet(self)
         self.bullets.add(new_bullet)

    def _update_screen(self):
            """Update images on the screen, and flip to the new screen."""
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                 bullet.draw_bullet()
            self.ship.blitme()
            self.rain.draw(self.screen)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
    def _update_rain(self):
         """Check if the fleet is at an edge, then update positions."""
         self._check_storm_edges()
         self.rain.update()

    def _check_storm_edges(self):
         """Respond appropriately if any aliens have reahed an edge."""
         for rain in self.rain.sprites():
             if rain.check_edges():
                   self._change_storm_direction()
                   break
              
    def _change_storm_direction(self):
         """Drop the entire fleet and change the fleet's direction."""
         for rain in self.rain.sprites():
              rain.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rs = Rainstorm()
    rs.run_game()