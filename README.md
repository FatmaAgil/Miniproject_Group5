# miniproject

# Sphere Snake Game with Elegant Background

A 2D Snake game built using `pygame`, featuring a gradient background, a gradient snake, and gradient food. The goal is to collect food to grow the snake while avoiding collisions with the wall and the snake's own body. The game progressively gets harder as the snake's speed increases after each food item is eaten.

## Features

- **Gradient Background**: Smooth vertical gradient from Light Sky Blue to Midnight Blue.
- **Gradient Snake**: Snake represented by spheres with a radial gradient.
- **Food with Gradient**: Food appears as a circle with a gradient color, respawning after being eaten.
- **Score System**: Score increases as the snake eats food.
- **Increasing Difficulty**: Snake's velocity increases after eating food.
- **Game Over Screen**: Displays "Game Over" if the snake collides with the wall or itself.
- **Congratulations Screen**: Displayed upon reaching a score of 100.


## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org) library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<username>/sphere-snake-game.git
   cd sphere-snake-game
Install Python dependencies: Ensure you have Python 3.x installed and run:
bash
Copy code
pip install pygame

# How to Play
Run the Game: Execute the main.py file to start the game:

bash
Copy code
python main.py

# Controls:

Use the arrow keys (UP, DOWN, LEFT, RIGHT) to control the snake's direction.

# Objective:

Collect food to grow the snake.
Avoid colliding with the walls or the snake's own body.
The game ends when the snake collides with itself or the walls.

# Score Milestone:

If you reach a score of 100, you will see a congratulatory message.

# Game Over:

When the snake collides with the wall or itself, the game ends, and your final score is displayed.
