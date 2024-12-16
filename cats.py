import pygame
import sys
from config import *  # Import configuration
from menu import *  # Import menu functions
from movement import handle_cat_movement
from mouse_ai import move_mouse_away_from_cat
from levels import get_level_config, LEVELS

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cat Puzzle Game')

# Initialize font
font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)

# Game states
MENU = 0
GAME = 1
INSTRUCTIONS = 2
GAME_OVER = 3
LEVEL_SELECT = 4
current_state = MENU

# Global game variables
current_level = 1

# Game screen logic
def game_screen():
    global cat_x, cat_y, mouse_x, mouse_y, wall_x, wall_y, current_state, move_speed, mouse_speed, current_level
    
    # Get current level configuration
    level_config = get_level_config(current_level)
    
    # Update wall, cat, and mouse speeds based on level
    wall_x = level_config['wall_x']
    wall_y = level_config['wall_y']
    
    screen.fill(BRIGHT_BLUE)  # Clear the screen with a bright blue background
    
    # Update cat position based on movement
    cat_x, cat_y = handle_cat_movement(cat_x, cat_y, wall_x, wall_y, wall_size, cat_size, move_speed)
    
    # Move the mouse away from the cat
    mouse_x, mouse_y = move_mouse_away_from_cat(mouse_x, mouse_y, cat_x, cat_y, mouse_speed)
    
    # Draw the cat (red block)
    pygame.draw.rect(screen, CAT_COLOR, (cat_x, cat_y, cat_size, cat_size))
    
    # Draw the mouse (green block)
    pygame.draw.rect(screen, MOUSE_COLOR, (mouse_x, mouse_y, cat_size, cat_size))
    
    # Draw the wall (blue block)
    pygame.draw.rect(screen, WALL_COLOR, (wall_x, wall_y, wall_size, wall_size))
    
    # Display current level
    level_text = small_font.render(f"Level {current_level}", True, WHITE)
    screen.blit(level_text, (10, 10))
    
    # Check for mouse catch (simple collision detection)
    if cat_x < mouse_x + cat_size and cat_x + cat_size > mouse_x and cat_y < mouse_y + cat_size and cat_y + cat_size > mouse_y:
        current_state = GAME_OVER

    pygame.display.flip()

# Level select screen
def level_select_screen():
    global current_state, current_level
    
    screen.fill(BRIGHT_BLUE)
    
    # Title
    title_text = font.render("Select Level", True, WHITE)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))
    
    # Create level buttons
    for i, level in enumerate(LEVELS):
        # Calculate button position
        x = 50 + (i % 5) * 150
        y = 150 + (i // 5) * 100
        
        # Draw button
        pygame.draw.rect(screen, (200, 200, 200), (x, y, 100, 50))
        
        # Level number
        level_text = small_font.render(f"Level {level['level']}", True, BLACK)
        level_text_rect = level_text.get_rect(center=(x + 50, y + 25))
        screen.blit(level_text, level_text_rect)
    
    # Back button
    pygame.draw.rect(screen, (200, 200, 200), (300, 450, 200, 50))
    back_text = font.render("Back", True, BLACK)
    back_rect = back_text.get_rect(center=(400, 475))
    screen.blit(back_text, back_rect)
    
    pygame.display.flip()
    
    # Handle level selection
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                # Check level buttons
                for i, level in enumerate(LEVELS):
                    x = 50 + (i % 5) * 150
                    y = 150 + (i // 5) * 100
                    if x <= mouse_x <= x + 100 and y <= mouse_y <= y + 50:
                        current_level = level['level']
                        return True
                
                # Back button
                if 300 <= mouse_x <= 500 and 450 <= mouse_y <= 500:
                    return True
        
        pygame.display.update()

# Game over screen
def game_over_screen():
    global current_state, current_level
    
    screen.fill(BRIGHT_BLUE)
    
    # "Game Over" text
    game_over_text = font.render("Game Over!", True, WHITE)
    text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
    screen.blit(game_over_text, text_rect)
    
    # "Caught the Mouse" text
    caught_text = font.render("You caught the mouse!", True, WHITE)
    caught_rect = caught_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    screen.blit(caught_text, caught_rect)
    
    # Level result
    result_text = small_font.render(f"Completed Level {current_level}", True, WHITE)
    result_rect = result_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(result_text, result_rect)
    
    # Draw buttons
    # Next Level
    next_color = (0, 200, 0) if current_level < 10 else (100, 100, 100)
    pygame.draw.rect(screen, next_color, (200, 350, 150, 50))
    next_text = font.render("Next Level" if current_level < 10 else "Max Level", True, WHITE)
    next_rect = next_text.get_rect(center=(275, 375))
    screen.blit(next_text, next_rect)
    
    # Return to Menu
    pygame.draw.rect(screen, (200, 200, 200), (400, 350, 150, 50))
    menu_text = font.render("Menu", True, BLACK)
    menu_rect = menu_text.get_rect(center=(475, 375))
    screen.blit(menu_text, menu_rect)
    
    pygame.display.flip()
    
    # Wait for user input :3    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                # Next Level
                if 200 <= mouse_x <= 350 and 350 <= mouse_y <= 400:
                    if current_level < 10:
                        current_level += 1
                        return True
                
                # Return to Menu
                if 400 <= mouse_x <= 550 and 350 <= mouse_y <= 400:
                    return True
        
        pygame.display.update()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if current_state == MENU:
        show_main_menu()  # Show the main menu
        
        # Check for menu interactions
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Left mouse button
            if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 250:  # Start Game
                # Reset game variables for the first level
                current_level = 1
                current_state = GAME
            elif 300 <= mouse_x <= 500 and 250 <= mouse_y <= 300:  # Level Select
                current_state = LEVEL_SELECT
            elif 300 <= mouse_x <= 500 and 350 <= mouse_y <= 400:  # Instructions
                current_state = INSTRUCTIONS
            elif 300 <= mouse_x <= 500 and 450 <= mouse_y <= 500:  # Quit
                running = False
    
    elif current_state == LEVEL_SELECT:
        if not level_select_screen():
            running = False
        else:
            current_state = MENU
    
    elif current_state == INSTRUCTIONS:
        show_instructions()  # Show the instructions screen
        
        # Check for back button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Left mouse button
            if 300 <= mouse_x <= 500 and 450 <= mouse_y <= 500:  # Back button
                current_state = MENU
    
    elif current_state == GAME:
        game_screen()  # Game logic
    
    elif current_state == GAME_OVER:
        # Show game over screen and wait for user input
        if game_over_screen():
            current_state = GAME
        else:
            running = False
    
    pygame.display.update()

pygame.quit()
sys.exit()