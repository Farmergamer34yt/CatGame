import random
import enum
from config import *

class MouseState(enum.Enum):
    ROAMING = 1
    RUNNING = 2
    BREATHING = 3

class MouseStateMachine:
    def __init__(self, initial_x, initial_y, mouse_speed):
        """
        Initialize the mouse state machine.
        
        Args:
            initial_x (int): Starting x-coordinate of the mouse
            initial_y (int): Starting y-coordinate of the mouse
            mouse_speed (int): Base speed of mouse movement
        """
        self.x = initial_x
        self.y = initial_y
        self.base_speed = mouse_speed
        self.current_state = MouseState.ROAMING
        
        # Roaming state parameters
        self.roaming_change_direction_timer = 0
        self.roaming_direction_x = random.uniform(-1, 1)
        self.roaming_direction_y = random.uniform(-1, 1)
        
        # Running state parameters
        self.running_timer = 0
        self.running_duration = 50  # frames to run
        
        # Breathing state parameters
        self.breathing_timer = 0
        self.breathing_duration = 30  # frames to breathe
    
    def update(self, cat_x, cat_y):
        """
        Update mouse position and state based on cat proximity.
        
        Args:
            cat_x (int): x-coordinate of the cat
            cat_y (int): y-coordinate of the cat
        
        Returns:
            tuple: (new_mouse_x, new_mouse_y)
        """
        # Calculate distance to cat
        distance_to_cat = ((self.x - cat_x)**2 + (self.y - cat_y)**2)**0.5
        
        # State transitions
        if self.current_state == MouseState.ROAMING:
            # If cat is too close, start running
            if distance_to_cat < cat_detection_range:
                self.current_state = MouseState.RUNNING
                self.running_timer = 0
        
        elif self.current_state == MouseState.RUNNING:
            # After running for a while, start breathing
            self.running_timer += 1
            if self.running_timer >= self.running_duration:
                self.current_state = MouseState.BREATHING
                self.breathing_timer = 0
        
        elif self.current_state == MouseState.BREATHING:
            # After breathing, return to roaming
            self.breathing_timer += 1
            if self.breathing_timer >= self.breathing_duration:
                self.current_state = MouseState.ROAMING
                # Reset roaming direction
                self.roaming_direction_x = random.uniform(-1, 1)
                self.roaming_direction_y = random.uniform(-1, 1)
        
        # Movement logic based on current state
        if self.current_state == MouseState.ROAMING:
            # Roaming: Slow, random movement
            self.roaming_change_direction_timer += 1
            if self.roaming_change_direction_timer > 100:
                # Periodically change roaming direction
                self.roaming_direction_x = random.uniform(-1, 1)
                self.roaming_direction_y = random.uniform(-1, 1)
                self.roaming_change_direction_timer = 0
            
            speed = self.base_speed * 0.5
            self.x += self.roaming_direction_x * speed
            self.y += self.roaming_direction_y * speed
        
        elif self.current_state == MouseState.RUNNING:
            # Running: Fast movement away from cat
            speed = self.base_speed * 1.5
            dx = cat_x - self.x
            dy = cat_y - self.y
            
            # Normalize direction
            length = (dx**2 + dy**2)**0.5
            if length != 0:
                dx = -dx / length
                dy = -dy / length
            
            self.x += dx * speed
            self.y += dy * speed
            
            # Add some randomness
            self.x += random.uniform(-speed/4, speed/4)
            self.y += random.uniform(-speed/4, speed/4)
        
        elif self.current_state == MouseState.BREATHING:
            # Breathing: Slow movement, slightly random
            speed = self.base_speed * 0.25
            self.x += random.uniform(-speed, speed)
            self.y += random.uniform(-speed, speed)
        
        # Ensure mouse stays within screen bounds
        self.x = max(0, min(screen_width - cat_size, self.x))
        self.y = max(0, min(screen_height - cat_size, self.y))
        
        return self.x, self.y

def move_mouse_away_from_cat(mouse_x, mouse_y, cat_x, cat_y, mouse_speed):
    """
    Wrapper function to maintain compatibility with existing code.
    
    Args:
        mouse_x (int): Current x-coordinate of the mouse
        mouse_y (int): Current y-coordinate of the mouse
        cat_x (int): x-coordinate of the cat
        cat_y (int): y-coordinate of the cat
        mouse_speed (int): Speed of mouse movement
    
    Returns:
        tuple: Updated (mouse_x, mouse_y)
    """
    # Create a state machine if it doesn't exist
    if not hasattr(move_mouse_away_from_cat, 'state_machine'):
        move_mouse_away_from_cat.state_machine = MouseStateMachine(mouse_x, mouse_y, mouse_speed)
    
    # Update the state machine
    return move_mouse_away_from_cat.state_machine.update(cat_x, cat_y)