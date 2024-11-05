import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sphere Snake Game with Elegant Background")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TOP_COLOR = (135, 206, 250)  # Light Sky Blue
BOTTOM_COLOR = (25, 25, 112)  # Midnight Blue

# Game variables
score = 0
running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


def create_vertical_gradient_surface(width, height, top_color, bottom_color):
    """Creates a surface with a vertical gradient."""
    gradient = pygame.Surface((width, height))
    for y in range(height):
        color = (
            int(top_color[0] + (bottom_color[0] - top_color[0]) * (y / height)),
            int(top_color[1] + (bottom_color[1] - top_color[1]) * (y / height)),
            int(top_color[2] + (bottom_color[2] - top_color[2]) * (y / height))
        )
        pygame.draw.line(gradient, color, (0, y), (width, y))
    return gradient


def create_gradient_circle_surface(radius, inner_color, outer_color):
    """Creates a surface with a circle that has a radial gradient."""
    circle_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    for i in range(radius, 0, -1):
        color = (
            int(outer_color[0] + (inner_color[0] - outer_color[0]) * (i / radius)),
            int(outer_color[1] + (inner_color[1] - outer_color[1]) * (i / radius)),
            int(outer_color[2] + (inner_color[2] - outer_color[2]) * (i / radius)),
            255
        )
        pygame.draw.circle(circle_surface, color, (radius, radius), i)
    return circle_surface


def draw_text(text, x, y, color=BLACK):
    """Displays the text on the screen."""
    score_text = font.render(text, True, color)
    screen.blit(score_text, (x, y))


def game_over():
    """Displays the Game Over screen."""
    screen.fill(BLACK)
    draw_text("Game Over!", WIDTH // 2 - 100, HEIGHT // 2 - 50, color=WHITE)
    draw_text(f"Your Score: {score}", WIDTH // 2 - 100, HEIGHT // 2, color=WHITE)
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    exit()


class Snake:
    def __init__(self, x, y, radius, velocity):
        self.radius = radius
        self.velocity = velocity
        self.direction = "RIGHT"
        self.body = [(x, y)]
        self.length = 1
        self.surface = create_gradient_circle_surface(self.radius, (0, 255, 0), (0, 100, 0))

    def update(self):
        # Update the position based on the direction
        x, y = self.body[0]
        if self.direction == "UP":
            y -= self.velocity
        elif self.direction == "DOWN":
            y += self.velocity
        elif self.direction == "LEFT":
            x -= self.velocity
        elif self.direction == "RIGHT":
            x += self.velocity
        new_head = (x, y)
        self.body.insert(0, new_head)
        if len(self.body) > self.length:
            self.body.pop()

    def draw(self, surface):
        for segment in self.body:
            pos = (int(segment[0] - self.radius), int(segment[1] - self.radius))
            surface.blit(self.surface, pos)

    def check_self_collision(self):
        if len(self.body) > 70:  # Adjusted threshold to start checking after the snake has grown a bit
            head = self.body[0]
            for segment in self.body[4:]:
                distance = ((head[0] - segment[0]) ** 2 + (head[1] - segment[1]) ** 2) ** 0.5
                if distance < self.radius:  # Adjusted threshold to avoid early collision
                    return True
        return False

    def check_wall_collision(self, width, height):
        x, y = self.body[0]
        if x - self.radius < 0 or x + self.radius > width or y - self.radius < 0 or y + self.radius > height:
            return True
        return False


class Food:
    def __init__(self, radius, color_inner, color_outer):
        self.radius = radius
        self.surface = create_gradient_circle_surface(self.radius, color_inner, color_outer)
        self.position = self.spawn()

    def spawn(self):
        x = random.randint(self.radius, WIDTH - self.radius)
        y = random.randint(self.radius, HEIGHT - self.radius)
        return (x, y)

    def draw(self, surface):
        x, y = self.position
        pos = (int(x - self.radius), int(y - self.radius))
        surface.blit(self.surface, pos)


# Initialize the background
background = create_vertical_gradient_surface(WIDTH, HEIGHT, TOP_COLOR, BOTTOM_COLOR)

# Initialize the snake and food
snake = Snake(WIDTH // 2, HEIGHT // 2, radius=20, velocity=3)
food = Food(radius=10, color_inner=(128, 0, 128), color_outer=(75, 0, 130))

# Main game loop
while running:
    screen.blit(background, (0, 0))  # Blit the gradient background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"

    # Update snake position
    snake.update()

    # Check for collisions with walls
    if snake.check_wall_collision(WIDTH, HEIGHT) or snake.check_self_collision():
        game_over()

    # Check for collisions with food
    head_x, head_y = snake.body[0]
    food_x, food_y = food.position
    distance_to_food = ((head_x - food_x) ** 2 + (head_y - food_y) ** 2) ** 0.5
    if distance_to_food < snake.radius + food.radius:
        score += 1
        snake.length += 1
        food.position = food.spawn()

        # Increase snake speed after eating food
        snake.velocity = min(snake.velocity + 0.1, 10)

    # Draw the snake
    snake.draw(screen)

    # Draw the food
    food.draw(screen)

    # Display the score
    draw_text(f"Score: {score}", 10, 10)

    # Check if score reaches 100
    if score >= 100:
        screen.fill(BLACK)
        draw_text("Congratulations! You reached 100!", WIDTH // 2 - 200, HEIGHT // 2 - 50, color=WHITE)
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    # Update the display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
