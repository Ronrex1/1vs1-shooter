import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Colorful Shooter")

# Colors
PLAYER_COLOR = (0, 0, 255)           # Blue and Red for Player
ENEMY_LOW_POINTS_COLOR = (180, 180, 180)  # Light gray for less points
ENEMY_HIGH_POINTS_COLOR = (50, 50, 50)    # Dark gray for high points

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        speed = 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed
        if keys[pygame.K_UP]:
            self.rect.y -= speed
        if keys[pygame.K_DOWN]:
            self.rect.y += speed

        # Wrap around the screen
        if self.rect.right < 0:
            self.rect.left = screen_width
        elif self.rect.left > screen_width:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = screen_height
        elif self.rect.top > screen_height:
            self.rect.bottom = 0

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))

        # Determine point value and set color accordingly
        self.point_value = random.choice([10, 30])
        if self.point_value == 10:
            self.image.fill(ENEMY_LOW_POINTS_COLOR)
        else:
            self.image.fill(ENEMY_HIGH_POINTS_COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-30, -10)

    def update(self):
        speed = 3
        self.rect.y += speed

        # Wrap around the screen
        if self.rect.right < 0:
            self.rect.left = screen_width
        elif self.rect.left > screen_width:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = screen_height
        elif self.rect.top > screen_height:
            self.rect.bottom = 0

# Create player and enemy groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

enemies = pygame.sprite.Group()
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill((0, 0, 0))  # Background color (black)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
