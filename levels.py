# Levels configuration
LEVELS = [
    {
        "level": 1,
        "wall_x": 200,
        "wall_y": 200,
        "wall_size": 50,
        "difficulty_text": "Easy: Slow and Simple"
    },
    {
        "level": 2,
        "wall_x": 150,
        "wall_y": 250,
        "wall_size": 60,
        "difficulty_text": "Getting Tricky"
    },
    {
        "level": 3,
        "wall_x": 100,
        "wall_y": 150,
        "wall_size": 70,
        "difficulty_text": "Obstacles Increasing"
    },
    {
        "level": 4,
        "wall_x": 250,
        "wall_y": 100,
        "wall_size": 80,
        "difficulty_text": "More Challenging"
    },
    {
        "level": 5,
        "wall_x": 50,
        "wall_y": 250,
        "wall_size": 90,
        "difficulty_text": "Halfway Point"
    },
    {
        "level": 6,
        "wall_x": 300,
        "wall_y": 200,
        "wall_size": 100,
        "difficulty_text": "Getting Tough"
    },
    {
        "level": 7,
        "wall_x": 150,
        "wall_y": 50,
        "wall_size": 110,
        "difficulty_text": "Advanced Challenge"
    },
    {
        "level": 8,
        "wall_x": 250,
        "wall_y": 300,
        "wall_size": 120,
        "difficulty_text": "Expert Level"
    },
    {
        "level": 9,
        "wall_x": 50,
        "wall_y": 150,
        "wall_size": 130,
        "difficulty_text": "Master Challenge"
    },
    {
        "level": 10,
        "wall_x": 350,
        "wall_y": 100,
        "wall_size": 140,
        "difficulty_text": "Ultimate Test"
    }
]

def get_level_config(level_number):
    """
    Retrieve the configuration for a specific level.
    
    Args:
        level_number (int): The level number (1-10)
    
    Returns:
        dict: Configuration for the specified level
    """
    # Ensure level number is within range
    level_index = max(0, min(level_number - 1, len(LEVELS) - 1))
    return LEVELS[level_index]