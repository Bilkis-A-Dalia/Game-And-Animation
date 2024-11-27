# Jump between platforms.
# Avoid obstacles.
# Collect items.

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window and other game variables
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple 2D Platformer")

# Player settings
player = pygame.Rect(100, 380, 50, 50) # Start on the platform (y = 380)
gravity = 0.7 # Gravity acceleration
jump_strength = -15 # Jumping force
player_velocity = [0, 0] # [x_velocity, y_velocity]
on_ground = True # Start on the ground

# Camera settings
camera_x = 0 # Camera's x position

# Initial platform settings
platforms = []
items = [] # List to hold items
platform_width = 200
platform_height = 20
num_initial_platforms = 5

# Generate initial platforms and items
for i in range(num_initial_platforms):
    platform_x = i * (platform_width + 100) # Space out platforms
    platform_y = 400
    platform = pygame.Rect(platform_x, platform_y, platform_width, platform_height)
    platforms.append(platform)

    # Randomly decide to place an item on the platform
    if random.choice([True, False]): # 50% chance to place an item
        item = pygame.Rect(platform.x + (platform_width / 2) - 10, platform.y - 20, 20, 20) # Center theitem on the platform
        items.append(item)

# Font for displaying score
font = pygame.font.Font(None, 36)
score = 0

# Function to apply gravity
def apply_gravity():
    global on_ground
    if not on_ground: # Apply gravity only if the player is in the air
        player_velocity[1] += gravity # Apply gravity to vertical velocity
        player.y += player_velocity[1] # Move player vertically

    # Check for ground collision
    if player.y > screen_height - player.height: # Player falls below screen
        player.y = screen_height - player.height
        player_velocity[1] = 0 # Reset velocity on the ground
        on_ground = True # Player is on the ground

# Function to make the player jump
def jump():
    global on_ground
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and on_ground: # Jump only if on ground
        player_velocity[1] = jump_strength
        on_ground = False # Player is no longer on the ground
        print("Jump triggered!") # Debugging statement

# Function to handle horizontal movement
def move_player():
    global camera_x
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: # Move left
        player.x -= 5 # Move left by 5 pixels
        camera_x -= 5 # Move camera left
    if keys[pygame.K_RIGHT]: # Move right
        player.x += 5 # Move right by 5 pixels
        camera_x += 5 # Move camera right

# Function to check for collisions with platforms
def check_collision():
    global on_ground
    on_ground = False # Assume the player is not on a platform
    for platform in platforms:
        if player.colliderect(platform):
            if player_velocity[1] > 0: # Only apply when falling
                player.bottom = platform.top # Place player on top of platform
                player_velocity[1] = 0 # Reset vertical velocity
                on_ground = True # Player is on the ground
                break # Exit after handling one collision

# Function to collect items
def collect_items():
    global score
    for item in items[:]:
        if player.colliderect(item):
            items.remove(item)
            score += 1

# Function to generate new platforms and items
def generate_platforms_and_items():
    global camera_x
    # Generate new platforms as the player moves right
    while platforms and platforms[-1].x < camera_x + screen_width:
        # Randomly determine y position for the new platform
        new_platform_y = random.randint(300, 500)
        new_platform = pygame.Rect(platforms[-1].x + platform_width + 100, new_platform_y,platform_width, platform_height)
        platforms.append(new_platform)
        # Randomly decide to place an item on the new platform
        if random.choice([True, False]): # 50% chance to place an item
            item = pygame.Rect(new_platform.x + (platform_width / 2) - 10, new_platform.y - 20, 20, 20) #Center the item on the platform
            items.append(item)
    # Remove platforms that are off the left side of the screen
    platforms[:] = [p for p in platforms if p.x + platform_width > camera_x]

    items[:] = [i for i in items if i.x + 20 > camera_x] # Remove items that are off-screen

# Function to display the score
def display_score():
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply gravity, handle jumping, and check for collisions
    apply_gravity()
    move_player() # Handle horizontal movement
    jump() # Handle jumping
    check_collision() # Check for collisions
    collect_items() # Collect items
    # Generate new platforms and items
    generate_platforms_and_items()
    # Clear the screen
    screen.fill((0, 0, 0))
    # Draw the player, platforms, and items
    pygame.draw.rect(screen, (255, 0, 0), player.move(-camera_x, 0)) # Adjust player position by camera
    for platform in platforms:
        pygame.draw.rect(screen, (0, 255, 0), platform.move(-camera_x, 0)) # Adjust platform position by camera
    for item in items:
        pygame.draw.rect(screen, (255, 255, 0), item.move(-camera_x, 0)) # Adjust item position by camera


    # Display score
    display_score()

    # Update the screen
    pygame.display.flip()

    # Set frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()