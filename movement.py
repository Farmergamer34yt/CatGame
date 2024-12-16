import pygame
from config import *

def handle_cat_movement(cat_x, cat_y, wall_x, wall_y, wall_size, cat_size, move_speed):
    """
    Handle cat movement with boundary and wall collision checks.
    
    Args:
        cat_x (int): Current x-coordinate of the cat
        cat_y (int): Current y-coordinate of the cat
        wall_x (int): x-coordinate of the wall
        wall_y (int): y-coordinate of the wall
        wall_size (int): Size of the wall
        cat_size (int): Size of the cat
        move_speed (int): Speed of cat movement
    
    Returns:
        tuple: Updated (cat_x, cat_y) after movement
    """
    keys = pygame.key.get_pressed()
    
    # Left movement
    if keys[pygame.K_LEFT]:
        if cat_x > 0 and not (cat_x - move_speed < wall_x + wall_size and 
                               cat_y < wall_y + wall_size and 
                               cat_y + cat_size > wall_y):
            cat_x -= move_speed
    
    # Right movement
    if keys[pygame.K_RIGHT]:
        if cat_x + cat_size < screen_width and not (cat_x + cat_size + move_speed > wall_x and 
                                                    cat_y < wall_y + wall_size and 
                                                    cat_y + cat_size > wall_y):
            cat_x += move_speed
    
    # Up movement
    if keys[pygame.K_UP]:
        if cat_y > 0 and not (cat_y - move_speed < wall_y + wall_size and 
                               cat_x < wall_x + wall_size and 
                               cat_x + cat_size > wall_x):
            cat_y -= move_speed
    
    # Down movement
    if keys[pygame.K_DOWN]:
        if cat_y + cat_size < screen_height and not (cat_y + cat_size + move_speed > wall_y and 
                                                     cat_x < wall_x + wall_size and 
                                                     cat_x + cat_size > wall_x):
            cat_y += move_speed
    
    return cat_x, cat_y