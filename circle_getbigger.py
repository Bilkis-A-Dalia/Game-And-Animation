import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption('Draw Circles with Independent Sizes')

# Define colors
color = (200, 155, 65)
radius_increment = 5  # Amount to increase the radius with each click
points = []  # List to store circle positions
radii = []   # List to store circle radii

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Store the position of the click
            points.append(event.pos)  
            # Append the next radius to the radii list
            if len(radii) == 0:
                radii.append(radius_increment)  # Start with radius 5
            else:
                radii.append(radii[-1] + radius_increment)  # Increase radius

    # Fill the screen with a white background
    screen.fill((255, 255, 255))

    # Draw circles at each stored point with their corresponding radius
    for point, radius in zip(points, radii):
        pygame.draw.circle(screen, color, point, radius)

    # Update the display
    pygame.display.flip()  # Use flip for double buffering
