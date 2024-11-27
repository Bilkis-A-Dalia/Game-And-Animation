import pygame

pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Doraemon Character")

# Load the Doraemon image
doraemon_image = pygame.image.load('character_sprite_sheet.png').convert_alpha()  # Replace with your image file name

# Scale the image to a larger size
character_width = 128  # Adjust width for a larger character
character_height = 128  # Adjust height for a larger character
doraemon_image = pygame.transform.scale(doraemon_image, (character_width, character_height))

# Player state
player = pygame.Rect(100, 500, character_width, character_height)
player_velocity = [0, 0]  # [x_velocity, y_velocity]
gravity = 0.5
jump_strength = -15  # Stronger jump for larger character
walk_speed = 5
run_speed = 10

# Movement states
is_walking = False
is_running = False
is_jumping = False

# Handle player input
def handle_input():
    global is_walking, is_running, is_jumping, player_velocity
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_velocity[0] = -walk_speed if not keys[pygame.K_LSHIFT] else -run_speed
        is_walking = True
        is_running = keys[pygame.K_LSHIFT]
    elif keys[pygame.K_RIGHT]:
        player_velocity[0] = walk_speed if not keys[pygame.K_LSHIFT] else run_speed
        is_walking = True
        is_running = keys[pygame.K_LSHIFT]
    else:
        player_velocity[0] = 0
        is_walking = False
        is_running = False

    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        player_velocity[1] = jump_strength

# Apply gravity
def apply_gravity():
    global is_jumping
    player_velocity[1] += gravity
    player.y += player_velocity[1]
    player.x += player_velocity[0]

    # Ground collision
    if player.y >= 500:  # Ground level
        player.y = 500
        player_velocity[1] = 0
        is_jumping = False

    # Prevent going out of bounds horizontally
    if player.x < 0:
        player.x = 0
    elif player.x > screen_width - player.width:
        player.x = screen_width - player.width

# Draw the player
def draw_player():
    screen.blit(doraemon_image, player)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input and physics
    handle_input()
    apply_gravity()

    # Clear the screen
    screen.fill((135, 206, 235))  # Background color (sky blue)

    # Draw the player
    draw_player()

    # Update the screen
    pygame.display.flip()

    # Set frame rate
    clock.tick(60)

pygame.quit()