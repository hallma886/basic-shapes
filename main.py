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

def draw_polygon(screen, color, points, thickness=0):
    pygame.draw.polygon(screen, color, points, thickness)

def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    
    points5 = [(20, 10), (31, 25), (16, 20), (30, 60), (55, 65)]

    points4 = [(900, 10), (900, 20), (800, 40), (700, 60), (760, 70)]

    points3 = [(25, 550), (70, 500), (25, 400), (89, 500), (25, 600)]
 
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

        draw_polygon(screen, config.RED, points5, 0)

        draw_polygon(screen, config.BLUE, points4, 0)

        draw_polygon(screen, config.BLACK, points3, 5)

        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































