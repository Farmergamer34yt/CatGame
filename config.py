import pygame

# Initialize pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cat Puzzle Game')

# Initialize positions and other necessary variables
cat_x = 100  # Starting X position for the cat
cat_y = 100  # Starting Y position for the cat
cat_size = 50  # Size of the cat (as a square)
mouse_x = 300  # Starting X position for the mouse
mouse_y = 300  # Starting Y position for the mouse
mouse_speed = 0.1  # Speed at which the mouse moves away from the cat
move_speed = 0.2  # Speed at which the cat moves
screen_width = 800  # Width of the screen
screen_height = 600  # Height of the screen
cat_detection_range = 200 #Detection range of the cat
running_duration = 10 #How long it runs
breathing_duration = 5 #How long the mouse rests

# Define other necessary constants (like wall size, colors, etc.)
WALL_COLOR = (0, 0, 255)
CAT_COLOR = (255, 0, 0)
MOUSE_COLOR = (0, 255, 0)
BRIGHT_BLUE = (0, 191, 255)
WHITE = (255, 255, 255)
BUTTON_COLOR = (0, 255, 0)
HOVER_COLOR = (255, 0, 0)
BLACK = (0,0,0)

# Wall dimensions (example)
wall_x = 200
wall_y = 200
wall_size = 100

# Font for text
font = pygame.font.SysFont(None, 55)
