import pygame
import random
import sys

from snake.models.snake import Snake

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720 
PIECE_MARGIN = 5
SNAKE_LENGTH = 6
SNAKE_HEIGHT = 10


velocity = [4, 0]


class Entry:
    def __init__(self, interface: pygame):
        self.interface = interface

    def init_game(self):
        self.interface.init()
        screen = self.interface.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = self.interface.time.Clock()

        running = True

        snake = Snake()

        # fruit position 
        fruit_position = [random.randrange(1, (SCREEN_WIDTH//10)) * 10,
                        random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
        fruit_spawn = True
        
        # setting default snake direction 
        # towards right
        direction = 'RIGHT'
        change_to = direction

        while True:
            # handling key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
        
            # If two keys pressed simultaneously 
            # we don't want snake to move into two directions
            # simultaneously
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
        
            # Moving the snake
            if direction == 'UP':
                snake.position[1] -= 10
            if direction == 'DOWN':
                snake.position[1] += 10
            if direction == 'LEFT':
                snake.position[0] -= 10
            if direction == 'RIGHT':
                snake.position[0] += 10
        
            # snake body growing mechanism 
            # if fruits and snakes collide then scores will be 
            # incremented by 10
            snake.insert()
            if snake.position[0] == fruit_position[0] and snake.position[1] == fruit_position[1]:
                # score += 10
                fruit_spawn = False
            else:
                snake.pop()
                
            if not fruit_spawn:
                fruit_position = [random.randrange(1, (SCREEN_WIDTH //10)) * 10, 
                                random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
                
            fruit_spawn = True
            screen.fill("black")
            
            snake.draw(screen)
                
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))
        
            # Game Over conditions
            if snake.position[0] < 0 or snake.position[0] > SCREEN_WIDTH-10:
                snake.position[0] *= -1
            if snake.position[1] < 0 or snake.position[1] > SCREEN_HEIGHT-10:
                snake.position[1] *= -1
            
            # # Touching the snake body
            for block in snake.body[1:]:
                if snake.position[0] == block[0] and snake.position[1] == block[1]:
                    pygame.quit()
                    sys.exit(0)
            
            # displaying score continuously
            # show_score(1, white, 'times new roman', 20)
            
            # Refresh game screen
            pygame.display.update()
        
            # Frame Per Second /Refresh Rate
            clock.tick(100)
       
