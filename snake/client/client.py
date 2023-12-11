import pygame


class Entry:
    def __init__(self, interface: pygame):
        self.interface = interface

    def init_game(self):
        self.interface.init()
        screen = self.interface.display.set_mode((1280, 720))
        clock = self.interface.time.Clock()

        running = True
    
        while running:
            for event in self.interface.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            
            screen.fill("purple")
            self.interface.display.flip()
            clock.tick(60)
        
        self.interface.quit()
