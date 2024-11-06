markdown
# Sphere Snake Game

A modern 2D Snake game built using `pygame`, featuring a vibrant gradient background, a gradient snake, and gradient food. The objective is to collect food to grow the snake while avoiding collisions with the wall and the snake's own body. The game gets progressively harder as the snake's speed increases with each food item eaten.

## Features

- **Gradient Background**: Smooth vertical gradient from Light Sky Blue to Midnight Blue.
- **Gradient Snake**: Snake represented by spheres with a radial gradient effect.
- **Gradient Food**: Food appears as a circle with a gradient color, respawning after being eaten.
- **Score System**: The score increases as the snake eats food.
- **Increasing Difficulty**: Snake's velocity increases after eating food.
- **Game Over Screen**: Displays "Game Over" when the snake collides with the wall or itself.
- **Congratulations Screen**: Displayed upon reaching a score of 100.

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org) library

## Installation

Follow these steps to get the game running:

### 1. Clone the Repository

First, clone the repository to your local machine by running the following command in your terminal:

```bash
git clone https://github.com/<username>/sphere-snake-game.git
```

This command creates a local copy of the project on your computer.

### 2. Navigate into the Project Folder

Once cloned, change into the project directory with the following command:

```bash
cd sphere-snake-game
```

This will move you into the project folder, where all the game files are stored.

### 3. Install Python Dependencies

Ensure that you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

Next, install the required `pygame` library by running the following command:

```bash
pip install pygame
```

This will install the Pygame library, which is essential for rendering the graphics, handling game loops, and managing user inputs.

## How to Play

1. **Run the Game**: 

   Execute the `main.py` file to start the game:

   ```bash
   python main.py
   ```

2. **Controls**: 

   - Use the arrow keys:
     - **Up Arrow**: Move the snake up
     - **Down Arrow**: Move the snake down
     - **Left Arrow**: Move the snake left
     - **Right Arrow**: Move the snake right

3. **Objective**: 

   - Collect food to grow the snake.
   - Avoid colliding with the walls or the snake's own body.
   - The game ends when the snake collides with itself or the walls.

4. **Score Milestone**: 

   - Reach a score of 100 to see a congratulatory message!

5. **Game Over**: 

   - The game ends when the snake collides with the wall or itself, and your final score will be displayed.

## Future Enhancements

- **Obstacles**: Adding obstacles that the snake must avoid for extra difficulty.
- **Sound Effects**: Incorporating sounds for actions like eating food, movement, and game over scenarios.
- **High Score Tracking**: Keeping track of the highest score achieved during gameplay.

## About

- **Developers**: 
  - @Norah-G (Norah Kimathi)
  - @Radula254 (Joshua Radula)
  - @FatmaAgil (Fatma Agil)
  - @NjokiBless (Njoki Bless)

Enjoy the game, and feel free to contribute or improve upon it!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

