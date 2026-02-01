#Initial Pygame Window
#TODO: Remove the martian code. Was only used for exercise. 

import sys
import pygame

from settings import Settings
from ship import Ship#, Martian

class AlienInvasion: 
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """Initialize the game, and creat game resources."""
        pygame.init()
        
        # frame rate control. 
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # screen res.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        # window title
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)  
#        self.martian = Martian(self)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #helper methods
            self._check_events()
            self._update_screen()        

            # fps 60
            self.clock.tick(60) 

    def _check_events(self):
        """Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _update_screen(self):
        """Updae images on the screen, and flip to the new screen."""    
        # redraw the screen during each pass through the loop. 
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
#        self.martian.blitme()
                                        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
            
if __name__ == '__main__':
    # Make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()
