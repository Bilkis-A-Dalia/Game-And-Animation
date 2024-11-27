import pygame
import time
import cv2
import numpy as np
import os
from IPython.display import clear_output

# set SDL to use the dummy NULL video driver,
#   so it doesn't need a windowing system.
os.environ["SDL_VIDEODRIVER"] = "dummy"

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))

done = False
is_blue = True
x, y = 30, 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw rectangle
    color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()

    # Convert image so it can be displayed in OpenCV
    view = pygame.surfarray.array3d(screen)
    
    # Convert from (width, height, channel) to (height, width, channel)
    view = np.transpose(view, (1, 0, 2))

    # Convert from RGB to BGR
    img_bgr = cv2.cvtColor(view, cv2.COLOR_RGB2BGR)

    # Display image using OpenCV
    cv2.imshow("Pygame Window in OpenCV", img_bgr)

    # Pause for 0.5 seconds
    time.sleep(0.5)

    # Break loop on 'q' press in OpenCV window
    #this condition to give the user a way to close or stop the program. Instead of forcefully closing the window or waiting for a specific even
    if cv2.waitKey(1) & 0xFF == ord('d'):
        done = True
clear_output()

# # # Clean up
# pygame.quit()
# cv2.destroyAllWindows()
