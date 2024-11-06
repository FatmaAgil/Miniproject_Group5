# miniproject

# Sphere Snake Game 

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

1. Clone the Repository:

Start by copying the code from GitHub to your local machine.
Use this command to clone the repository:
bash
Copy code
git clone https://github.com/<username>/sphere-snake-game.git
Explanation: This command creates a local copy of the project on your computer, making it easy to work with the files.

2. Navigate into the Project Folder:

Once cloned, change into the project directory with:
bash
Copy code
cd sphere-snake-game
Explanation: This step moves you into the main project folder where the code is organized.

3. Install Python Dependencies:

Ensure that you have Python 3.x installed on your computer. Python 3 is required because Pygame, the library used in this project, is compatible with Python 3.
Install the Pygame library, which is essential for running the game, by entering:
bash
Copy code
pip install pygame
Explanation: Pygame provides the tools to create graphics, handle game loops, and manage inputs for the game. Installing it will allow the code to run without errors.

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
