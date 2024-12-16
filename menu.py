import pygame
from config import *  # Import configuration


# Assuming that screen is defined elsewhere (e.g., in a main game file or config file)
# You can import the screen variable or pass it to the functions as needed.

# You can import the necessary game variables (e.g., from config.py)
from config import screen, screen_width, screen_height, font, BUTTON_COLOR, HOVER_COLOR

def draw_button(text, x, y, width, height, color, hover_color):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if x <= mouse_x <= x + width and y <= mouse_y <= y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))
    
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x + width // 2 - text_surface.get_width() // 2, y + height // 2 - text_surface.get_height() // 2))

def show_main_menu():
    screen.fill((0, 191, 255))  # Fill screen with bright blue background
    draw_button("Start Game", 300, 200, 200, 50, BUTTON_COLOR, HOVER_COLOR)
    draw_button("Instructions", 300, 300, 200, 50, BUTTON_COLOR, HOVER_COLOR)
    draw_button("Quit", 300, 400, 200, 50, BUTTON_COLOR, HOVER_COLOR)
    pygame.display.flip()
def show_instructions():
    screen.fill((0, 0, 0))  # Fill the screen with a black background
    
    # Instructions text
    instructions_text = [
        "Instructions:",
        "1. Use arrow keys to move the cat.",
        "2. Avoid touching the wall.",
        "3. Try to catch the mouse!",
        "4. Press Back to return to the menu."
    ]
    
    y_offset = 100
    for line in instructions_text:
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (screen_width // 2 - text_surface.get_width() // 2, y_offset))
        y_offset += 50
    
    # Back button
    draw_button("Back", 300, 450, 200, 50, BUTTON_COLOR, HOVER_COLOR)
    
    pygame.display.flip()
