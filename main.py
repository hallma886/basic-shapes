# Draw 

# Pygame game template

import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def draw_rectangle(screen, rect, color, thickness):
    pygame.draw.rect(screen, color, rect, thickness)

def draw_circle(screen, center, radius, color, thickness):
    pygame.draw.circle(screen, color, center, radius, thickness)

def draw_line(screen, color, start_pos, end_pos, thickness):
    pygame.draw.line(screen, color, start_pos, end_pos, thickness)

def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    

 
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.WHITE) 

        draw_line(screen, config.BLACK, [100, 300], [400, 400], 5)

        draw_line(screen, config.GREEN, [350, 150], [300, 500], 8)

        draw_rectangle(screen, [100, 100, 200, 150], config.BLUE, 0)

        draw_rectangle(screen, [200, 200, 200, 150], config.ORANGE, 0)

        draw_rectangle(screen, [300, 300, 200, 150], config.PURPLE, 0)

        draw_rectangle(screen, [400, 400, 200, 150], config.RED, 0)

        draw_circle(screen, [537, 200], 75, config.FOREST_GREEN, 0)

        draw_circle(screen, [394, 200], 75, config.BROWN, 0)

        draw_circle(screen, [455, 200], 75, config.YELLOW, 0)

        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































