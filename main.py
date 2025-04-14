import pygame
import math
import sys
from  src.Matrix import Matrix
# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3D Cube from Matrix in Pygame")
clock = pygame.time.Clock()

# Define the cube's vertices (a list of 3D points)
vertices = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
]

# Define the edges (pairs of indices into the vertices list)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]


# Perspective projection: Converts 3D coordinates into 2D coordinates.
def project(point, win_width, win_height, fov, viewer_distance):
    x, y, z = point
    factor = fov / (viewer_distance + z)
    x_proj = x * factor + win_width / 2
    y_proj = -y * factor + win_height / 2
    return (int(x_proj), int(y_proj))

# Parameters for projection
fov = 256  # Field of view
viewer_distance = 4  # How far the viewer is from the screen

# Main loop variables
angle = 0

while True:
    # Handle events (like quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Increase the rotation angle for animation
    angle += 0.01

    # Clear the screen
    screen.fill((0, 0, 0))

    # Transform and project all vertices
    projected_points = []
    for vertex in vertices:
        # Apply rotations
        rotated = Matrix.rotateX(vertex, angle)
        rotated = Matrix.rotateY(rotated, angle)
        rotated = Matrix.rotateZ(rotated, angle)
        
        # Project the 3D point to 2D screen coordinates
        projected = project(rotated, screen_width, screen_height, fov, viewer_distance)
        projected_points.append(projected)

    # Draw the edges by connecting the vertices
    for edge in edges:
        start, end = edge
        pygame.draw.line(screen, (255, 255, 255), projected_points[start], projected_points[end], 2)

    # Update the display and tick the clock
    pygame.display.flip()
    clock.tick(60)
