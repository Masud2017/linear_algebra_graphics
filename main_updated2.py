import pygame
import sys
from  src.Matrix import Matrix
from pygame_widgets.button import Button
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from utils.util import init_projection
from utils.util import project
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Linear Algebra graphics project")
clock = pygame.time.Clock()
play_auto = False


# widget section started
rotate_x_text_box = TextBox(screen, 20, 120, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
rotate_right_and_left_slider = Slider(screen, 20,190, 200, 20, min=0, max=100, step=1, initial=50)
rotate_y_text_box = TextBox(screen, 20, 230, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
rotate_up_and_down_slider = Slider(screen, 20, 280, 200, 20, min=0, max=100, step=1, initial=50)
zoom_text_box = TextBox(screen, 20, 310, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
zoom_in_and_out_slider = Slider(screen, 20, 350, 200, 20, min=0.1, max=5, step=0.5, initial=2.5)
shear_text_box = TextBox(screen, 20, 380, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
shear_slider = Slider(screen, 20, 420, 200, 20, min=0.1, max=2, step=0.01, initial=1)

translate_x_text_box = TextBox(screen, 20, 460, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
translate_x_slider = Slider(screen, 20, 500, 200, 20, min=-5, max=5, step=0.7, initial=0)
translate_y_text_box = TextBox(screen, 20, 540, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
translate_y_slider = Slider(screen, 20, 580, 200, 20, min=-5, max=5, step=0.7, initial=0)
# widget section ended

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

zoom_state = [1,1,1]

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

projected_points = []
init_projection(vertices=vertices, fov = fov, viewer_distance=viewer_distance, projected_points=projected_points)

# manual transformation :
x_translation_value = 1
y_translation_value = 1

def start_auto():
    global play_auto
    play_auto = True
def stop_auto():
    global play_auto
    play_auto = False
play_auto_button = None



while True:
    if play_auto:
        play_auto_button = Button(screen, 20, 50, 100, 50, text='Stop Auto', onClick=lambda: stop_auto())
    
    else:
        play_auto_button = Button(screen, 20, 50, 100, 50, text='Play Auto', onClick=lambda: start_auto())
    
    
    # initializing the proejcted_points
    
    # Handle events (like quitting)
    events = pygame.event.get()
    for event in events:
        
        # mod = pygame.key.get_mods()
        
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         projected_points = []
        #         for vertex in vertices:
        #             rotated = vertex
        #             rotated = Matrix.translate(vertex,x_translation_value)
                    
        #             projected_points.append(project(rotated, fov = fov, viewer_distance=viewer_distance,win_height=screen_height, win_width=screen_width))
        #             x_translation_value -= 0.01
            
        #     if event.key == pygame.K_RIGHT:
        #         projected_points = []
        #         for vertex in vertices:
        #             rotated = vertex
        #             rotated = Matrix.translate(vertex,x_translation_value)
                    
        #             projected_points.append(project(rotated, fov = fov, viewer_distance=viewer_distance,win_height=screen_height, win_width=screen_width))
        #             x_translation_value += 0.01
                    
        #     if event.key == pygame.K_UP:
        #         projected_points = []
        #         for vertex in vertices:
        #             rotated = vertex
        #             rotated = Matrix.translate(vertex,dy = y_translation_value)
                    
        #             projected_points.append(project(rotated, fov = fov, viewer_distance=viewer_distance,win_height=screen_height, win_width=screen_width))
        #             y_translation_value += 0.01
                    
        #     if event.key == pygame.K_DOWN:
        #         projected_points = []
        #         for vertex in vertices:
        #             rotated = vertex
        #             rotated = Matrix.translate(vertex,dy = y_translation_value)
                    
        #             projected_points.append(project(rotated, fov = fov, viewer_distance=viewer_distance,win_height=screen_height, win_width=screen_width))
        #             y_translation_value -= 0.01
                    
                    
                    
        # if event.type == pygame.MOUSEWHEEL:
        #     print(f"Mouse button is pressed")

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Increase the rotation angle for animation
    screen.fill(color = pygame.Color(44,66,43))
    pygame_widgets.update(events)

    play_auto_button.listen(events=events)
    play_auto_button.draw()
    
    # rendering all the widgets
    rotate_right_and_left_slider.listen(events)
    rotate_up_and_down_slider.listen(events)
    
    rotate_right_and_left_slider.draw()
    rotate_up_and_down_slider.draw()   
    translate_x_slider.draw()
    translate_y_slider.draw()
    rotate_x_text_box.setText("Rotate in x axis")
    rotate_y_text_box.setText("Rotate in y axis")
    zoom_text_box.setText("Zoom in and out")
    shear_text_box.setText("Shear ")
    translate_x_text_box.setText("Translate x axis")
    translate_y_text_box.setText("Translate y axis")
    # widget rendering section ended
    
    angle += 0.01
    # projected_points = []
    # if not play_auto:
    #     init_projection(vertices=vertices, fov = fov, viewer_distance=viewer_distance,projected_points=projected_points)
    play_auto_button.listen(events)
    if play_auto:
        projected_points = []
        for vertex in vertices:
            rotated = vertex
            rotated = Matrix.translate(rotated, dx = translate_x_slider.getValue())
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

    else:
        for i, face in enumerate(faces):
            point_list = [projected_points[i] for i in face]
            pygame.draw.polygon(screen, face_colors[i], point_list)
            # 3. Draw small rectangles at each projected vertex
        for point in projected_points:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(point[0]-3, point[1]-3, 6, 6))


    # Update the display and tick the clock
    pygame.display.flip()
    clock.tick(60)


