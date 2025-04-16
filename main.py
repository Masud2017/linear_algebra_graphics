import pygame
import sys
from  src.Matrix import Matrix
from pygame_widgets.button import Button
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Linear Algebra graphics project")
clock = pygame.time.Clock()

play_auto_button = Button(screen, 20, 50, 100, 50, text='Play Auto', onClick=lambda: print('Play Auto clicked!'))
rotate_x_text_box = TextBox(screen, 20, 120, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
rotate_right_and_left_slider = Slider(screen, 20,190, 200, 20, min=0, max=100, step=1, initial=50)
rotate_y_text_box = TextBox(screen, 20, 230, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
rotate_up_and_down_slider = Slider(screen, 20, 280, 200, 20, min=0, max=100, step=1, initial=50)
zoom_text_box = TextBox(screen, 20, 310, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
zoom_in_and_out_slider = Slider(screen, 20, 350, 200, 20, min=0, max=100, step=1, initial=50)
shear_text_box = TextBox(screen, 20, 380, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
shear_slider = Slider(screen, 20, 420, 200, 20, min=0, max=100, step=1, initial=50)
pygame.font.init() # you have to call this at the start, 
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Rotate right and left', False, (0, 0, 0))

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
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Increase the rotation angle for animation
    angle += 0.01

    # Clear the screen
    screen.fill(color = pygame.Color(44,66,43))
    pygame_widgets.update(events)
    
    play_auto_button.listen(events)
    rotate_right_and_left_slider.listen(events)
    rotate_up_and_down_slider.listen(events)
    screen.blit(text_surface, (20, 90))
    
    play_auto_button.draw()
    rotate_right_and_left_slider.draw()
    rotate_up_and_down_slider.draw()   
    rotate_x_text_box.setText("Rotate in x axis")
    rotate_y_text_box.setText("Rotate in y axis")
    zoom_text_box.setText("Zoom in and out")
    shear_text_box.setText("Shear ")
    

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
