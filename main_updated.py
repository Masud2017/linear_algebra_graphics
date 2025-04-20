import pygame
import sys
from  src.Matrix import Matrix
from pygame_widgets.button import Button
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from src.operations import operations
from utils.util import apply_to_vertex,init_projection, apply_to_vertex_auto
from utils.util import project
# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Linear Algebra graphics project")
clock = pygame.time.Clock()


BUTTON_POS = 5
ZOOM_STATE = 5


# constants
play_auto = False

def start_auto():
    global play_auto
    play_auto = True
def stop_auto():
    global play_auto
    play_auto = False
play_auto_button = None
if play_auto:
    play_auto_button = Button(screen, 20, 50, 100, 50, text='Stop Auto', onClick=lambda: stop_auto())
    
else:
    play_auto_button = Button(screen, 20, 50, 100, 50, text='Play Auto', onClick=lambda: start_auto())



pygame.font.init() # you have to call this at the start, 
my_font = pygame.font.SysFont('Comic Sans MS', 30)
# text_surface = my_font.render('Rotate right and left', False, (0, 0, 0))

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
# edges = [
#     (0, 1), (1, 2), (2, 3), (3, 0),
#     (4, 5), (5, 6), (6, 7), (7, 4),
#     (0, 4), (1, 5), (2, 6), (3, 7)
# ]


faces = [
    (0, 1, 2, 3),  # back face
    (4, 5, 6, 7),  # front face
    (0, 1, 5, 4),  # bottom face
    (3, 2, 6, 7),  # top face
    (1, 2, 6, 5),  # right face
    (0, 3, 7, 4)   # left face
]

face_colors = [
    (255, 0, 0),     # Red        - back face
    (0, 255, 0),     # Green      - front face
    (0, 0, 255),     # Blue       - bottom face
    (255, 255, 0),   # Yellow     - top face
    (255, 0, 255),   # Magenta    - right face
    (0, 255, 255)    # Cyan       - left face
]


# Parameters for projection
fov = 256  # Field of view
viewer_distance = 4  # How far the viewer is from the screen

# Main loop variables
angle = 0

while True:
    # Handle events (like quitting)
    events = pygame.event.get()
    for event in events:
        mod = pygame.key.get_mods()
        if not play_auto:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("translating x axis")
                    projected_points = apply_to_vertex(vertices=vertices,
                                                    fov = fov,
                                                    viewer_distance=viewer_distance,
                                                    factor = BUTTON_POS,
                                                    projected_points=projected_points,
                                                    operation_type=operations.TRANSLATE_X)
                    BUTTON_POS -= 0.7
                    print(f"New value of up button pos : {BUTTON_POS}")
                if event.key == pygame.K_RIGHT:
                    # translate right
                    print("translating x axis")
                
                    projected_points = apply_to_vertex(vertices=vertices,
                                                    fov = fov,
                                                    viewer_distance=viewer_distance,
                                                    factor = BUTTON_POS,
                                                    projected_points=projected_points,
                                                    operation_type=operations.TRANSLATE_X)
                    BUTTON_POS += 0.7
                    print(f"New value of up button pos : {BUTTON_POS}")
                    
                
                if event.key == pygame.K_UP:
                    # translate down
                    # 
                    print("translating y axis")
                    projected_points = apply_to_vertex(vertices=vertices,
                                                    fov = fov,
                                                    viewer_distance=viewer_distance,
                                                    factor = BUTTON_POS,
                                                    projected_points=projected_points,
                                                    operation_type=operations.TRANSLATE_Y)
                    BUTTON_POS += 0.7
                    print(f"New value of up button pos : {BUTTON_POS}")
                    
                if event.key == pygame.K_DOWN:
                    print("translating y axis")
                    projected_points = apply_to_vertex(vertices=vertices,
                                                    fov = fov,
                                                    viewer_distance=viewer_distance,
                                                    factor = BUTTON_POS,
                                                    projected_points=projected_points,
                                                    operation_type=operations.TRANSLATE_Y)
                    BUTTON_POS -= 0.7
                    print(f"New value of up button pos : {BUTTON_POS}")
                    
            if event.type == pygame.MOUSEWHEEL:
                print("Started zooming...")
                
                print("VAlue of mouse wheell : ",pygame.mouse.get_pos())
                projected_points = apply_to_vertex(vertices=vertices,
                                                fov = fov,
                                                viewer_distance=viewer_distance,
                                                factor = ZOOM_STATE,
                                                projected_points=projected_points,
                                                operation_type=operations.ZOOM)
                if event.y < 0:
                    if ZOOM_STATE < 0.5:
                        continue
                    ZOOM_STATE = ZOOM_STATE - 2
                
                else:
                    if ZOOM_STATE > 4 and ZOOM_STATE < 5:
                        continue
                    ZOOM_STATE = ZOOM_STATE + 2
                    

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Increase the rotation angle for animation
    screen.fill(color = pygame.Color(44,66,43))
    pygame_widgets.update(events)
    
    angle += 0.01
    
    if not play_auto:
        init_projection(vertices=vertices, fov = fov, viewer_distance=viewer_distance,projected_points=projected_points)
    play_auto_button.listen(events)
    if play_auto:
        projected_points = []
        for vertex in vertices:
            rotated = vertex
            rotated = Matrix.rotateX(rotated, angle=angle)
            rotated = Matrix.rotateY(rotated, angle=angle)
            rotated = Matrix.rotateZ(rotated, angle=angle)
            
            projected_points.append(project(rotated, fov = fov, viewer_distance=viewer_distance,win_height=screen_height, win_width=screen_width))
        
        for i, face in enumerate(faces):
            point_list = [projected_points[i] for i in face]
            pygame.draw.polygon(screen, face_colors[i], point_list)
            # 3. Draw small rectangles at each projected vertex
        for point in projected_points:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(point[0]-3, point[1]-3, 6, 6))


    # Update the display and tick the clock
    pygame.display.flip()
    clock.tick(60)
